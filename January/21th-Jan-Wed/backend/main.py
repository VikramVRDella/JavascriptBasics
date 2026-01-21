from fastapi import FastAPI,Depends,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import StudentCreate,StudentResponse
from models import StudentModel
from decouple import config
from sqlalchemy.orm import Session
from database import Base,get_db,engine

app = FastAPI(
    title = "StudentModel",
    version="0.1.0"
)

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins = config("origins"),
    allow_credentials = True,
    allow_headers = ["*"],
    allow_methods= ["*"]
)

@app.get("/students/get",response_model=list[StudentResponse])
def get_Students(db:Session=Depends(get_db)):
    fetch_all = db.query(StudentModel).all()
    if not fetch_all:
        raise HTTPException(status_code=404,detail="No More Details")
    else:
        return fetch_all

@app.get("/students/get/{roll}",response_model=StudentResponse)
def get_single_student(roll:int,db:Session=Depends(get_db)):
    fetch_student = db.query(StudentModel).filter(StudentModel.roll == roll).first()
    if not fetch_student:
        raise HTTPException(status_code=404,detail="Detail not Found")
    else:
        return fetch_student

@app.post("/students/create",response_model=StudentResponse)
def create_student(student:StudentCreate,db:Session=Depends(get_db)):
    create = StudentModel(**student.dict())
    db.add(create)
    db.commit()
    db.refresh(create)
    return create

@app.put("/students/update/{roll}",response_model=StudentResponse)
def update_student(student:StudentCreate,db:Session=Depends(get_db)):
    fetch_student = db.query(StudentModel).filter(student.roll == StudentModel.roll).first()
    if not fetch_student:
        raise HTTPException(status_code=404,detail="Detail not Found")
    else:
        if fetch_student.name is None:
            fetch_student.name = fetch_student.name
        else:
            fetch_student.name = student.name
        if fetch_student.age is None:
            fetch_student.age = fetch_student.age
        else:
            fetch_student.age = student.age
    
    db.commit()
    db.refresh(fetch_student)
    return fetch_student
@app.delete("/students/delete/{roll}")
def delete_student(roll:int,db:Session=Depends(get_db)):
    fetch_student = db.query(StudentModel).filter(roll == StudentModel.roll).first()
    if not fetch_student:
        raise HTTPException(status_code=404,detail="Detail not Found")
    else:
        db.delete(fetch_student)
        db.commit()
    return "Student Deleted Successfully"

if __name__ =="__main__":
    import uvicorn 
    uvicorn.run(app="main:app",reload=True)