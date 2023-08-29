from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import VARCHAR, String
from datetime import date


str_255 = Annotated[str, mapped_column(VARCHAR(255))]

str_pk = Annotated[
    int,
    mapped_column(String, primary_key=True)
]


class Base(DeclarativeBase):
    pass


class Budget_Items(Base):
    __tablename__ = "budget_items"
    id: Mapped[str_pk]
    target_amount: Mapped[float]
    target_date_at: Mapped[date]
    vault_id: Mapped[str_255]
    is_default: Mapped[bool]
    created_at: Mapped[date]
    updated_at: Mapped[date]
    season_id: Mapped[str_255]
    category_id: Mapped[str_255]
    description: Mapped[str_255]
