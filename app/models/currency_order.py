from pydantic import BaseModel


class CurrencyOrder(BaseModel):
    currency: str
    price: float
    qty: float


class CancelCurrencyOrder(CurrencyOrder):
    order_id: str
