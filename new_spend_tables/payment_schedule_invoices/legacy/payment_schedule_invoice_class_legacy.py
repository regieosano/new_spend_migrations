from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import VARCHAR, Integer
from datetime import date

str_255 = Annotated[str, mapped_column(VARCHAR(255))]
str_44 = Annotated[str, mapped_column(VARCHAR(44))]
str_64 = Annotated[str, mapped_column(VARCHAR(64))]
str_10 = Annotated[str, mapped_column(VARCHAR(10))]

pk = Annotated[
    int,
    mapped_column(Integer, primary_key=True)
]

class Base(DeclarativeBase):
    pass

class PaymentScheduleInvoice(Base):
    __tablename__ = "payment_schedule_invoice"
    schedule_invoice_id: Mapped[pk]
    description: Mapped[str_255]
    due_date: Mapped[date]
    optional: Mapped[bool]
    state: Mapped[str_10]
    note: Mapped[str_255]
    amount_due: Mapped[int]
    team_id: Mapped[str_44]
    season_id: Mapped[int]
    budget_item_id: Mapped[int]


