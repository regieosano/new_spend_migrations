from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import VARCHAR, Integer
from datetime import date

str_255 = Annotated[str, mapped_column(VARCHAR(255))]
str_44 = Annotated[str, mapped_column(VARCHAR(44))]

pk = Annotated[
    int,
    mapped_column(Integer, primary_key=True)
]


class Base(DeclarativeBase):
    pass


class Budget(Base):
    __tablename__ = "budget"
    id: Mapped[pk]
    description: Mapped[str_255]
    target_date: Mapped[date]
    target_amount: Mapped[int]
    payment_method_id: Mapped[str_44]
    season_id: Mapped[int]
    category_id: Mapped[int]
    created_at: Mapped[date]
    updated_at: Mapped[date]
