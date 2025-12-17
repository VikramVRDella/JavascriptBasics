from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from decouple import config

Database_url= config('database_url')

engine = create_engine(Database_url)

SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
