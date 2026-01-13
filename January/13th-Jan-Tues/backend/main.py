from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import TodoModel
from decouple import config
from schemas import TodoResponse, TodoCreate
from fastapi.middleware.cors import CORSMiddleware
from database import Base,get_db,engine


app = FastAPI(title="TodoAPI")
Base.metadata.create_all(bind =engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config("host"),
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


@app.post("/todo/create/",response_model=TodoResponse)
def create_todo(todo: TodoCreate, db:Session = Depends(get_db)):
    todo_get = TodoModel(**todo.dict())
    db.add(todo_get)
    db.commit()
    db.refresh(todo_get)
    return todo_get

@app.get("/todo/get/",response_model=list[TodoResponse])
def fetch_todo(db:Session=Depends(get_db)):
    return db.query(TodoModel).all()

@app.get("/todo/get/{id}",response_model=TodoResponse)
def fetch_single_todo(id:int,db:Session=Depends(get_db)):
    fetch_detail = db.query(TodoModel).filter(TodoModel.id == id ).first()
    if not fetch_detail:
        raise HTTPException(status_code=404,detail='Detail not Found')
    return fetch_detail

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


