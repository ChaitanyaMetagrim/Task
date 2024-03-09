from stud_schema.schema import Student,StudentCreate
from stud_model.model import  StudentModel,Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from typing import List


class StudentRepository:
    def __init__(self):
        engine = create_engine('sqlite:///students.db')
        Base.metadata.create_all(engine)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def create_student(self, student_data: StudentCreate, age: int) -> Student:
        db_student = StudentModel(name=student_data.name, date_of_birth=student_data.date_of_birth, age=age)
        db = self.SessionLocal()
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        db.close()
        return db_student

    def get_all_students(self) -> List[Student]:
        db = self.SessionLocal()
        students = db.query(StudentModel).all()
        db.close()
        return students
