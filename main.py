import os
import requests
from dotenv import load_dotenv

load_dotenv()


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"



STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")


stock_params ={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY

}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()

if "Time Series (Daily)" not in data:
    print("\n❌ API Error or Rate Limit Exceeded!")
    if "Information" in data:
        clean_msg = data["Information"].replace(str(STOCK_API_KEY), "[REDACTED_KEY]")
        print(f"Details: {clean_msg}")
    else:
        print(f"Raw Response received: {data}")
    exit()


daily_data = data["Time Series (Daily)"]

data_list = [value for (key, value) in daily_data.items()]

yesterday_closing_data = float(data_list[0]["4. close"])    

day_before_yesterday_closing_data = float(data_list[1]["4. close"]) 


difference = yesterday_closing_data-day_before_yesterday_closing_data

up_down = "🔺" if difference > 0 else "🔻"

diff_percent = round((abs(difference)/day_before_yesterday_closing_data) * 100)

if diff_percent >=1:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    

    for article in three_articles:
            message_body = (
                f"{STOCK}: {up_down}{diff_percent}%\n"
                f"Headline: {article['title']}\n"
                f"Brief: {article['description']}\n"
            )
            print(message_body)
            print("-" * 40)
else:
    print(f"Market fluctuation ({diff_percent}%) did not reach the threshold target limit.")



 

