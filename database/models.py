from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Numeric, DateTime
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    pass


class Sales(Base):
    __tablename__ = "sales"

    orderid = Column(Integer, primary_key=True)

    product = Column(String(100), nullable=False)

    quantity = Column(Integer, nullable=False)

    price = Column(Numeric(10, 2), nullable=False)

    totalamount = Column(Numeric(10, 2), nullable=False)

    loaddate = Column(DateTime(timezone=True), server_default=func.now())