import uuid
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from database import Base


class StudentModel(Base):
    __tablename__ = 'student_table'

    roll_no = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer)


class CourseModel(Base):
    __tablename__ = 'course_table'

    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String(60), nullable=False)

class EnrollmentTable(Base):
    __tablename__ = 'enrollment_table'

    enrollment_id = Column(Integer,primary_key=True,autoincrement=True)
    student_roll = Column(Integer, ForeignKey("student_table.roll_no"))
    course_id = Column(Integer, ForeignKey("course_table.course_id"))