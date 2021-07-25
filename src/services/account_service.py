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


def get_limit_sell(price: float, qty: float, currency: str):
    payload = {
        "access_token": ACCESS_TOKEN,
        "price": price,
        "qty": qty,
        "currency": currency,
    }
    return req.post(action='v2/order/limit_sell', payload=payload)


def get_limit_order(currency: str):
    payload = {
        "access_token": ACCESS_TOKEN,
        "currency": currency,
    }
    return req.post(action='v2/order/limit_orders', payload=payload)


def get_krw_transaction_history():
    payload = {
        "access_token": ACCESS_TOKEN
    }
    return req.post(action='v2/transaction/krw/history', payload=payload)


def get_coin_transaction_history(currency: str):
    payload = {
        "access_token": ACCESS_TOKEN,
        "currency": currency
    }
    return req.post(action='v2/transaction/history', payload=payload)
