from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import VARCHAR, Integer
from datetime import date

str_4096 = Annotated[str, mapped_column(VARCHAR(4096))]
str_255 = Annotated[str, mapped_column(VARCHAR(255))]
str_140 = Annotated[str, mapped_column(VARCHAR(140))]
str_60 = Annotated[str, mapped_column(VARCHAR(60))]
str_64 = Annotated[str, mapped_column(VARCHAR(64))]
str_44 = Annotated[str, mapped_column(VARCHAR(44))]
str_12 = Annotated[str, mapped_column(VARCHAR(12))]
str_4 = Annotated[str, mapped_column(VARCHAR(4))]
str_2 = Annotated[str, mapped_column(VARCHAR(2))]

pk = Annotated[
    int,
    mapped_column(Integer, primary_key=True)
]


class Base(DeclarativeBase):
    pass


class Organization(Base):
    __tablename__ = "organization"
    id: Mapped[pk]
    payment_method_id: Mapped[str_44]
    hash: Mapped[str_44]
    legal_name: Mapped[str_255]
    nickname: Mapped[str_255]
    type: Mapped[int]
    sport:  Mapped[int]
    email: Mapped[str_255]
    phone: Mapped[str_12]
    website: Mapped[str_255]
    logo_url: Mapped[str_255]
    address1: Mapped[str_255]
    address2: Mapped[str_255]
    city: Mapped[str_255]
    state: Mapped[str_2]
    zip: Mapped[str_12]
    statement_descriptor: Mapped[str_140]
    app_fee_pct: Mapped[int]
    app_fee_base: Mapped[int]
    cc_fee_pct: Mapped[int]
    cc_fee_base: Mapped[int]
    approved: Mapped[bool]
    verified: Mapped[bool]
    strict: Mapped[bool]
    notification: Mapped[str_4096]
    status: Mapped[str_64]
    reason: Mapped[str_255]
    paystand_id: Mapped[str_255]
    paystand_bank_id: Mapped[str_255]
    paystand_event_id: Mapped[str_44]
    created_at: Mapped[date]
    updated_at: Mapped[date]
    team_banks_enabled: Mapped[bool]
    agreement_enabled: Mapped[bool]
    sales_id: Mapped[int]
    app_bank_id: Mapped[str_44]
    external_id: Mapped[str_64]
    external_doc_id: Mapped[str_64]
    account_id: Mapped[str_60]
    synapse_verified: Mapped[bool]
    notify_upcoming_everyone: Mapped[bool]
    synapse_flagged: Mapped[bool]
    synapse_watchlists: Mapped[str_64]
    synapse_doc_status: Mapped[str_64]
    subscription_team_fee: Mapped[int]
    subscription_plan: Mapped[str_4]
    bank_2fa_completed: Mapped[bool]
    cip: Mapped[int]
    external_transfer_out_enabled: Mapped[bool]
