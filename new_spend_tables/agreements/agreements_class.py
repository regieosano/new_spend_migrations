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


class Agreements(Base):
    __tablename__ = "agreements"
    id: Mapped[str_pk]
    name: Mapped[str_255]
    created_at: Mapped[date]
    updated_at: Mapped[date]
    is_active: Mapped[bool]
    org_id: Mapped[str]
    content: Mapped[str]
