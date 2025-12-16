from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.ext.declarative import declarative_base

db_url="mysql+pymysql://root:123456@localhost:3306/16th_dec"

engine=create_engine(db_url)

SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base=declarative_base()