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


def find_rsi_divergence(df):
    """Looks in the data series for rsi divergence."""
    rsis = df['RSI'].values.tolist()
    closes = df['Close'].values.tolist()
    rsi_divergences_dates = []
    for i in range(len(df)):
        for j in range(i, len(df)):
            if closes[j] > closes[i] and rsis[j] < rsis[i]:
                diff_closes = ((closes[j] / closes[i]) - 1) * 100
                diff_rsi = ((rsis[i] / rsis[j]) - 1) * 100
                rsi_divergences_dates.append(
                    (
                        df.index.values[j],
                        closes[j],
                        rsis[j],
                        df.index.values[i],
                        closes[i],
                        rsis[i],
                        format(diff_closes, '.2f'),
                        format(diff_rsi, '.2f')
                    )
                )

    return pd.DataFrame(rsi_divergences_dates,
                        columns=['Date1', 'Close1', 'RSI1',
                                 'Date2', 'Close2', 'RSI2',
                                 'Close Diff %', 'RSI Diff %'])


def highlight_rsi_divergences(df):
    return df['Date2'].value_counts()
