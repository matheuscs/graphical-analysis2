from unittest import TestCase
import finance_api


class TestFinanceAPI(TestCase):
    def test_make_api_request(self):
        fun = finance_api.make_api_request('BBAS3')
        self.assertIn('Meta Data', fun)
        self.assertIn('1. Information', fun['Meta Data'])
        self.assertIn('Daily Prices (open, high, low, close) and Volumes',
                      fun['Meta Data']['1. Information'])
        self.assertIn('Time Series (Daily)', fun)

    def test_get_stock_data(self):
        self.assertEqual(len(finance_api.get_stock_data('bbas3', 20)), 20)
        self.assertEqual(finance_api.get_stock_data('bbas3', 20).size, 100)
