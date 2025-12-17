from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from models import StudentModel
from schema import StudentMain,StudentCreate
from database import engine,Base,get_db
from fastapi.middleware.cors import CORSMiddleware

origins=[
    "http://localhost:5173"
]



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


Base.metadata.create_all(bind=engine)

@app.get("/student/get")
def get_student(id=None,db:Session=Depends(get_db)):
    if id == None:
        get_all=db.query(StudentModel).all()
        return get_all
    else:
        get_one=db.query(StudentModel).filter(StudentModel.id == id).first()
        return get_one

@app.post("/student/create")
def create_student(student:StudentCreate,db:Session=Depends(get_db)):
    db_add=db.add(StudentModel(**student.model_dump()))
    db.commit()
    return {"message":"New Student Created..."}

@app.put("/student/update")
def update_student(id:int,student:StudentCreate,db:Session=Depends(get_db)):
    db_fetch=db.query(StudentModel).filter(StudentModel.id == id).first()
    if db_fetch:
        db_fetch.roll_no = student.roll_no
        db_fetch.name = student.name
        db_fetch.age = student.age
        db.commit()
        return {"message" : "Student Updated.."}
    else:
        return {"message" : "Student Not Found"}

@app.delete("/student/delete")
def delete_student(id:int,db:Session=Depends(get_db)):
    db_delete=db.query(StudentModel).filter(StudentModel.id == id).first()
    db.delete(db_delete)
    db.commit()
    return {"message":"Student Deleted..."}

