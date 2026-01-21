from pydantic import BaseModel

class StudentBase(BaseModel):
    roll:int
    name:str
    age:int

class StudentCreate(StudentBase):
    pass 

class StudentResponse(StudentBase):
    id:int

    class config:
        orm_mode:True