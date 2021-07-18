import unittest
from src.services.account_service import get_my_balance


class AccountServiceTestCase(unittest.TestCase):
    def test_get_my_balance(self):
        sut = get_my_balance()

        for d in sut:
            self.assertTrue(float(d['balance']) > 0)
