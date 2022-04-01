# Stock News Monitoring Program

import requests
from twilio.rest import Client

STOCK_NAME = "AMZN"
COMPANY_NAME = "Amazon.com, Inc."

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "ZAW4CJ7WI675DQKG"
NEWS_API_KEY = "4a48f22aeab44956a3ed89902a9e5b96 "

TWILIO_SID = "ACd64c2f1f1661ab17ed8978de3442d32c"
TWILIO_AUTH_TOKEN = "0ee4954ed22e28883f0d42cce40473d9"

# Get yesterday's closing stock price.
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (difference / float(yesterday_closing_price)) * 100
print(diff_percent)

if diff_percent > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    print(articles)

    # Use Python slice operator to create a list that contains the first 3 articles.
    three_articles = articles[:3]
    print(three_articles)

    # Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']} " for
        article in three_articles]

    # Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+12184383451',
            to='+919163218832'
        )
