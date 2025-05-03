from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=True)
SessionLocal = sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()

def get_db():
    with SessionLocal() as session:
        yield session