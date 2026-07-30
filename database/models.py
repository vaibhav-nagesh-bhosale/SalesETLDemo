from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Numeric, DateTime, Text,BigInteger
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


class ETLJobHistory(Base):

    __tablename__ = "etl_job_history"

    job_id = Column(Integer, primary_key=True)

    file_name = Column(String(255))

    source = Column(String(50))

    records_loaded = Column(Integer)

    status = Column(String(20))

    duration_seconds = Column(Numeric(10,2))

    error_message = Column(Text)

    start_time = Column(DateTime(timezone=True))

    end_time = Column(DateTime(timezone=True),
                      server_default=func.now())


class UploadedFile(Base):

    __tablename__ = "uploaded_files"

    file_id = Column(Integer, primary_key=True)

    file_name = Column(String(255))

    blob_path = Column(String(500))

    file_size = Column(BigInteger)

    uploaded_at = Column(DateTime(timezone=True),
                         server_default=func.now())

    uploaded_by = Column(String(100))

    processing_status = Column(String(20))