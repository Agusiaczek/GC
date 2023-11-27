# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 14:03:08 2023

@author: student
"""


class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return "Library: " + self.city + ", " + self.street + "\nZip Code: " + self.zip_code + "\nOpen Hours: " + self.open_hours + "\nPhone: " + self.phone


class Employee:
     def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
     def__str__(self):
        return "Employee: " + self.first_name + " " + self.last_name + "\nHire Date: " + self.hire_date + "\nBirth Date: " + self.birth_date + "\nAddress: " + self.city + ", " + self.street + ", " + self.zip_code + "\nPhone: " + self.phone


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return "Book: " + self.author_name + " " + self.author_surname + "\nPublished on: " + self.publication_date + "\nPages: " + str(self.number_of_pages) + "\nAvailable at: " + str(self.library)


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):

        book_list = "\n".join(["- " + book.author_name + " " + book.author_surname for book in self.books])
        return "Order by " + self.employee.first_name + " " + self.employee.last_name + " for " + str(self.student) + "\nDate: " + self.order_date + "\nBooks:\n" + book_list


libraries = [
    Library("City ABC", "Street 1", "12345", "8 - 16", "123-456-7590"),
    Library("City XYZ", "Street 2", "56789", "9 - 17", "987-624-3280")
]

books = [
    Book(libraries[0], "2022-01-01", "Alan", "Defoe", 456),
    Book(libraries[0], "2021-02-15", "Astrid", "Openhey", 123),
    Book(libraries[0], "2020-12-10", "Emily", "Inparis", 234),
    Book(libraries[1], "2022-07-20", "Howard", "Stark", 259),
    Book(libraries[1], "2019-06-30", "Andy", "Walker", 170)
]

employees = [
    Employee("Kamil", "Kowalski", "2021-01-15", "1990-05-25", "City ABC", "Street 3", "56789", "987-624-3288"),
    Employee("Aneta", "Nowakowska", "2020-11-10", "1988-08-12", "City XYZ", "Street 4", "12345", "444-555-6666"),
    Employee("Emilia", "Paluch", "2022-02-28", "1995-04-30", "City ABC", "Street 5", "12345", "777-888-9999")
]

orders = [
    Order(employees[0], "Student X", [books[0], books[2], books[4]], "2023-05-10"),
    Order(employees[1], "Student Y", [books[1], books[3]], "2023-06-20")
]

for order in orders:
    print(order)
