from pydantic import BaseModel

class Currency(BaseModel):
    pass

class Transaction(BaseModel):
    id: int
    title: str
    value: int | float
    currency: str

class RepeatedT(Transaction):
    start: str
    period: str


class BasicT(Transaction):
    deadline: str