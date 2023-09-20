from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import VARCHAR, String

str_255 = Annotated[str, mapped_column(VARCHAR(255))]

str_pk = Annotated[
    str,
    mapped_column(String, primary_key=True)
]

# MISSING FIELDS (Present in legacy but not in new spend)
# address1
# address2
# payment_method_id
# hash
# nickname
# type
# sport
# statement_descriptor
# app_fee_pct
# cc_fee_base
# approved
# strict
# notification
# status
# reason
# paystand_id
# paystand_bank_id
# paystand_event_id
# created_at
# updated_at
# team_banks_enabled
# agreement_enabled
# sales_id
# app_bank_id
# external_doc_id
# synapse_verified
# notify_upcoming_everyone
# synapse_flagged
# synapse_watchlists
# synapse_doc_status
# subscription_team_fee
# subscription_plan
# bank_2fa_completed
# cip
# external_transfer_out_enabled


class Base(DeclarativeBase):
    pass


class Organizations(Base):
    __tablename__ = "organizations"
    id: Mapped[str_pk]
    legal_name: Mapped[str_255]
    email: Mapped[str_255]
    phone: Mapped[str_255]
    street: Mapped[str_255]
    city: Mapped[str_255]
    state: Mapped[str_255]
    zip: Mapped[str_255]
    website: Mapped[str_255]
    logo: Mapped[str_255]
    is_verified: Mapped[bool]
    user_id: Mapped[str_255]
    org_id: Mapped[str_255]
    external_id: Mapped[str_255]
    account_id: Mapped[str_255]
    spend_base_fee: Mapped[int]
    spend_percent: Mapped[float]
    card_base_fee: Mapped[int]
    card_percent: Mapped[float]
    ach_base_fee: Mapped[int]
    ach_percent: Mapped[float]
