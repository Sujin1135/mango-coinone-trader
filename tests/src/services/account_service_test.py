import unittest
from src.services.account_service import get_my_balance, get_limit_buy


class AccountServiceTestCase(unittest.TestCase):
    def test_get_my_balance(self):
        sut = get_my_balance()

        for d in sut:
            self.assertTrue(float(d['balance']) > 0)

    def test_get_limit_sell(self):
        sut = get_limit_buy(35000000, 0.002, 'BTC')

        self.assertTrue(len(sut['result']) > 0)
