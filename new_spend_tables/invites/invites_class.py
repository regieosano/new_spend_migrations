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


class Invites(Base):
    __tablename__ = "invites"
    id: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str]
    type: Mapped[str]
    is_user: Mapped[bool]
    status: Mapped[str]
    organization_id: Mapped[str]
    group_id: Mapped[str]
    user_id: Mapped[str]
    is_archived: Mapped[str]
    created_at: Mapped[date]
    expires_at: Mapped[date]
