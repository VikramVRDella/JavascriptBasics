from fastapi import FastAPI, Depends,HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from models.todo import TodoModel
from db.database import get_db,create_tables
from schemas.todoSchema import TodoResponse, TodoCreate


app=FastAPI(
    title="Todo App",
    version="0.1.0"
)

create_tables()

app.add_middleware(
    CORSMiddleware,
    # allow_origins = settings.ALLOWED_ORIGINS,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_headers =["*"]
)

@app.get("/todo/fetch",response_model = list[TodoResponse])
def get_todo(db:Session=Depends(get_db)):
    fetch_todo = db.query(TodoModel).all()
    return fetch_todo

@app.get("/todo/fetch/{id}",response_model=TodoResponse)
def fetch_single_todo(id:int,db:Session=Depends(get_db)):
    fetch_single = db.query(TodoModel).filter(id == TodoModel.id).first()
    return fetch_single

@app.post("/todo/create",response_model=TodoResponse)
def create_todo(todo:TodoCreate,db:Session=Depends(get_db)):
    todos = TodoModel(**todo.dict())
    db.add(todos)
    db.refresh(todos)
    return todos 

@app.put("/todo/update/{id}",response_model=TodoResponse)
def update_todo(id:int,todo:TodoCreate, db:Session=Depends(get_db)):
    fetch_detail = db.query(TodoModel).filter(TodoModel.id == id).first()
    if not fetch_detail:
        raise HTTPException(status_code=404,detail='Detail not Found')
    for key,value in todo.dict().items():
        setattr(fetch_detail, key,value)
    db.commit()
    db.refresh(fetch_detail)
    return fetch_detail

@app.delete("/todo/delete/{id}")
def delete_todo(id:int, db:Session=Depends(get_db)):
    delete_detail = db.query(TodoModel).filter(TodoModel.id == id).first()
    if not delete_todo:
        raise HTTPException(status_code=404,detail='Detail not Found')
    db.delete(delete_detail)
    db.commit()
    return 'Todo Deleted Successfully'


