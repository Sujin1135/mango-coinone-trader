import pytest
from app.services.accounts import (
    get_my_balance,
    get_orders,
    get_krw_transaction_history,
    get_coin_transaction_history,
    get_deposit_address,
    get_my_krw,
)


def test_get_my_balance():
    sut = get_my_balance()

    for k in sut:
        assert float(sut[k]["balance"]) > 0.0


def test_get_my_krw():
    sut = get_my_krw()

    assert "avail" in sut
    assert "balance" in sut


def test_get_orders():
    sut = get_orders("BTC")

    assert sut is not None


def test_get_my_krw_transaction_history():
    sut = get_krw_transaction_history()

    assert sut is not None


def test_get_my_coin_transaction_history_with_invalid_currency():
    sut = get_coin_transaction_history("BBTC")

    assert sut["result"] == "error"


@pytest.mark.parametrize("currency", ["BTC", "ETH", "XRP"])
def test_get_my_coin_transaction_history_with_correctly(currency: str):
    sut = get_coin_transaction_history(currency)

    assert sut is not None


def test_get_my_deposit_address():
    sut = get_deposit_address()

    assert sut is not None
