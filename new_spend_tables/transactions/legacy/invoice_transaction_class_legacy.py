from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import Integer

pk = Annotated[
    int,
    mapped_column(Integer, primary_key=True)
]


class Base(DeclarativeBase):
    pass


class Invoice_Transaction(Base):
    __tablename__ = "invoice_transaction"
    id: Mapped[pk]
    invoice_id: Mapped[int]
    amount: Mapped[int]
    transaction_id: Mapped[int]
    fee: Mapped[int]
    revenue: Mapped[int]
    discount: Mapped[int]
