from pydantic import BaseModel

class StudentBase(BaseModel):
    roll_no: int
    name:str
    age:int

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    pass

class CourseBase(BaseModel):
    course_name:str

class CourseCreate(CourseBase):
    pass

class CourseResponse(CourseBase):
    course_id:int

class EnrollmentBase(BaseModel):
    student_roll:int
    course_id:int

class EnrollmentCreate(EnrollmentBase):
    pass

class EnrollmentResponse(EnrollmentBase):
    Enrollment_id:int
    