import os

API_KEY = os.environ['ALPHAVANTAGE_API_KEY']
API_URL = 'https://www.alphavantage.co/query?function=' \
          'TIME_SERIES_DAILY&symbol={}.SA&apikey={}&outputsize=full'\
    .format('{}', API_KEY)
