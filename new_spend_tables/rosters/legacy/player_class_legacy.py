from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import VARCHAR, String
from datetime import date

str_255 = Annotated[str, mapped_column(VARCHAR(255))]

pk = Annotated[
    str,
    mapped_column(String, primary_key=True)
]


class Base(DeclarativeBase):
    pass


class Player(Base):
    __tablename__ = "player"
    player_id: Mapped[pk]
    player_name: Mapped[str_255]
    dob: Mapped[date]
    archived: Mapped[bool]
