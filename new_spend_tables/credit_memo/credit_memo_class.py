from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy import VARCHAR, String
from datetime import date

str_255 = Annotated[str, mapped_column(VARCHAR(255))]

str_pk = Annotated[
    str,
    mapped_column(String, primary_key=True)
]



class Base(DeclarativeBase):
    pass


class CreditMemo(Base):
    __tablename__ = "credit_memo"
    id: Mapped[str_pk]
    correlationId: Mapped[str]
    note: Mapped[str]
    dateToApply: Mapped[date]
    creditApplied: Mapped[float]
    creditAmount: Mapped[float]
    createdAt: Mapped[date]
    createdByUserId: Mapped[str]
    isArchived: Mapped[bool]
    archivedAt: Mapped[date]
    invoiceId: Mapped[str]   
