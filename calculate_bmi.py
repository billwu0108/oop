#!/usr/bin/python3


class Student:

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def bmi(self):
        return self.weight / (self.height / 100.0) ** 2

    def is_fat():
        return True if self.bmi >= 35 else False

students = [
    Student('bill', 169, 100),
    Student('brian', 164, 56),
    Student('eagle', 173, 20)
]

for student in students:
    if student.is_fat():
        print(student.name)
