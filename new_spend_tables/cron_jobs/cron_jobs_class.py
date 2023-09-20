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


class Cron_Jobs(Base):
    __tablename__ = "cron_jobs"
    id: Mapped[str_pk]
    name: Mapped[str]
    status: Mapped[str]
    last_run_time: Mapped[date]
    is_active: Mapped[bool]
    created_at: Mapped[date]
    updated_at: Mapped[date]
