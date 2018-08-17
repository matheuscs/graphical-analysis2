from unittest import TestCase
from helpers import finance_api as api


class TestFinanceAPI(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_request = api.make_api_request('BBAS3')

    def test_make_api_request(self):
        self.assertIn('Meta Data', self.api_request)
        self.assertIn('1. Information', self.api_request['Meta Data'])
        self.assertIn('Daily Prices (open, high, low, close) and Volumes',
                      self.api_request['Meta Data']['1. Information'])
        self.assertIn('Time Series (Daily)', self.api_request)

    def test_dataframe_from_request_output(self):
        self.assertEqual(
            len(api.dataframe_from_request_output(self.api_request, 20)), 20)
        self.assertEqual(
            api.dataframe_from_request_output(self.api_request, 20).size, 100)
