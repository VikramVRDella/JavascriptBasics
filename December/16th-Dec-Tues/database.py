from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Database_url="mysql+pymysql://root:123456@localhost:3306/16th_dec"

engine=create_engine(Database_url)

SessionLocal =sessionmaker(autoflush=False,autocommit=False,bind=engine)
