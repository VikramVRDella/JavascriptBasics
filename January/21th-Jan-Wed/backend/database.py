from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from decouple import config

engine = create_engine(config('DATABASE_URL'))

SessionLocal  = sessionmaker(autoflush=False,autocommit=False,bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()