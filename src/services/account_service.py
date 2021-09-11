from src.providers.coinone_req import CoinoneReq

req = CoinoneReq()


def _get_available_balance_by_keys(keys: [], origin_balance: dict):
    result = {}

    for k in keys:
        result[k] = origin_balance[k]

    return result


def _filter_available(balance: dict):
    available_keys = list(
        filter(lambda k: 'avail' in balance[k] and float(balance[k]['avail']) > 0.0, balance.keys()),
    )

    return _get_available_balance_by_keys(available_keys, balance)


def get_my_balance():
    return _filter_available(req.post(action='v2/account/balance'))


def get_limit_sell(price: float, qty: float, currency: str):
    payload = {
        "price": price,
        "qty": qty,
        "currency": currency,
    }
    return req.post(action='v2/order/limit_sell', payload=payload)


def get_limit_order(currency: str):
    payload = {
        "currency": currency,
    }
    return req.post(action='v2/order/limit_orders', payload=payload)['limitOrders']


def get_krw_transaction_history():
    return req.post(action='v2/transaction/krw/history')['krwHistory']


def get_coin_transaction_history(currency: str):
    payload = {
        "currency": currency
    }
    return req.post(action='v2/transaction/history', payload=payload)['transactions']


def _filter_available_deposit(deposits: dict):
    return list(
            map(
                lambda k : {k: deposits[k]},
                filter(lambda k : deposits[k] is not None, deposits.keys())
            )
        )


def get_deposit_address():
    return _filter_available_deposit(req.post(action='v2/account/deposit_address')['walletAddress'])
