from unittest import TestCase
from helpers import finance_api as api
from analysis import rsi_divergence as diver
from tests.test_db import mocked_request_stock_values, mocked_request_rsi


class TestRSIDIvergence(TestCase):
    @classmethod
    def setUpClass(cls):
        sv = api.stock_values_as_dataframe(
            mocked_request_stock_values('hbor3'), 90)
        rsi = api.rsi_as_dataframe(mocked_request_rsi('hbor3'), 90)
        cls.dataframe = api.add_rsi_to_dataframe(sv, rsi)

    # def test_find_oversold(self):
    #     print(diver.find_oversold(self.dataframe))

    def test_find_rsi_divergence(self):
        print(diver.find_rsi_divergence(diver.find_oversold(self.dataframe)))
