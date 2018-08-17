import sqlite3
import pandas as pd

from helpers import constants


def create_table():
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
            PRIMARY KEY (symbol, date)
    );
    """)
    conn.close()


def drop_table():
    conn = sqlite3.connect(constants.DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS stocks")
    conn.commit()
    conn.close()


def bulk_insert(stock_data):
    data = []
    for index, row in stock_data.iterrows():
        data.append(('bbas3', index, row[0], row[1], row[2], row[3], row[4]))

    conn = sqlite3.connect(constants.DB_PATH)
    cursor = conn.cursor()
    cursor.executemany("""
    INSERT OR IGNORE INTO stocks (symbol, date, open, high, low, close, volume)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, data)
    conn.commit()
    conn.close()


def read(symbol, output_size):
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
        data.append([row[2], row[3], row[4], row[5], row[6]])
        if len(index) == output_size:
            break
    conn.close()

    return pd.DataFrame(data, index=index,
                        columns=['Open', 'High', 'Low', 'Close', 'Volume'])


def delete_all():
    conn = sqlite3.connect(constants.DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM stocks')
    conn.commit()
    conn.close()
