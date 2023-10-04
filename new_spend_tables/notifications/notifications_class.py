from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import String
from datetime import date

str_pk = Annotated[
    int,
    mapped_column(String, primary_key=True)
]


class Base(DeclarativeBase):
    pass


class Notifications(Base):
    __tablename__ = "notifications"
    id: Mapped[str_pk]
    past_due: Mapped[bool]
    failed_payment: Mapped[bool]
    created_at: Mapped[date]
    updated_at: Mapped[date]
   
