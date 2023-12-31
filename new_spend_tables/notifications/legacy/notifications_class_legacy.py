from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import Integer
from datetime import date

pk = Annotated[
    int,
    mapped_column(Integer, primary_key=True)
]


class Base(DeclarativeBase):
    pass


class Notifications(Base):
    __tablename__ = "notifications"
    id: Mapped[pk]
    past_due: Mapped[bool]
    failed_payment: Mapped[bool]
    created_at: Mapped[date]
    updated_at: Mapped[date]
    org_level: Mapped[bool]
    club_user_level: Mapped[bool]
    team_user_level: Mapped[bool]
    snap_home_notify: Mapped[bool]

