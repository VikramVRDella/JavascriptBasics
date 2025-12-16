from sqlalchemy import Column, Integer,String,Boolean
from database import Base

class TodoModel(Base):
    __tablename__ = 'todo_model'
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(50),nullable=False)
    description=Column(String)
    completed=Column(Boolean,default=False)
   