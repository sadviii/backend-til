"""Create a small Library Management System from scratch.

Requirements

A library has books and members.

Your program should be able to:

Create a Book with:
title
author
availability
Create a Member with:
name
member ID
A member should be able to borrow a book.
A book can only be borrowed if it is available.
After borrowing, the book should become unavailable.
A member should be able to return a book.
After returning, the book should become available again.
Your program should display useful information about a book when you print it.
Example behavior

Your program should be able to do something like:

Book: Python Basics
Author: John Smith
Available: True

Sadvika borrowed Python Basics

Available: False

Sadvika returned Python Basics

Available: True"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            return True
        else:
            return False

    def return_book(self):
        self.available = True

    def __str__(self):
        return f"Book: {self.title}\nAuthor: {self.author}\nAvailable: {self.available}"
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    def borrow_book(self, book):
        if book.borrow():
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} is not available for borrowing.")

    def return_book(self, book):
        book.return_book()
        print(f"{self.name} returned {book.title}")
book1 = Book("Python Basics", "John Smith")
member1 = Member("Sadvika", "M001")

print(book1)

member1.borrow_book(book1)
print(book1)

member1.return_book(book1)
print(book1)

















#practice

"""class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, subject):
        print(self.name, "is studying", subject)
student1 = Student("Sadvika", 22)

student1.study("Python")"""

"""class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
account = BankAccount(5000)
account.deposit(1000)
print(account.balance)"""

"""class Student:
    
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def display_details(self):
       print(self.name,self.age,self.course)
student1=Student("sadvi",22,"python")
student2=Student("Ghana",22,"aiml")

student1.display_details()
student2.display_details()"""

"""class Bankaccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit_amount(self,amount):
        self.balance=self.balance + amount
account=Bankaccount(100000)
account.deposit_amount(500000)

print(account.balance)"""


"""class Calculator:
    def add(self,a,b):
        return (a+b)

calculator = Calculator()

result = calculator.add(20, 30)

print(result)"""

#calculator with multiple operations
"""class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b
calculator = Calculator()
result1 = calculator.add(10, 20)
result2 = calculator.subtract(20, 10)
result3 = calculator.multiply(10, 20)

print("Addition:", result1)
print("Subtraction:", result2)
print("Multiplication:", result3)"""

"""class Student:
    college="RIT"
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
student1=Student("sadvi",22,"python")
student2=Student("Ghana",22,"aiml")

print(student1.name,student1.age,student1.course,student1.college)
print(student2.name,student2.age,student2.course,student2.college)"""

"""class calculator:
    @staticmethod
    def is_even(number):
        return number % 2 == 0
print(calculator.is_even(10))
print(calculator.is_even(7))"""

#inheritance
"""class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
dog=Dog()
dog.eat()
dog.bark()"""

#OVERREDING
"""class Vehicle:
    def start(self):
        print("Vehicle is starting")
class Car(Vehicle):
    def start(self):
        print("Car is starting") 
vehicle=Vehicle()
car=Car()
vehicle.start()
car.start()"""


#polymorphism
"""class Dog:
    def sound(self):
        print("Woof")
class Cat:
    def sound(self):
        print("Meow")
class Cow:
    def sound(self):
        print("Moo")
animals=[Dog(), Cat(), Cow()]
for animal in animals:
    animal.sound()"""

#encapsulation   

"""class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount")

    def get_balance(self):
        return self.__balance

account = BankAccount(5000)

account.deposit(1000)

print(account.get_balance())"""

#Abstractiohn

"""from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Woof")  
class Cat(Animal):
    def sound(self):
        print("Meow")
dog = Dog()
cat = Cat()
dog.sound()"""

#composition

"""class Engine:

    def start(self):
        print("Engine started")


class Car:

    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()

engine = Engine()
car = Car(engine)
car.start()"""

#multiple inheritance and method resolution order (MRO)
"""class Father:
    def skill(self):
        print("programming")
class Mother:
    def skill(self):
        print("Painting")

class Child(Father, Mother):
    pass
child = Child()
child.skill() 
print(Child.mro())  # Calls Father's skill method"""


"""class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
student = Student("Sadvika", 22)

print(student)"""
#__str__ method 
"""class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"
student = Student("Sadvika", 22)

print(student)"""


"""class Student:

    def __init__(self, name, age,course):
        self.name = name
        self.age = age
        self.course=course

    def __str__(self):
        return f"{self.name} - {self.age} - {self.course}" 
student = Student("Sadvika", 22,"Python")
print(student)"""


#len method
"""class Team:

    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)
team = Team(["A", "B", "C"])

print(len(team))"""    


"""class Student:

    def __init__(self, name):
        self.name = name
student1 = Student("Sadvika")
student2 = Student("Sadvika")
print(student1 == student2)"""


"""class Team:

    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)
team = Team(["A", "B", "C", "D", "E"])

print(len(team))"""

#__eq__ method


"""class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


student1 = Student("Sadvika", 22)
student2 = Student("Sadvika", 22)
student3 = Student("Ghana", 22)

print(student1 == student2)
print(student1 == student3)"""

#@property 

"""class Person:

    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 0:
            self.__age = value
        else:
            print("Invalid age")
person = Person(22)

print(person.age)

person.age = 25
print(person.age)

person.age = -5 """

          
