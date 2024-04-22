# Sentiment-Analysis-of-Stocks-from-Financial-News
Using python 

Extract stock sentiments on financial news headlines, plot the hourly/daily sentiments in a Flask web app and deploy it online.

# Project Directory Structure

```
stock_sentiment_webapp/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── templates/
│   │   ├── index.html
│   │   └── sentiment.html
│   └── static/
│       └── style.css
│
├── data/
│   ├── apple-computers.txt
│   └── apple-fruit.txt
│
├── requirements.txt
└── run.py
```




#Here's a brief explanation of the structure:

1. app/: Contains the Flask application files.
2. __init__.py: Initializes the Flask application.
3. routes.py: Defines the routes and views for the application.
4. templates/: Contains HTML templates for rendering pages.
5. static/: Contains static files such as CSS stylesheets.
6. data/: Contains text files with data related to Apple Inc. and apple fruit.
7. requirements.txt: Lists the required Python packages for the project.
8. run.py: Script to run the Flask application.

# Flask Application Structure:

The `app` directory contains all application-related files.

- `__init__.py` initializes the Flask application.
- `routes.py` contains the route definitions.
- HTML templates are stored in the `templates` directory.
- Static files like CSS are stored in the `static` directory.

## Data Directory:

The `data` directory stores text files containing information about Apple Inc. and the fruit.

## Requirements File:

`requirements.txt` lists all the Python packages required by the application.

## Run Script:

`run.py` is the script to run the Flask application.





# Workflow of the Code

1. **Import Necessary Libraries:**
   - Import required libraries such as Flask, BeautifulSoup, pandas, plotly, nltk, etc.
   
2. **Configure SSL and Download NLTK Data:**
   - Configure SSL to handle secure connections.
   - Download NLTK data required for sentiment analysis.
   
3. **Define Functions:**
   - `get_news(ticker)`: Fetches news headlines for a given stock ticker from the FinViz website.
   - `parse_news(news_table)`: Parses the raw HTML news table into a pandas DataFrame.
   - `score_news(parsed_news_df)`: Scores each headline in the DataFrame using the VADER sentiment analyzer.
   - `plot_hourly_sentiment(parsed_and_scored_news, ticker)`: Plots the hourly sentiment scores of the stock.
   - `plot_daily_sentiment(parsed_and_scored_news, ticker)`: Plots the daily sentiment scores of the stock.
   
4. **Create Flask Application:**
   - Initialize the Flask application.
   
5. **Define Routes:**
   - Define two routes:
     - `/`: Renders the index page.
     - `/sentiment`: Handles the sentiment analysis request and renders the sentiment page.
     
6. **Define Route Functions:**
   - `index()`: Renders the index page containing the form to input the stock ticker.
   - `sentiment()`: Handles the sentiment analysis request, fetches news data, performs sentiment analysis, and renders the sentiment page with charts and news headlines.
   
7. **Run the Application:**
   - Start the Flask application if the script is executed directly.
8. **HTML Templates and Static Files:**
   - **Templates Directory:**
     - Contains HTML templates for rendering web pages.
     - `index.html`: Provides a form to input the stock ticker.
     - `sentiment.html`: Displays sentiment analysis results with charts and news headlines.
   - **Static Directory:**
     - Contains static files such as CSS stylesheets.
     - `style.css`: Defines styles for the web pages.
   
9. **Data Directory:**
   - Contains text files with information about Apple Inc. and the fruit.
   - `apple-computers.txt`: Text file containing information about Apple Inc.
   - `apple-fruit.txt`: Text file containing information about the apple fruit.
   
10. **Requirements File:**
    - `requirements.txt`: Lists all the Python packages required by the application.

11. **Run Script:**
    - `run.py`: Script to run the Flask application.

12. **Execution:**
    - When the script is executed, it starts the Flask application.
    - Users can access the application through a web browser.
    - They can input a stock ticker to view sentiment analysis results.
    - 
13. **Flask Application Structure:**
    - The `app` directory contains all application-related files.
    - `__init__.py` initializes the Flask application.
    - `routes.py` contains the route definitions.
    
14. **Parsing and Sentiment Analysis:**
    - The `get_news()` function extracts news headlines from the FinViz website for a given stock ticker.
    - The `parse_news()` function parses the HTML content of news headlines into a DataFrame.
    - The `score_news()` function assigns sentiment scores to each headline using the NLTK Vader library.
    
15. **Plotting Sentiment Scores:**
    - The `plot_hourly_sentiment()` function plots hourly sentiment scores using Plotly.
    - The `plot_daily_sentiment()` function plots daily sentiment scores using Plotly.

16. **Flask Routes:**
    - The `/` route renders the index.html template, which displays the input form.
    - The `/sentiment` route processes the form submission, retrieves sentiment analysis results, and renders the sentiment.html template.

17. **User Interaction:**
    - Users input a stock ticker in the index.html form.
    - Upon submission, the Flask application retrieves news headlines and performs sentiment analysis.
    - The sentiment analysis results, along with interactive charts and news headlines, are displayed in the sentiment.html template.

18. **Deployment:**
    - The Flask application can be deployed locally for testing and development purposes.
    - It can also be deployed to a web server to make it accessible over the internet.

19. **Usage:**
    - Users can access the web application through a web browser.
    - They input a stock ticker and receive sentiment analysis results in graphical and tabular formats.

20. **Dependencies:**
    - The application requires various Python packages, including Flask, BeautifulSoup, pandas, Plotly, and NLTK.
    - These dependencies are listed in the requirements.txt file for easy installation.





