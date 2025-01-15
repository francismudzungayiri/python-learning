import requests
import datetime as dt
from twilio.rest import Client





STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHA_API_KEY = 'QZRP3ZOY7JWHDFSQ'
NEWS_API_KEY = 'cc9ad879371f40c4b6b4296c28822966'


ALPHAVANTAGE_URL = f'https://www.alphavantage.co/query?'
NEWS_URL = 'https://newsapi.org/v2/everything?'

stock_params ={
    'function':'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': ALPHA_API_KEY
}

news_params = {
    'qInTitle' : COMPANY_NAME,
    'apiKey': NEWS_API_KEY
}
response = requests.get(ALPHAVANTAGE_URL, params= stock_params)
response.raise_for_status()

data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']

#the day before yesterday
day_before_yesterday = data_list[1]
day_before_yesterday_price = day_before_yesterday['4. close']

print(yesterday_closing_price)
print(day_before_yesterday_price)

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_price))

diff_percent = (difference / float(yesterday_closing_price)) * 100
if diff_percent > 1:
    #Get news
    news_response = requests.get(NEWS_URL, params= news_params)
    articles = news_response.json()['articles']
    
    #three article
    three_articles = articles[:3] 
    
    formatted_articles = [f"Headline: {article['title']}. \n Brief: {article['description']}" for article in three_articles]
    
    #send message using twilio
    
    account_ssid = ''
    account_auth = ''

    client = Client(account_ssid, account_auth)

    twilio_number = ''
    my_number = '+263783976834'
    
    for article in formatted_articles:
        message = client.messages.create(
            body="Hello from Francis I am learning how to send sms using python code",
            from_= twilio_number,
            to= my_number
        )

    print(message.sid)




