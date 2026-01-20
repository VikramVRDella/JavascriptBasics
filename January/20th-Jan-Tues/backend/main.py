from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from models import TodoModel
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
from database import Base,engine,get_db
from schemas import TodoCreate, TodoResponse

app=FastAPI(
    title = "Todo App",
    version="0.1.0"
)

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config("origins"),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/todo/fetch",response_model = list[TodoResponse])
def fetch_todo(db:Session=Depends(get_db)):
    return db.query(TodoModel).all()

@app.get("/todo/fetch/{id}",response_model = TodoResponse)
def fetch_single_todo(id:int,db:Session=Depends(get_db)):
    return db.query(TodoModel).filter(id == TodoModel.id).first()

@app.post("/todo/create",response_model=TodoResponse)
def create_todo(todo:TodoCreate,db:Session=Depends(get_db)):
    create = TodoModel(**todo.dict())
    db.add(create)
    db.commit()
    db.refresh(create)
    return create

@app.put("/todo/update/{id}",response_model= TodoResponse)
def update_todo(id:int,todo:TodoCreate, db:Session=Depends(get_db)):
    fetch_detail = db.query(TodoModel).filter(id == TodoModel.id).first()
    if not fetch_detail:
        raise HTTPException(status_code=404,detail="Detail not Found")
    else:
        if todo.title is None:
            fetch_detail.title = fetch_detail.title
        else:
            fetch_detail.title = todo.title
        if todo.description is None:
            fetch_detail.description = fetch_detail.description
        else:
            fetch_detail.description = todo.description
        if todo.completed is None:
            fetch_detail.completed = fetch_detail.completed
        else:
            fetch_detail.completed = todo.completed
    db.commit()
    db.refresh(fetch_detail)
    return fetch_detail

@app.delete("/todo/delete/{id}")
def delete_todo(id:int,db:Session=Depends(get_db)):
    delete = db.query(TodoModel).filter(TodoModel.id == id).first()
    db.delete(delete)
    db.commit()
    return "Task Deleted Successfully"


