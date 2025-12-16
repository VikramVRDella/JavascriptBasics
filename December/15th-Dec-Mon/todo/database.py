from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from decouple import config

Db_url=config('db_url')
engine=create_engine(Db_url)
sessionLocal=sessionmaker(bind=engine)
Base=declarative_base()
