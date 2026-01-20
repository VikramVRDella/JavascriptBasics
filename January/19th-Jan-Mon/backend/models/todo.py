from sqlalchemy import Column, Integer, Boolean, String
from db.database import Base

class TodoModel(Base):
    __tablename__ = 'todo_table'
    id = Column(Integer,primary_key=True,autoincrement=True,index=True)
    title = Column(String(50),nullable=False)
    description = Column(String(100))
    completed = Column(Boolean,default=False)

