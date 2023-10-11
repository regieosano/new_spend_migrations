from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import String
from datetime import date

str_pk = Annotated[
    str,
    mapped_column(String, primary_key=True)
]


class Base(DeclarativeBase):
    pass


class ReconciledTransactions(Base):
    __tablename__ = "reconciled_transactions"
    id: Mapped[str_pk]
    amount: Mapped[float]
    type: Mapped[str]
    payment_id: Mapped[str]
    created_at: Mapped[date]
    updated_at: Mapped[date]
    # budget_category_type: Mapped[str]

