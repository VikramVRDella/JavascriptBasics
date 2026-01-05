from sqlalchemy import Column, Integer, String
from database import Base

class StudentModel(Base):
    __tablename__ = 'fastapi_students'
    id = Column(Integer, primary_key = True , autoincrement=True)
    roll_no = Column(Integer)
    name=Column(String(50))
    age = Column(Integer)