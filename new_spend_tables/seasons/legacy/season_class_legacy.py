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


class Season(Base):
    __tablename__ = "season"
    created_at: Mapped[date]
    updated_at: Mapped[date]
    id: Mapped[pk]
    team_id: Mapped[str_255]
    name: Mapped[str_255]
    start_date: Mapped[date]
    end_date: Mapped[date]
    link_allowed: Mapped[bool]
    payment_schedule_state: Mapped[str_255]
    budget_shared: Mapped[bool]
    discount_amount: Mapped[int]
    discount_cutoff_amount: Mapped[int]
    discount_cutoff_date: Mapped[date]
    discount_enabled: Mapped[bool]
