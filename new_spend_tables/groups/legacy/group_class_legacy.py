from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import VARCHAR, String
from datetime import date

str_255 = Annotated[str, mapped_column(VARCHAR(255))]


class Base(DeclarativeBase):
    pass
