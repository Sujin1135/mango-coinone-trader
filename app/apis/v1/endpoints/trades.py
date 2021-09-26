from fastapi import APIRouter, Response, status
from app.services.trades import sell, buy, cancel_buy, cancel_sell
from app.providers.res_helper import response_success, response_failure
from app.models.currency_order import CurrencyOrder, CancelCurrencyOrder

trade_router = APIRouter()


@trade_router.post("/sell", status_code=status.HTTP_201_CREATED)
def sell_currency(
    response: Response,
    order_info: CurrencyOrder,
):
    try:
        return response_success(
            sell(order_info.price, order_info.qty, order_info.currency)
        )
    except Exception as e:
        return response_failure(response, e)


@trade_router.post("/buy", status_code=status.HTTP_201_CREATED)
def buy_currency(response: Response, order_info: CurrencyOrder):
    try:
        return response_success(
            buy(order_info.price, order_info.qty, order_info.currency)
        )
    except Exception as e:
        return response_failure(response, e)


@trade_router.post("/cancel/buy")
def cancel_buy_order(response: Response, cancel_info: CancelCurrencyOrder):
    try:
        return response_success(
            cancel_buy(
                cancel_info.order_id,
                cancel_info.price,
                cancel_info.qty,
                cancel_info.currency,
            )
        )
    except Exception as e:
        return response_failure(response, e)


@trade_router.post("/cancel/sell")
def cancel_sell_order(
    response: Response,
    cancel_info: CancelCurrencyOrder,
):
    try:
        return response_success(
            cancel_sell(
                cancel_info.order_id,
                cancel_info.price,
                cancel_info.qty,
                cancel_info.currency,
            )
        )
    except Exception as e:
        return response_failure(response, e)
