from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import String
from datetime import date

str_pk = Annotated[
    str,
    mapped_column(String, primary_key=True)
]

class Base(DeclarativeBase):
    pass

class PaymentScheduleInvoices(Base):
    __tablename__ = "payment_schedule_invoices"
    id: Mapped[str_pk]
    description: Mapped[str]
    note: Mapped[str]
    amount_due: Mapped[float]
    due_date: Mapped[date]
    is_optional: Mapped[bool]
    status: Mapped[str]
    group_id: Mapped[str]
    season_id: Mapped[int]
    budget_item_id: Mapped[int]
    is_archived: Mapped[bool]
    last_published_state: Mapped[str]

