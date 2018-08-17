import pandas as pd


def find_rsi(df, time_frame=14):
    if type(df) is not pd.DataFrame:
        raise TypeError(f'First parameter must be pd.DataFrame. '
                        f'Found {type(df)}')

    if len(df) < time_frame:
        raise ValueError(f'DataFrame length must be greater than or equal to '
                         f'time_frame. '
                         f'Found dataframe: {df}, time_frame: {time_frame}')
    if time_frame <= 2:
        raise ValueError(f'time_frame must be greater than 2')

