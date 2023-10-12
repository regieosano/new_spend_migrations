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


class Income_Budget_Transaction(Base):
    __tablename__ = "income_budget_transaction"
    budget_id: Mapped[pk]
    transaction_id: Mapped[int]
    invoice_id: Mapped[int]
    amount: Mapped[int]
    created_at: Mapped[date]
    updated_at: Mapped[date]
