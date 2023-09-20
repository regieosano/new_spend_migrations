from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import VARCHAR, Integer
from datetime import date

str_255 = Annotated[str, mapped_column(VARCHAR(255))]
str_44 = Annotated[str, mapped_column(VARCHAR(44))]
str_40 = Annotated[str, mapped_column(VARCHAR(40))]
str_20 = Annotated[str, mapped_column(VARCHAR(20))]

pk = Annotated[
    int,
    mapped_column(Integer, primary_key=True)
]


class Base(DeclarativeBase):
    pass


class Invite(Base):
    __tablename__ = "invite"
    id: Mapped[pk]
    email: Mapped[str_255]
    token: Mapped[str_44]
    message_id: Mapped[str_255]
    type: Mapped[str_20]
    status: Mapped[str_40]
    created_at: Mapped[date]
    updated_at: Mapped[date]
