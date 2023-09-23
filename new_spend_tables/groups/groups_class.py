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


class Groups(Base):
    __tablename__ = "groups"
    id: Mapped[str_pk]
    name: Mapped[str]
    vault_id: Mapped[str]
    prog_id: Mapped[str]
    is_archived: Mapped[bool]
    created_at: Mapped[date]
    archived_at: Mapped[date]
    organization_id: Mapped[str]
    account_id: Mapped[str]
