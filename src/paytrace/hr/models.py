from datetime import date

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from paytrace.db import Base


class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[str] = mapped_column(String(10), primary_key=True)  # "EMP-014"
    name: Mapped[str] = mapped_column(String(100))
    status: Mapped[str] = mapped_column(String(10))  # ACTIVE / INACTIVE
    joining_date: Mapped[date]
    monthly_gross_paise: Mapped[int]  # Rs 75,000 = 7500000 paise
    tax_regime: Mapped[str] = mapped_column(String(3))  # OLD / NEW
    ifsc: Mapped[str] = mapped_column(String(11))
    account_number: Mapped[str] = mapped_column(String(20))
    upi_id: Mapped[str | None] = mapped_column(String(50))