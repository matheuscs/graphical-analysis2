from unittest import TestCase, mock, main
from helpers import db, constants
import os
import sqlite3
import json
import helpers.finance_api as api


def mocked_make_api_request(_):
    with open(constants.MOCKED_DATA_PATH, 'r') as f:
        return json.load(f)


class TestDB(TestCase):
    @mock.patch('helpers.finance_api.make_api_request',
                side_effect=mocked_make_api_request)
    def test_create_drop_read_table(self, _):
        self.assertFalse(db.drop_table())
        self.assertFalse(db.create_table())
        with self.assertRaises(sqlite3.OperationalError):
            db.create_table()
        stock_data = api.dataframe_from_request_output(
            api.make_api_request('bbas3'), 20)
        self.assertFalse(db.bulk_insert(stock_data))
        self.assertEqual(
            len(db.read('bbas3', 10)), 10)
