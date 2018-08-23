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


def find_rsi_divergence(dataframe, max_window=10):
    """Looks in the data series for rsi divergence."""
    pass
