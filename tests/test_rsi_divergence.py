from unittest import TestCase

from analysis.rsi_divergence import find_oversold, find_rsi_divergence, \
    highlight_rsi_divergences
from helpers import db


class TestRSIDIvergence(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.stock_df = db.read('bbas3', 120)

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
