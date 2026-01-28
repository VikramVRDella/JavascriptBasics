from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker
from decouple import config


engine = create_engine(config("DATABASE_URL"))

Localsession = sessionmaker(autoflush=False,autocommit=False,bind=engine)

def get_db():
    db=Localsession()
    try:
        yield db
    finally:
        db.close()

class Base(DeclarativeBase):
    pass
