import flask
from flask import Flask, render_template  # for web app
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
import plotly
import plotly.express as px
import json  # for graph plotting in website
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk


import nltk
import ssl

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Download NLTK data
nltk.download('vader_lexicon')

# Initialize SentimentIntensityAnalyzer with the path to the VADER lexicon
vader = SentimentIntensityAnalyzer(
    lexicon_file="/Users/reubenjoseph/Downloads/vader_lexicon.txt"
)


import ssl  # Import SSL

nltk.downloader.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Configure SSL
ssl._create_default_https_context = ssl._create_unverified_context

# for extracting data from finviz
finviz_url = 'https://finviz.com/quote.ashx?t='


import ssl
from urllib.request import urlopen, Request
    


def get_news(ticker):
    url = finviz_url + ticker
    try:
        req = Request(url=url,
                      headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'})
        response = urlopen(req)
        # Read the contents of the file into 'html'
        html = BeautifulSoup(response, 'html.parser')  # Specify the parser explicitly
        # Find 'news-table' in the Soup and load it into 'news_table'
        news_table = html.find(id='news-table')
        if news_table is None:
            raise ValueError("Couldn't find 'news-table' element in HTML.")
        return news_table
    except Exception as e:
        print("Error fetching news:", e)
        return None




# parse news into dataframe
import pandas as pd
from datetime import datetime


def parse_news(news_table):
    parsed_news = []

    for x in news_table.findAll('tr'):
        # read the text from each tr tag into text
        # get text from a only
        text = x.a.get_text()
        # split text in the td tag into a list
        date_scrape = x.td.text.split()
        # if the length of 'date_scrape' is 1, load 'time' as the only element

        if len(date_scrape) == 1:
            time = date_scrape[0]
            # For datetime strings like "Today 09:23AM", convert to standard format
            today_date = datetime.now().strftime('%Y-%m-%d')
            date = today_date
        else:
            if date_scrape[0] == 'Today':
                today_date = datetime.now().strftime('%Y-%m-%d')
                date = today_date
            else:
                date = pd.to_datetime(' '.join(date_scrape[:2])).strftime('%Y-%m-%d')
            time = date_scrape[-1]

        # Append ticker, date, time and headline as a list to the 'parsed_news' list
        parsed_news.append([date, time, text])

    # Set column names
    columns = ['date', 'time', 'headline']

    # Convert the parsed_news list into a DataFrame called 'parsed_and_scored_news'
    parsed_news_df = pd.DataFrame(parsed_news, columns=columns)

    # Create a pandas datetime object from the strings in 'date' and 'time' column
    parsed_news_df['datetime'] = pd.to_datetime(parsed_news_df['date'] + ' ' + parsed_news_df['time'])

    return parsed_news_df


def score_news(parsed_news_df):
    # Initialize SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()

    # Iterate through the headlines and get the polarity scores
    scores = parsed_news_df['headline'].apply(sia.polarity_scores)

    # Convert the scores into a DataFrame
    scores_df = pd.DataFrame(list(scores))

    # Merge the scores DataFrame with the parsed news DataFrame
    parsed_and_scored_news = pd.concat([parsed_news_df, scores_df], axis=1)

    # Convert the 'compound' column to numeric and rename it to 'sentiment_score'
    parsed_and_scored_news['sentiment_score'] = pd.to_numeric(parsed_and_scored_news['compound'], errors='coerce')

    # Drop unnecessary columns
    parsed_and_scored_news.drop(['neg', 'neu', 'pos', 'compound'], axis=1, inplace=True)

    # Convert the date and time columns to datetime
    parsed_and_scored_news['datetime'] = pd.to_datetime(parsed_and_scored_news['date'] + ' ' + parsed_and_scored_news['time'])

    # Set the 'datetime' column as the index
    parsed_and_scored_news.set_index('datetime', inplace=True)

    return parsed_and_scored_news


def plot_hourly_sentiment(parsed_and_scored_news, ticker):
    mean_scores = parsed_and_scored_news.resample('h').mean(numeric_only=True)
    mean_scores.dropna(inplace=True)  # Remove rows with missing values

    fig = px.bar(mean_scores, x=mean_scores.index, y='sentiment_score', title=ticker + ' Hourly Sentiment Scores')
    return fig

def plot_daily_sentiment(parsed_and_scored_news, ticker):
    mean_scores = parsed_and_scored_news.resample('D').mean(numeric_only=True)
    mean_scores.dropna(inplace=True)  # Remove rows with missing values

    fig = px.bar(mean_scores, x=mean_scores.index, y='sentiment_score', title=ticker + ' Daily Sentiment Scores')
    return fig

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sentiment', methods=['POST'])
def sentiment():
    ticker = flask.request.form['ticker'].upper()
    news_table = get_news(ticker)
    parsed_news_df = parse_news(news_table)
    parsed_and_scored_news = score_news(parsed_news_df)
    fig_hourly = plot_hourly_sentiment(parsed_and_scored_news, ticker)
    fig_daily = plot_daily_sentiment(parsed_and_scored_news, ticker)

    graphJSON_hourly = json.dumps(fig_hourly, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON_daily = json.dumps(fig_daily, cls=plotly.utils.PlotlyJSONEncoder)

    header = "Hourly and Daily Sentiment of {} Stock".format(ticker)
    description = """
	    The above chart averages the sentiment scores of {} stock hourly and daily.
	The table below gives each of the most recent headlines of the stock and the negative, neutral, positive and an aggregated sentiment score.
	The news headlines are obtained from the FinViz website.
	Sentiments are given by the nltk.sentiment.vader Python library.
    """.format(ticker)
    return render_template('sentiment.html', graphJSON_hourly=graphJSON_hourly, graphJSON_daily=graphJSON_daily,
                           header=header, table=parsed_and_scored_news.to_html(classes='data'), description=description)


if __name__ == '__main__':
    app.run()