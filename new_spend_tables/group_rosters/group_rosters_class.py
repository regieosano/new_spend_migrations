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


class Group_Rosters(Base):
    __tablename__ = "group_rosters"
    id: Mapped[str_pk]
    roster_id: Mapped[str]
    user_id: Mapped[str]
    group_id: Mapped[str]
    invite_id: Mapped[str]
    season_id: Mapped[str]
    is_archived: Mapped[bool]
    archived_at: Mapped[date]
    joined_at: Mapped[date]
    is_member_initiated: Mapped[bool]
    created_at: Mapped[date]
