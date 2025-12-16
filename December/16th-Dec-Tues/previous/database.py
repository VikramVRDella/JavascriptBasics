from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from decouple import config
from urllib.parse import quote_plus

DATABASE_URL = f"mysql+pymysql://{config('username')}:{config('password')}@{config('host')}:{config('port')}/{config('db')}"

engine=create_engine(DATABASE_URL)
SessionLocal=Session(autoflush=False,autocommit=False,bind=engine)

Base=declarative_base()
