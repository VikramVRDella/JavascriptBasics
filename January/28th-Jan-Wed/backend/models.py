from sqlalchemy import Column, String, Integer,ForeignKey
from sqlalchemy.orm import relationship
from database import Base,engine

class BaseModel(Base):
    __abstract__ =True
    __allow_unmapped__ =True
    id = Column(Integer,primary_key=True,autoincrement=True)

class Address(BaseModel):
    __tablename__ = "addresses"
    city=Column(String(50),nullable=False)
    state = Column(String(25))
    zip_code = Column(Integer)
    user_id = Column(ForeignKey("users.id"))
    user = relationship("User",back_populates="address")

class User(BaseModel):
    __tablename__ = "users"
    name = Column(String(50),nullable=False)
    age = Column(String(75))
    address = relationship("Address",back_populates="user")