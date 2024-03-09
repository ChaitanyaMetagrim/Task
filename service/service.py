from stud_domain.domain import StudentDomain
from stud_schema.schema import Student ,StudentCreate
from stud_repo.repository import StudentRepository
from typing import List


class StudentService:
    def __init__(self):
        self.repo = StudentRepository()

    def create_student(self, student_data: StudentCreate) -> Student:
        student_domain = StudentDomain(name=student_data.name, date_of_birth=student_data.date_of_birth)
        age = student_domain.calculate_age()
        return self.repo.create_student(student_data, age)

    def get_all_students(self) -> List[Student]:
        return self.repo.get_all_students()

