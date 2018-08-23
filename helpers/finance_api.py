import pandas as pd
import requests
import json
from helpers import constants


def request_stock_values(stock_symbol):
    return json.loads(requests.get(constants.STOCK_VALUES_API
                                   .format(stock_symbol)).text)


def request_rsi(stock_symbol):
    return json.loads(requests.get(constants.RSI_API.format(stock_symbol)).text)


def stock_values_as_dataframe(stock_values, output_size):
    time_series = stock_values['Time Series (Daily)']
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


def rsi_as_dataframe(rsi, output_size):
    time_series = rsi['Technical Analysis: RSI']
    index = []
    data = []

    for day in time_series:
        index.append(day)
        data.append([float(time_series[day]['RSI'])])

        if len(index) == output_size:
            break

    return pd.DataFrame(data, index=index, columns=['RSI'])


def add_rsi_to_dataframe(stock_values_df, rsi_df):
    return stock_values_df.join(rsi_df)

