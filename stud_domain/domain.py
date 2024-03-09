from datetime import date
from typing import List

class StudentDomain:
    def __init__(self, name: str, date_of_birth: date):
        self.name = name
        self.date_of_birth = date_of_birth

    def calculate_age(self) -> int:
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

