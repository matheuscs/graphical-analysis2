import unittest
from finance_api import *


class TestFinanceAPI(unittest.TestCase):
    def test_make_api_request(self):
        self.assertRegex(
            make_api_request(),
            r'formation": "Daily Time Series with Splits and Dividend Events",')
