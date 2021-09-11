import pytest
from src.services.account_service import get_my_balance, sell, get_orders, \
    get_krw_transaction_history, get_coin_transaction_history, get_deposit_address


def test_get_my_balance():
    sut = get_my_balance()

    for d in sut:
        assert float(d['balance']) > 0


def test_sell():
    sut = sell(35000000, 0.001, 'BTC')

    assert len(sut['result']) > 0


def test_get_orders():
    sut = get_orders('BTC')

    assert sut is not None


def test_get_my_krw_transaction_history():
    sut = get_krw_transaction_history()

    assert sut is not None


def test_get_my_coin_transaction_history_with_invalid_currency():
    sut = get_coin_transaction_history('BBTC')

    assert sut['result'] == 'error'


@pytest.mark.parametrize("currency", ['BTC', 'ETH', 'XRP'])
def test_get_my_coin_transaction_history_with_correctly(currency: str):
    sut = get_coin_transaction_history(currency)

    assert sut is not None


def test_get_my_deposit_address():
    sut = get_deposit_address()

    assert sut is not None
