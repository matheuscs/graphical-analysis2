from unittest import TestCase, mock
from helpers import db, constants
import sqlite3
import json
import helpers.finance_api as api


def mocked_request_stock_values(stock_symbol):
    with open(constants.MOCKED_STOCK_VALUES_PATH.format(
            stock_symbol), 'r') as f:
        return json.load(f)


def mocked_request_rsi(stock_symbol):
    with open(constants.MOCKED_RSI_PATH.format(stock_symbol), 'r') as f:
        return json.load(f)


class TestDB(TestCase):
    @mock.patch('helpers.finance_api.request_stock_values',
                side_effect=mocked_request_stock_values)
    def test_create_drop_read_table_stock_values(self, _):
        self.assertFalse(db.drop_table())
        self.assertFalse(db.create_table())
        with self.assertRaises(sqlite3.OperationalError):
            db.create_table()
        stock_symbol = 'bbas3'
        sv_df = api.stock_values_as_dataframe(
            api.request_stock_values(stock_symbol), 20)
        self.assertFalse(db.bulk_insert(stock_symbol, sv_df))
        self.assertEqual(len(db.read(stock_symbol, 10)), 10)
        self.assertEqual(db.read(stock_symbol, 10).size, 60)
        self.assertEqual(len(db.read('itub4', 10)), 0)
        self.assertEqual(db.read('itub4', 10).size, 00)

    @mock.patch('helpers.finance_api.request_stock_values',
                side_effect=mocked_request_stock_values)
    @mock.patch('helpers.finance_api.request_rsi',
                side_effect=mocked_request_rsi)
    def test_create_drop_read_table_rsi(self, _, __):
        self.assertFalse(db.drop_table())
        self.assertFalse(db.create_table())
        with self.assertRaises(sqlite3.OperationalError):
            db.create_table()
        stock_symbol = 'hbor3'
        sv_df = api.stock_values_as_dataframe(
            api.request_stock_values(stock_symbol), 20)
        rsi_df = api.rsi_as_dataframe(
            api.request_rsi(stock_symbol), 20)
        df = api.add_rsi_to_dataframe(sv_df, rsi_df)
        self.assertFalse(db.bulk_insert(stock_symbol, df))
        self.assertEqual(len(db.read(stock_symbol, 10)), 10)
        self.assertEqual(db.read(stock_symbol, 10).size, 60)
        self.assertEqual(len(db.read('bbas3', 10)), 0)
        self.assertEqual(db.read('bbas3', 10).size, 00)
