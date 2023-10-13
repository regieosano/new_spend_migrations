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


class Invoices(Base):
    __tablename__ = "invoices"
    id: Mapped[str_pk]
    paid: Mapped[bool]
    amount: Mapped[float]
    note: Mapped[str_255]
    paid_date: Mapped[date]
    last_notification_date: Mapped[date]
    notification_attempts: Mapped[int]
    last_notification_id: Mapped[str_255]
    description: Mapped[str_255]
    balance_due: Mapped[float]
    is_optional: Mapped[bool]
    opted_in: Mapped[bool]
    created_at: Mapped[date]
    updated_at: Mapped[date]
    due_date: Mapped[date]
    payment_schedule_invoice_id: Mapped[str_255]
    group_roster_id: Mapped[str_255]
    budget_item_id: Mapped[str_255]
    payment_method_source: Mapped[str_255]
    payment_method_id: Mapped[str_255]
    is_refunded: Mapped[bool]
    refund_date: Mapped[date]
    is_auto_pay_authorized: Mapped[bool]
    is_archived: Mapped[bool]
    discount_amount: Mapped[float]
    penalty_amount: Mapped[float]
