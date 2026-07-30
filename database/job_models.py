from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, DateTime, Numeric, Text
from sqlalchemy.sql import func

class Base(DeclarativeBase):
    pass

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