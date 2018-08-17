
def get_body_size(row):
    return abs(row['Open'] - row['Close'])


def get_upper_shadow_size(row):
    return row['High'] - max(row['Open'], row['Close'])


def get_lower_shadow_size(row):
    return min(row['Open'], row['Close']) - row['Low']
