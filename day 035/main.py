import requests
import datetime as dt



STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHA_API_KEY = 'QZRP3ZOY7JWHDFSQ'
NEWS_API_KEY = 'cc9ad879371f40c4b6b4296c28822966'


ALPHAVANTAGE_URL = f'https://www.alphavantage.co/query?'
NEWS_URL = 'https://newsapi.org/v2/everything?q=keyword&apiKey=cc9ad879371f40c4b6b4296c28822966'

stock_params ={
    'function':'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': ALPHA_API_KEY
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





