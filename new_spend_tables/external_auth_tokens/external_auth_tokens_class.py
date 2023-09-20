from datetime import date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import String

str_pk = Annotated[
    str,
    mapped_column(String, primary_key=True)
]


class Base(DeclarativeBase):
    pass


class External_Auth_Tokens(Base):
    __tablename__ = "external_auth_tokens"
    id: Mapped[str_pk]
    value: Mapped[str]
    source: Mapped[str]
    type: Mapped[str]
    reference_id: Mapped[str]
    user_id: Mapped[str]
    created_at: Mapped[date]
