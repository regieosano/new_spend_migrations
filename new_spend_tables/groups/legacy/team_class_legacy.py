from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import VARCHAR, String
from datetime import date

str_255 = Annotated[str, mapped_column(VARCHAR(255))]
str_64 = Annotated[str, mapped_column(VARCHAR(64))]
str_60 = Annotated[str, mapped_column(VARCHAR(60))]
str_36 = Annotated[str, mapped_column(VARCHAR(36))]

str_pk = Annotated[
    str,
    mapped_column(String, primary_key=True)
]


class Base(DeclarativeBase):
    pass


class Team(Base):
    __tablename__ = "team"
    team_id: Mapped[str_pk]
    team_name: Mapped[str_255]
    sport: Mapped[str_255]
    archived: Mapped[bool]
    app_fee_base: Mapped[int]
    app_fee_pct: Mapped[int]
    org_id: Mapped[int]
    payment_method_id: Mapped[str_36]
    bank_enabled: Mapped[bool]
    agreement_enabled: Mapped[bool]
    agreement_id: Mapped[int]
    active_date: Mapped[date]
    created_at: Mapped[date]
    inactive_date: Mapped[date]
    updated_at: Mapped[date]
    account_id: Mapped[str_60]
    external_doc_id: Mapped[str_64]
    external_id: Mapped[str_64]
    synapse_verified: Mapped[bool]
    synapse_flagged: Mapped[bool]
    synapse_watchlists: Mapped[str_64]
    synapse_doc_status: Mapped[str_64]
