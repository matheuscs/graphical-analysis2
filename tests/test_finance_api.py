from unittest import TestCase
from helpers import finance_api as api


class TestFinanceAPI(TestCase):
    def test_make_api_request(self):
        fun = api.make_api_request('BBAS3')
        self.assertIn('Meta Data', fun)
        self.assertIn('1. Information', fun['Meta Data'])
        self.assertIn('Daily Prices (open, high, low, close) and Volumes',
                      fun['Meta Data']['1. Information'])
        self.assertIn('Time Series (Daily)', fun)

    def test_dataframe_from_request_output(self):
        self.assertEqual(
            len(api.dataframe_from_request_output(
                api.make_api_request('bbas3'), 20)),
            20
        )
        self.assertEqual(
            api.dataframe_from_request_output(
                api.make_api_request('bbas3'), 20).size,
            100
        )
