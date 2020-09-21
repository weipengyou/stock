from unittest import TestCase

from src.IO.get_data_from_yahoo import get_last_stock_price


class TestGet_last_stock_price(TestCase):
    def test_get_last_stock_price(self):
        d = get_last_stock_price('AZPN', True)
        self.assertTrue(len(d) > 10)
