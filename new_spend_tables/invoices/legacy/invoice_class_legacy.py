from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import VARCHAR, Integer
from datetime import date

str_255 = Annotated[str, mapped_column(VARCHAR(255))]
str_44 = Annotated[str, mapped_column(VARCHAR(44))]
str_64 = Annotated[str, mapped_column(VARCHAR(64))]

pk = Annotated[
    int,
    mapped_column(Integer, primary_key=True)
]


class Base(DeclarativeBase):
    pass


class Invoice(Base):
    __tablename__ = "invoice"
    invoice_id: Mapped[pk]
    team_player_id: Mapped[int]
    description: Mapped[str_255]
    due_date: Mapped[date]
    optional: Mapped[bool]
    opted_in: Mapped[bool]
    stopped: Mapped[bool]
    last_parent_notification_date: Mapped[date]
    last_parent_notification_age: Mapped[int]
    note: Mapped[str_255]
    payment_schedule_invoice_id: Mapped[int]
    payment_method_id: Mapped[str_44]
    amount_due: Mapped[int]
    reason: Mapped[str_255]
    status: Mapped[str_64]
    cc_fee_base: Mapped[int]
    cc_fee_pct: Mapped[int]
    app_fee_base: Mapped[int]
    app_fee_pct: Mapped[int]
    created_at: Mapped[date]
    updated_at: Mapped[date]
    penalty: Mapped[int]
    paid: Mapped[int]
    pending: Mapped[int]
    credit: Mapped[int]
    memo: Mapped[str_255]
    budget_item_id: Mapped[int]
