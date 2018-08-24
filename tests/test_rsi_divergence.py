from unittest import TestCase

from analysis.rsi_divergence import find_oversold, find_rsi_divergence, \
    highlight_rsi_divergences
from helpers import finance_api as api

from tests.test_db import mocked_request_stock_values, mocked_request_rsi


class TestRSIDIvergence(TestCase):
    @classmethod
    def setUpClass(cls):

        sv = api.stock_values_as_dataframe(
            # mocked_request_stock_values('hbor3'), 60)
            api.request_stock_values('itub4'), 120)
        # rsi = api.rsi_as_dataframe(mocked_request_rsi('hbor3'), 60)
        rsi = api.rsi_as_dataframe(api.request_rsi('itub4'), 120)
        cls.stock_df = api.add_rsi_to_dataframe(sv, rsi)

    def test_find_oversold(self):
        df = find_oversold(self.stock_df)
        self.assertEqual(len(list(df)), 2)

    def test_find_rsi_divergence(self):
        df = find_rsi_divergence(find_oversold(self.stock_df))
        self.assertEqual(len(list(df)), 8)
        print(df)

    def test_highlight_rsi_divergences(self):
        df = find_rsi_divergence(find_oversold(self.stock_df))
        print(highlight_rsi_divergences(df))
