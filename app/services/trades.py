from app.enums.behavior import Behavior
from app.providers.coinone_req import CoinoneReq

req = CoinoneReq()


def sell(price: float, qty: float, currency: str):
    payload = {
        "price": price,
        "qty": qty,
        "currency": currency,
    }
    return req.post(action="v2/order/limit_sell", payload=payload)


def buy(price: float, qty: float, currency: str):
    payload = {
        "price": price,
        "qty": qty,
        "currency": currency,
    }
    return req.post(action="v2/order/limit_buy", payload=payload)


def _cancel(behavior: Behavior, order_id: str, price: float, qty: float, currency: str):
    payload = {
        "order_id": order_id,
        "is_ask": behavior.value,
        "price": price,
        "qty": qty,
        "currency": currency,
    }
    return req.post(action="v2/order/cancel", payload=payload)


def cancel_buy(order_id: str, price: float, qty: float, currency: str):
    return _cancel(Behavior.BUY, order_id, price, qty, currency)


def cancel_sell(order_id: str, price: float, qty: float, currency: str):
    return _cancel(Behavior.SELL, order_id, price, qty, currency)
