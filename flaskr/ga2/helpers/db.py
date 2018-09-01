import sqlite3
import pandas as pd

from ..helpers import constants


def create_table():
    """Create stock values database."""
    conn = sqlite3.connect(constants.DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE stocks (
            symbol VARCHAR(6) NOT NULL,
            date VARCHAR(10) NOT NULL,
            open NUMERIC NOT NULL,
            high NUMERIC NOT NULL,
            low NUMERIC NOT NULL,
            close NUMERIC NOT NULL,
            volume NUMERIC NOT NULL,
            rsi NUMERIC,
            PRIMARY KEY (symbol, date)
    );
    """)
    conn.close()


def drop_table():
    """Drop stock values database."""
    conn = sqlite3.connect(constants.DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS stocks")
    conn.commit()
    conn.close()


def bulk_insert(stock_symbol, stock_data):
    """Insert dataframed stock values into the database."""
    data = []
    for index, row in stock_data.iterrows():
        r5 = 0
        if len(row) == 6:
            r5 = row[5]
        data.append(
            (stock_symbol, index, row[0], row[1], row[2], row[3], row[4], r5)
        )

    conn = sqlite3.connect(constants.DB_PATH)
    cursor = conn.cursor()
    cursor.executemany("""
    INSERT OR IGNORE INTO stocks
        (symbol, date, open, high, low, close, volume, rsi)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, data)
    conn.commit()
    conn.close()


def read(symbol, output_size):
    """Read specified symbol limited to the indicated output size."""
    conn = sqlite3.connect(constants.DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM stocks
    WHERE symbol=?
    """, (symbol, ))
    index = []
    data = []
    for row in cursor.fetchall():
        index.append(row[1])
        data.append([row[2], row[3], row[4], row[5], row[6], row[7]])
        if len(index) == output_size:
            break
    conn.close()

    return pd.DataFrame(data, index=index,
                        columns=['Open', 'High', 'Low', 'Close', 'Volume',
                                 'RSI'])


def delete_all():
    """Delete all data from the database."""
    conn = sqlite3.connect(constants.DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM stocks')
    conn.commit()
    conn.close()
