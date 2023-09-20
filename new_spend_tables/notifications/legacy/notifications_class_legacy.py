from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import VARCHAR, Integer
from datetime import date

pk = Annotated[
    int,
    mapped_column(Integer, primary_key=True)
]


class Base(DeclarativeBase):
    pass


# id
# past_due
# failed_payment
# created_at
# updated_at
# org_level
# club_user_level
# team_user_level
# snap_home_notify
