from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import VARCHAR, Integer
from datetime import date

str_64 = Annotated[str, mapped_column(VARCHAR(64))]

pk = Annotated[
    int,
    mapped_column(Integer, primary_key=True)
]


class Base(DeclarativeBase):
    pass


class Sales(Base):
    __tablename__ = "organization"
    id: Mapped[pk]
    name: Mapped[str_64]
    created_at: Mapped[date]
    updated_at: Mapped[date]
