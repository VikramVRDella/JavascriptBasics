from sqlalchemy import Column, Integer,String
from database import Base

class StudentModel(Base):
    __tablename__ = 'students'
    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    roll=Column(Integer,nullable=False)
    name=Column(String(100),nullable=False)
    age = Column(Integer)