from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import VARCHAR, String


str_255 = Annotated[str, mapped_column(VARCHAR(255))]

str_pk = Annotated[
    str,
    mapped_column(String, primary_key=True)
]


class Base(DeclarativeBase):
    pass


class Transactions(Base):
    __tablename__ = "transactions"
    id: Mapped[str_pk]
    source: Mapped[str_255]
    external_id: Mapped[str_255]
    invoice_id: Mapped[str_255]
    is_reconciled: Mapped[bool]
