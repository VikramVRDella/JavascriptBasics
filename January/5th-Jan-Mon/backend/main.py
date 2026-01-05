from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from schemas import StudentCreate, StudentGet
from database import engine,get_db,Base

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.get('/student/get/{student_id}')
def get_students(Student_id = None,db:Session=Depends(get_db)):
    if Student_id == None:
        return db.query(models.StudentModel).all()
    else:
        get_student= db.query(models.StudentModel).filter(models.StudentModel.id == Student_id).first()
        return get_student

@app.post('/students/post/')
def create_students(student:StudentCreate, db:Session=Depends(get_db)):
    get_student = models.StudentModel(roll_no = student.roll_no,name=student.name,age=student.age)
    db.add(get_student)
    db.commit()
    db.refresh(get_student)
    return get_student

@app.put("/students/put/{student_id}")
def update_students(student_id:int,student:StudentCreate,db:Session=Depends(get_db)):
    get_student = db.query(models.StudentModel).filter(models.StudentModel.id == student_id).first()
    get_student.roll_no = student.roll_no
    get_student.name = student.name
    get_student.age  = student.age
    db.commit()
    db.refresh(get_student)
    return get_student

@app.delete("/students/delete/{student_id}")
def delete_student(student_id:int,db:Session=Depends(get_db)):
    remove_student=db.query(models.StudentModel).filter(models.StudentModel.id == student_id).first()
    db.delete(remove_student)
    db.commit()
    return "Student Deleted..."

