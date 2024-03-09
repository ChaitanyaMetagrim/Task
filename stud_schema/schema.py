from pydantic import BaseModel
from datetime import date

class StudentBase(BaseModel):
    name: str
    date_of_birth: date

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    age: int

    class Config:
        orm_mode = True