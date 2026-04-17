from sqlalchemy import Column, Integer, Float, String
from database.db_connection import Base


class Health(Base):
    __tablename__ = "health"

    id = Column(Integer, primary_key=True, autoincrement=True)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    blood_type = Column(String, nullable=False)
    medical_condition = Column(String, nullable=False)
    insurance_provider = Column(String, nullable=False)
    billing_amount = Column(Float, nullable=False)
    admission_type = Column(String, nullable=False)
    medication = Column(String, nullable=False)
    test_result = Column(String, nullable=False)
