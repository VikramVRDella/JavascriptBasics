from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

Database_url = 'mysql+pymysql://root:123456@localhost:3306/jan5th'

engine = create_engine(Database_url)

sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()