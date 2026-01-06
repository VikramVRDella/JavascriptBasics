from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models 
from schemas import StudentCreate, StudentResponse, CourseCreate, CourseResponse,EnrollmentCreate,EnrollmentResponse
from database import Base,engine,get_db

Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.post("/students/create/")
def student_create(student:StudentCreate,db:Session=Depends(get_db)):
    get_student=models.StudentModel(roll_no=student.roll_no,name=student.name,age=student.age)
    db.add(get_student)
    db.commit()
    db.refresh(get_student)
    return "Students Added"

@app.post("/course/create")
def course_create(course:CourseCreate,db:Session=Depends(get_db)):
    get_course = models.CourseModel(course_name=course.course_name)
    db.add(get_course)
    db.commit()
    db.refresh(get_course)
    return "Course Created"

@app.post("/enrollment/course")
def enroll_course(enroll:EnrollmentCreate,db:Session=Depends(get_db)):
    get_enrollment = models.EnrollmentTable(student_roll=enroll.student_roll,course_id=enroll.course_id)
    db.add(get_enrollment)
    db.commit()
    db.refresh(get_enrollment)
    return "Course Enrolled..."


@app.get("/students/get/")
def get_all_students(db:Session=Depends(get_db)):
    get_student = db.query(models.StudentModel).all()
    return get_student

@app.get("/courses/enrolled/")
def courses_enrolled_by_student(roll: int, db: Session = Depends(get_db)):
    student = db.query(models.StudentModel).filter(models.StudentModel.roll_no == roll).first()
    enrollments = db.query(models.EnrollmentTable).filter(models.EnrollmentTable.student_roll == roll).all()
    course_ids = [enrollment.course_id for enrollment in enrollments]
    courses = db.query(models.CourseModel).filter(models.CourseModel.course_id.in_(course_ids)).all()
    return {
        "student": student,
        "courses": courses
    }

