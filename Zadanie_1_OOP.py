# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 13:51:35 2023

@author: student
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average = sum(self.marks) / len(self.marks)
        return average > 50

student1 = Student("Jan Kowalski", [20, 30, 20, 40, 30, 40, 20, 10, 50, 40, 20])
student2 = Student("Anna Nowak", [60, 80, 70, 65, 90, 89, 76, 78, 95, 83, 98,])

print(student1.is_passed())  
print(student2.is_passed())  
