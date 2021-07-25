import pytest
from src.services.account_service import get_my_balance, get_limit_sell, get_limit_order, \
    get_krw_transaction_history, get_coin_transaction_history


def test_get_my_balance():
    sut = get_my_balance()

    for d in sut:
        assert float(d['balance']) > 0


def test_get_limit_sell():
    sut = get_limit_sell(35000000, 0.001, 'BTC')

    assert len(sut['result']) > 0


def test_get_limit_order():
    sut = get_limit_order('BTC')

    assert sut['result'] == 'success'


def test_get_my_krw_transaction_history():
    sut = get_krw_transaction_history()

    assert sut['result'] == 'success'


def test_get_my_coin_transaction_history_with_invalid_currency():
    sut = get_coin_transaction_history('BBTC')

    assert sut['result'] == 'error'


@pytest.mark.parametrize("currency", ['BTC', 'ETH'])
def test_get_my_coin_transaction_history_with_correctly(currency: str):
    sut = get_coin_transaction_history(currency)

    assert sut['result'] == 'success'
