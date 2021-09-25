from fastapi import APIRouter, Response
from app.providers.res_helper import response_success, response_failure
from app.services.accounts import (
    get_my_balance,
    get_my_krw,
    get_orders,
    get_coin_transaction_history,
    get_krw_transaction_history,
    get_deposit_address,
)

account_router = APIRouter()


@account_router.get("/balance", status_code=200)
def get_balance(response: Response):
    try:
        return response_success(get_my_balance())
    except Exception as e:
        return response_failure(response, e)


@account_router.get("/krw")
def get_krw(response: Response):
    try:
        return response_success(get_my_krw())
    except Exception as e:
        return response_failure(response, e)


@account_router.get("/order-history/{currency}")
def get_order_history(currency: str, response: Response):
    try:
        return response_success(get_orders(currency))
    except Exception as e:
        return response_failure(response, e)


@account_router.get("/coin-transaction-history/{currency}")
def get_coin_history(currency: str, response: Response):
    try:
        return response_success(get_coin_transaction_history(currency))
    except Exception as e:
        return response_failure(response, e)


@account_router.get("/krw-transaction-history")
def get_krw_history(response: Response):
    try:
        return response_success(get_krw_transaction_history())
    except Exception as e:
        return response_failure(response, e)


@account_router.get("/deposit")
def get_deposit(response: Response):
    try:
        return response_success(get_deposit_address())
    except Exception as e:
        return response_failure(response, e)
