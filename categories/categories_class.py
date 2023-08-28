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


class Categories(Base):
    __tablename__ = "categories"
    id: Mapped[str_pk]
    name: Mapped[str_255]
    type: Mapped[str_255]
    is_default: Mapped[bool]
    is_hidden: Mapped[bool]
    created_at: Mapped[date]
    updated_at: Mapped[date]
    organization_id: Mapped[str]
