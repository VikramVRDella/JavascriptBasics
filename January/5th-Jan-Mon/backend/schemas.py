from pydantic import BaseModel

class StudentBase(BaseModel):
    roll_no:int
    name:str
    age:int

class StudentCreate(StudentBase):
    pass

class StudentGet(StudentBase):
    id:int

class Config:
    orm_mode=True