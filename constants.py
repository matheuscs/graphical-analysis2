with open('./data/api_key.txt', 'r') as f:
    API_KEY = f.read()

API_URL = 'https://www.alphavantage.co/query?function=' \
          'TIME_SERIES_DAILY_ADJUSTED&symbol={}.SA&apikey={}'\
    .format('{}', API_KEY)
