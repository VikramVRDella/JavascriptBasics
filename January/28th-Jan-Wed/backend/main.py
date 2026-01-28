from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from models import User
from database import Base,engine, get_db
from schemas import UserResponse,UserCreate

app=FastAPI(
    title="Relationship API"
)

Base.metadata.create_all(engine)

@app.get("/api/get/")
def get_all_users(db:Session=Depends(get_db)):
    # return db.query(User).filter(User.age>21,User.age<24).all()
    # return db.query(User).offset(0).limit(10).all()
    return db.query(User).all()

@app.get("/api/get/{id}")
def get_single_user(id:int,db:Session=Depends(get_db)):
    return db.query(User).filter(User.id == id).first()

@app.post("/api/post/")
def create_users(user:UserCreate,db:Session=Depends(get_db)):
    users = User(**user.dict())
    db.add(users)
    db.commit()
    db.refresh(users)
    return users
