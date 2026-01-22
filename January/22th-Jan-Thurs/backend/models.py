from sqlalchemy import Column,Integer,String
from database import Base

class UserModel(Base):
    __tablename__ = "user"
    id=Column(Integer,primary_key=True,autoincrement=True,index=True)
    username = Column(String(50),nullable=False,index=True)
    hashed_password = Column(String(255),nullable=False)
