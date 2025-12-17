from sqlalchemy import Column,Integer,String
from database import Base

class StudentModel(Base):
    __tablename__ = 'studentModel'

    id=Column(Integer,autoincrement=True,primary_key=True,index=True)
    roll_no=Column(Integer,nullable=False)
    name=Column(String(50),nullable=False)
    age=Column(Integer)
