from src.providers.coinone_req import CoinoneReq
from config import ACCESS_TOKEN

req = CoinoneReq()


def _filter_available(balance: dict):
    return list(
        map(
            lambda k : balance[k],
            filter(lambda k : 'avail' in balance[k] and float(balance[k]['avail']) > 0.0, balance.keys()),
        )
    )


def get_my_balance():
    payload = {"access_token": ACCESS_TOKEN}
    return _filter_available(req.post(action='v2/account/balance', payload=payload))
