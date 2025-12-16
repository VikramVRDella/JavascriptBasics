from pydantic import BaseModel

class TodoBase(BaseModel):
    title:str
    description:str
    completed:bool

class TodoMain(TodoBase):
    pass 

class TodoShow(TodoBase):
    id:int
    class Config:
        orm_mode=True