from app.providers.coinone_req import CoinoneReq
from app.enums.behavior import Behavior

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


def get_my_krw():
    return req.post(action='v2/account/balance')['krw']


def sell(price: float, qty: float, currency: str):
    payload = {
        "price": price,
        "qty": qty,
        "currency": currency,
    }
    return req.post(action='v2/order/limit_sell', payload=payload)


def buy(price: float, qty: float, currency: str):
    payload = {
        "price": price,
        "qty": qty,
        "currency": currency,
    }
    return req.post(action='v2/order/limit_buy', payload=payload)


def _cancel(behavior: Behavior, order_id: str, price: float, qty: float, currency: str):
    payload = {
        "order_id": order_id,
        "is_ask": behavior.value,
        "price": price,
        "qty": qty,
        "currency": currency,
    }
    return req.post(action='v2/order/cancel', payload=payload)


def cancel_buy(order_id: str, price: float, qty: float, currency: str):
    return _cancel(Behavior.BUY, order_id, price, qty, currency)


def cancel_sell(order_id: str, price: float, qty: float, currency: str):
    return _cancel(Behavior.SELL, order_id, price, qty, currency)


def get_orders(currency: str):
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


def get_market_price_cur(currency: str):
    return req.get(action='ticker?currency={}'.format(currency))
