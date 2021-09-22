import unittest
from config import ACCESS_TOKEN
from app.providers.coinone_req import CoinoneReq


class CoinoneReqTestCase(unittest.TestCase):
    def setUp(self):
        self.req = CoinoneReq()

    def test_get_balance(self):
        payload = {"access_token": ACCESS_TOKEN}
        req = CoinoneReq()

        sut = req.post(action="v2/account/balance", payload=payload)

        self.assertEqual(sut["result"], "success")
