#!/usr/bin/python3


class Student:

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def bmi(self):
        return self.weight / (self.height / 100.0) ** 2

    def is_fat(self):
        return True if self.bmi() >= 35 else False

# 如果我直接被執行的話，才執行以下的程式碼片段
# 阿如果我不是直接被執行，而是被 import 的話就不要執行
if __name__ == '__main__':
    students = [
        Student('bill', 169, 100),
        Student('brian', 164, 56),
        Student('eagle', 173, 20)
    ]

    for student in students:
        if student.is_fat():
            print(student.name)
