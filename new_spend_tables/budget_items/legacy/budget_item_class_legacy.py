from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import VARCHAR, Integer
from datetime import date

str_255 = Annotated[str, mapped_column(VARCHAR(255))]

pk = Annotated[
    int,
    mapped_column(Integer, primary_key=True)
]


class Base(DeclarativeBase):
    pass


class BudgetItem(Base):
    __tablename__ = "budget"
    id: Mapped[pk]
    description: Mapped[str_255]
    target_amount: Mapped[int]
    season_id:Mapped[int]
    category_id: Mapped[int]
    created_at: Mapped[date]
    updated_at: Mapped[date]

