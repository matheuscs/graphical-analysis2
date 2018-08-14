import pandas as pd
import requests
import json
import constants


def make_api_request(stock_symbol):
    return json.loads(requests.get(constants.API_URL.format(stock_symbol)).text)


def get_stock_data(stock_symbol, output_size):
    time_series = make_api_request(stock_symbol)['Time Series (Daily)']
    index = []
    data = []

    for day in time_series:
        index.append(day)
        data.append([float(time_series[day]['1. open']),
                     float(time_series[day]['2. high']),
                     float(time_series[day]['3. low']),
                     float(time_series[day]['4. close']),
                     float(time_series[day]['5. volume'])])

        if len(index) == output_size:
            break

    return pd.DataFrame(data, index=index,
                        columns=['Open', 'High', 'Low', 'Close', 'Volume'])
