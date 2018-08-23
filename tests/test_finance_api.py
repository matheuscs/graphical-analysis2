from unittest import TestCase
from helpers import finance_api as api


class TestFinanceAPI(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.stock_values = api.request_stock_values('BBAS3')
        cls.rsi = api.request_rsi('BBAS3')

    def test_request_stock_values(self):
        self.assertIn('Meta Data', self.stock_values)
        self.assertIn('1. Information', self.stock_values['Meta Data'])
        self.assertIn('Daily Prices (open, high, low, close) and Volumes',
                      self.stock_values['Meta Data']['1. Information'])
        self.assertIn('Time Series (Daily)', self.stock_values)

    def test_stock_values_as_dataframe(self):
        self.assertEqual(
            len(api.stock_values_as_dataframe(self.stock_values, 20)), 20)
        self.assertEqual(
            api.stock_values_as_dataframe(self.stock_values, 20).size, 100)

    def test_request_rsi(self):
        rsi_meta_data = self.rsi['Meta Data']
        self.assertIn('1: Symbol', rsi_meta_data)
        self.assertIn('Relative Strength Index (RSI)',
                      rsi_meta_data['2: Indicator'])
        self.assertIn('3: Last Refreshed', rsi_meta_data)
        self.assertIn('4: Interval', rsi_meta_data)
        self.assertIn('5: Time Period', rsi_meta_data)
        self.assertIn('6: Series Type', rsi_meta_data)
        self.assertIn('7: Time Zone', rsi_meta_data)

    def test_rsi_as_dataframe(self):
        self.assertEqual(
            len(api.rsi_as_dataframe(self.rsi, 20)), 20)
        self.assertEqual(
            api.rsi_as_dataframe(self.rsi, 20).size, 20)
