from unittest import TestCase

from modules.candlesticks import get_body_size, get_upper_shadow_size, \
    get_lower_shadow_size


class TestCandlesticks(TestCase):
    def test_get_body_size(self):
        row = {'Open': 10.21, 'Close': 10.51}
        self.assertAlmostEqual(get_body_size(row), 0.3)
        self.assertNotAlmostEqual(get_body_size(row), 0.29)
        self.assertNotAlmostEqual(get_body_size(row), 0.31)

    def test_get_upper_shadow_size(self):
        row = {'Open': 10.21, 'High': 10.57, 'Low': 10.10, 'Close': 10.51}
        self.assertAlmostEqual(get_upper_shadow_size(row), 0.06)
        self.assertNotAlmostEqual(get_upper_shadow_size(row), 0.05)
        self.assertNotAlmostEqual(get_upper_shadow_size(row), 0.04)
        row = {'Open': 11.87, 'High': 11.88, 'Low': 11.10, 'Close': 11.61}
        self.assertAlmostEqual(get_upper_shadow_size(row), 0.01)
        self.assertNotAlmostEqual(get_upper_shadow_size(row), 0.00)
        self.assertNotAlmostEqual(get_upper_shadow_size(row), 0.02)

    def test_get_lower_shadow_size(self):
        row = {'Open': 10.21, 'High': 10.57, 'Low': 10.10, 'Close': 10.51}
        self.assertAlmostEqual(get_lower_shadow_size(row), 0.11)
        self.assertNotAlmostEqual(get_lower_shadow_size(row), 0.10)
        self.assertNotAlmostEqual(get_lower_shadow_size(row), 0.12)
        row = {'Open': 11.87, 'High': 11.88, 'Low': 11.10, 'Close': 11.61}
        self.assertAlmostEqual(get_lower_shadow_size(row), 0.51)
        self.assertNotAlmostEqual(get_lower_shadow_size(row), 0.50)
        self.assertNotAlmostEqual(get_lower_shadow_size(row), 0.52)
