import pandas as pd
import requests
import json
from helpers import constants


def make_api_request(stock_symbol):
    return json.loads(requests.get(constants.API_URL.format(stock_symbol)).text)


def dataframe_from_request_output(api_request, output_size):
    time_series = api_request['Time Series (Daily)']
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
