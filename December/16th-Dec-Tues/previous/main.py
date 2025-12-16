from fastapi import FastAPI, Depends
from schemas import TodoCreate
from database import SessionLocal,Base,engine
from sqlalchemy.orm import Session
from models import TodoModel

Base.metadata.create_all(bind=engine)
app=FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/todo", response_model=TodoCreate)
def create(todo:TodoCreate,db:Session=Depends(get_db)):
    db_todo=TodoModel(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh()
    return db_todo

