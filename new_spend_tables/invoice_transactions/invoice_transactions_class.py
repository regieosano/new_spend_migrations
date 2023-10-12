from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import Integer
from datetime import date

pk = Annotated[
    int,
    mapped_column(Integer, primary_key=True)
]


class Base(DeclarativeBase):
    pass


class InvoiceTransactions(Base):
    __tablename__ = "invoice_transactions"
    id: Mapped[pk]
    invoice_id: Mapped[int]
    amount: Mapped[int]
    transaction_id: Mapped[int]
