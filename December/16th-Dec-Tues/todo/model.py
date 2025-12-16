from sqlalchemy import Column,Integer,String,Boolean
from database import Base

class TodoModel(Base):
    __tablename__ = "todos"

    id=Column(Integer,primary_key=True,autoincrement=True)
    title=Column(String(50))
    description=Column(String(50))
    completed=Column(Boolean,default=False)