from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import VARCHAR, Integer
from datetime import date

str_255 = Annotated[str, mapped_column(VARCHAR(255))]
str_64 = Annotated[str, mapped_column(VARCHAR(64))]
str_60 = Annotated[str, mapped_column(VARCHAR(60))]
str_44 = Annotated[str, mapped_column(VARCHAR(44))]
str_20 = Annotated[str, mapped_column(VARCHAR(20))]
str_10 = Annotated[str, mapped_column(VARCHAR(10))]

pk = Annotated[
    int,
    mapped_column(Integer, primary_key=True)
]


class Base(DeclarativeBase):
    pass


class Transaction(Base):
    __tablename__ = "transaction"
    id: Mapped[pk]
    source_id: Mapped[str_44]
    type: Mapped[str_64]
    method: Mapped[str_64]
    check_no: Mapped[str_10]
    amount: Mapped[int]
    fee: Mapped[int]
    revenue: Mapped[int]
    cost: Mapped[int]
    status: Mapped[str_64]
    reason: Mapped[str_255]
    settled_at: Mapped[date]
    external_id: Mapped[str_60]
    paystand_event_id: Mapped[str_44]
    created_at: Mapped[date]
    updated_at: Mapped[date]
    entry: Mapped[str_64]
    org_id: Mapped[int]
    note: Mapped[str_255]
    discount: Mapped[int]
    destination_id: Mapped[str_44]
    external: Mapped[str_20]
    source_balance: Mapped[int]
    idempotency_key: Mapped[str_10]
    debit_card_id: Mapped[str_44]
    merchant: Mapped[str_255]
    returned: Mapped[bool]
    destination_balance: Mapped[int]
    return_fee: Mapped[int]
    disputed: Mapped[bool]
    initiator_id: Mapped[str_44]
    notified_on: Mapped[str_64]
    memo: Mapped[str_255]
    destination_note: Mapped[str_255]
