from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///./claims.db", echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class Claim(Base):
    __tablename__ = "claims"
    id = Column(String, primary_key=True, index=True)
    hospital = Column(String)
    patient_id = Column(String)
    diagnosis = Column(String)
    claimed = Column(Float)
    score = Column(Float)
    type = Column(String)
    risk = Column(String)

def init_db():
    Base.metadata.create_all(bind=engine)
