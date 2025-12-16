from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from database import Base, SessionLocal,engine
import model
from schemas import TodoMain, TodoShow

app=FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/todo")
def get(db:Session=Depends(get_db)):
    db_todos=db.query(model.TodoModel).all()
    return db_todos

@app.get("/todo/{id}")
def get_by_id(id:int,db:Session=Depends(get_db)):
    db_todo=db.query(model.TodoModel).filter(model.TodoModel.id == id).first()
    if db_todo:
        return db_todo
    else:
        return {"Error":"Product not found"}

@app.post("/todo/add",response_model=TodoMain)
def add_todo(todo:TodoMain,db:Session=Depends(get_db)):
    db_add=model.TodoModel(**todo.dict())
    if db_add:
        db.add(db_add)
        db.commit()
        db.refresh(db_add)
        return db_add
    else:
        return {"message":"Failed to add Product"}
    
@app.put("/todo/{id}",response_model=TodoMain)
def update_task(id:int,todo:TodoMain,db:Session=Depends(get_db)):
    db_update= db.query(model.TodoModel).filter(model.TodoModel.id == id).first()
    if db_update:
        db_update.title=todo.title
        db_update.description=todo.description
        db_update.completed=todo.completed
        db.commit()
        return {"message":"task updated"}
    else:
        return {"message":"task not found"}

@app.delete("/todo/delete/{id}")
def delete_task(id:int,db:Session=Depends(get_db)):
    delete_task=db.query(model.TodoModel).filter(model.TodoModel.id == id)
    if delete_task:
        db.delete(delete_task)
        db.commit()
        return {"message":"task Deleted"}
    else:
        return {"message":"Task not Found"}


