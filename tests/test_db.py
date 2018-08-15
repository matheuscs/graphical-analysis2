from unittest import TestCase, mock
from helpers import db, constants
import sqlite3
import json
import helpers.finance_api as api


def mocked_make_api_request(_):
    with open(constants.MOCKED_DATA_PATH, 'r') as f:
        return json.load(f)


class TestDB(TestCase):
    def test_create_and_drop_table(self):
        self.assertFalse(db.drop_table())
        self.assertFalse(db.create_table())
        with self.assertRaises(sqlite3.OperationalError):
            db.create_table()

    @mock.patch('helpers.finance_api.make_api_request',
                side_effect=mocked_make_api_request)
    def test_bulk_insert(self, _):
        stock_data = api.dataframe_from_request_output(
            api.make_api_request('bbas3'), 20)
        db.bulk_insert(stock_data)

    def test_read(self):
        self.assertEqual(
            len(db.read('bbas3', 20)), 0)
