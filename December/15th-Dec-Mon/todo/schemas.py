from pydantic import BaseModel

class TodoBase(BaseModel):
    title:str
    description:str | None =None
    completed:bool

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id:str
    class Config:
        orm_mode=True
