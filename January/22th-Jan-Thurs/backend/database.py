from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
from decouple import config

engine = create_engine(config("DATABASE_URL"))

SessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base = declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
