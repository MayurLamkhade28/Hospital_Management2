from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = 'postgresql://postgres:1234@localhost:5432/hospital_database'
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


class SqlAlchemy:
    def __init__(self):
        self.SessionLocal = SessionLocal
