from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import VARCHAR
from sqlalchemy import Integer
from datetime import date

str_44 = Annotated[str, mapped_column(VARCHAR(44))]

pk = Annotated[
    int,
    mapped_column(Integer, primary_key=True)
]


class Base(DeclarativeBase):
    pass


class Team_Player(Base):
    __tablename__ = "team_player"
    id: Mapped[pk]
    team_id: Mapped[str_44]
    player_id: Mapped[str_44]
    payer_id: Mapped[int]
    join_date: Mapped[date]
    add_date:  Mapped[date]
    archived: Mapped[bool]
    invite_id: Mapped[int]
    payer_initiated: Mapped[bool]
    agreement_id: Mapped[int]
    season_id: Mapped[int]
