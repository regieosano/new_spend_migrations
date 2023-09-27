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


class Category(Base):
    __tablename__ = "category"
    id: Mapped[pk]
    name: Mapped[str_255]
    org_id: Mapped[int]
    hidden: Mapped[bool]
    created_at: Mapped[date]
    updated_at: Mapped[date]
