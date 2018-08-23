
def get_body_size(row):
    """Candlestick body size."""
    return abs(row['Open'] - row['Close'])


def get_upper_shadow_size(row):
    """Upper shadow size."""
    return row['High'] - max(row['Open'], row['Close'])


def get_lower_shadow_size(row):
    """Lower shadow size."""
    return min(row['Open'], row['Close']) - row['Low']
