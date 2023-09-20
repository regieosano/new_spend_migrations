from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import String

str_pk = Annotated[
    str,
    mapped_column(String, primary_key=True)
]


class Base(DeclarativeBase):
    pass


class Budget_Transactions(Base):
    __tablename__ = "budget_transactions"
    id: Mapped[str_pk]
    transaction_id: Mapped[str]
    budget_item_id: Mapped[str]
    amount: Mapped[float]
