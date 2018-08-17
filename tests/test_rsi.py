from unittest import TestCase
import pandas as pd

from modules.rsi import find_rsi


class TestRSI(TestCase):
    def test_find_rsi_exceptions(self):
        with self.assertRaises(TypeError):
            find_rsi(1)
        with self.assertRaises(ValueError):
            find_rsi(pd.DataFrame())
        with self.assertRaises(ValueError):
            find_rsi(pd.DataFrame([i for i in range(3)]), 2)
        with self.assertRaises(ValueError):
            find_rsi(pd.DataFrame([i for i in range(3)]), 4)

