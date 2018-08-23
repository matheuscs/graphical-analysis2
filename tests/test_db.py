from unittest import TestCase, mock
from helpers import db, constants
import sqlite3
import json
import helpers.finance_api as api


def mocked_request_stock_values(_):
    with open(constants.MOCKED_STOCK_VALUES_PATH, 'r') as f:
        return json.load(f)


class TestDB(TestCase):
    @mock.patch('helpers.finance_api.request_stock_values',
                side_effect=mocked_request_stock_values)
    def test_create_drop_read_table(self, _):
        self.assertFalse(db.drop_table())
        self.assertFalse(db.create_table())
        with self.assertRaises(sqlite3.OperationalError):
            db.create_table()
        dataframe = api.stock_values_as_dataframe(
            api.request_stock_values('bbas3'), 20)
        self.assertFalse(db.bulk_insert(dataframe))
        self.assertEqual(len(db.read('bbas3', 10)), 10)
