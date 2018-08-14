import os

API_FILE_KEY = './data/api_key.txt'

if os.path.isfile(API_FILE_KEY):
    with open(API_FILE_KEY, 'r') as f:
        API_KEY = f.read()

    API_URL = 'https://www.alphavantage.co/query?function=' \
              'TIME_SERIES_DAILY_ADJUSTED&symbol={}.SA&apikey={}'\
        .format('{}', API_KEY)
