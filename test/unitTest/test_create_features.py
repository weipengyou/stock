from unittest import TestCase

from src.IO.get_data_from_yahoo import get_last_stock_price
from src.algo.dummy_model import create_features


class TestCreate_features(TestCase):
    def test_create_features(self):
        df = get_last_stock_price('AZPN', True)
        df_features = create_features(df)
        self.assertTrue(len(df_features > 0))
