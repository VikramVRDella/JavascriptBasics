from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Database_url = "mysql+pymysql://root:123456@localhost:3306/jan6th"

engine = create_engine(Database_url)
SessionLocal =sessionmaker(bind=engine)

Base=declarative_base()

def get_db():
    db=SessionLocal()

    try:
        yield db
    finally:
        db.close()
