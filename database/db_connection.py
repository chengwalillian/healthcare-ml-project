from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv("DB_URL")

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


def get_engine():
    return engine


def get_session():
    return SessionLocal()

try:
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
        print("Database connected")
        conn.close()
except SQLAlchemyError as SQE:
    print("Database connection failed", SQE)
