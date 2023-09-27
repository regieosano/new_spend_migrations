from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import VARCHAR, String
from datetime import date


str_255 = Annotated[str, mapped_column(VARCHAR(255))]

str_pk = Annotated[
    str,
    mapped_column(String, primary_key=True)
]


class Base(DeclarativeBase):
    pass


class Seasons(Base):
    __tablename__ = "seasons"
    id: Mapped[str_pk]
    start_date_at: Mapped[date]
    end_date_at: Mapped[date]
    name: Mapped[str_255]
    is_link_enabled: Mapped[bool]
    is_budget_shared: Mapped[bool]
    created_at: Mapped[date]
    updated_at: Mapped[date]
    group_id: Mapped[str_255]
