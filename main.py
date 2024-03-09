from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date, timedelta
from typing import List

from stud_service.service import StudentService

app = FastAPI()
student_service = StudentService()

class StudentCreate(BaseModel):
    name: str
    date_of_birth: date

class Student(BaseModel):
    id: int
    name: str
    age: int

@app.post("/students/", response_model=Student)
async def create_student(student_data: StudentCreate):
    student = student_service.create_student(student_data)
    return student

@app.get("/students/", response_model=List[Student])
async def get_students():
    return student_service.get_all_students()