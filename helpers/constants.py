import os

API_KEY = os.environ['ALPHAVANTAGE_API_KEY']
API_URL = 'https://www.alphavantage.co/query'

STOCK_VALUES_API = '{}?function=TIME_SERIES_DAILY&symbol={}.SA&' \
                   'apikey={}&outputsize=full'.format(API_URL, '{}', API_KEY)
RSI_API = '{}?function=RSI&symbol={}.SA&interval=daily&time_period=14&' \
          'series_type=close&apikey={}'.format(API_URL, '{}', API_KEY)

MOCKED_STOCK_VALUES_PATH = './data/mocked_stock_values_{}.txt'
MOCKED_RSI_PATH = './data/mocked_rsi_{}.txt'
DB_PATH = './data/stocks.db'
