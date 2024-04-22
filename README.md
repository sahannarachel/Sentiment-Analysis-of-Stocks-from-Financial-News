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




