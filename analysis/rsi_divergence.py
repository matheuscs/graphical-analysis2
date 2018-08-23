import pandas as pd


def find_oversold(dataframe, oversold=30):
    index = dataframe.index.values
    closes = dataframe['Close'].values.tolist()
    rsis = dataframe['RSI'].values.tolist()
    os_index = []
    os_data = []
    for i in range(len(index)):
        if rsis[i] < oversold:
            os_index.append(index[i])
            os_data.append([closes[i], rsis[i]])

    return pd.DataFrame(os_data, index=os_index, columns=['Close', 'RSI'])


def find_rsi_divergence(dataframe):
    """Looks in the data series for rsi divergence."""
    rsis = dataframe['RSI'].values.tolist()
    closes = dataframe['Close'].values.tolist()
    rsi_divergences_dates = []
    for i in range(len(dataframe)):
        for j in range(i, len(dataframe)):
            if closes[j] > closes[i] and rsis[j] < rsis[i]:
                diff_closes = ((closes[j] / closes[i]) - 1) * 100
                diff_rsi = ((rsis[i] / rsis[j]) - 1) * 100
                rsi_divergences_dates.append(
                    (dataframe.index.values[i],
                     closes[i],
                     rsis[i],
                     dataframe.index.values[j],
                     closes[j],
                     rsis[j],
                     format(diff_closes, '.2f'),
                     format(diff_rsi, '.2f')
                     )
                )
    return rsi_divergences_dates
