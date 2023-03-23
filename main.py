###Task 1

class Car:
    def __init__(self, brand, model):
        self.brand  = brand
        self.model  = model
        self._speed = 12

    def accelerate(self, increase):
        self._speed += increase
        print(f"Current speed of the {self.brand} {self.model} is: {self._speed}km/h")

print("########################################################################")
speed = Car("Toyota", "Camry")
speed.accelerate(104)

###Task 2

class Employee:
    def __init__(self, name, age):
        self.name    = name
        self.age     = age
        self._salary = 0
        self.__id    = 1619616531
    
    def name_age(self):
        print(f"{self.name} is {self.age} years old")
    
    def _display_salary(self, new_salary):
        self._salary = new_salary
        print(f"His salary is: {self._salary}$")
    
    def __display_id(self):
        print(f"His privat id is: {self.__id}")

print("########################################################################")
info = Employee("Anybody", 35)
info.name_age()
info._display_salary(5000)
info._Employee__display_id()

###Task 3

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self._age = age

    @property
    def age(self):
        return f"Age is: {self._age}"
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be less than 0")
        self._age = value

print("########################################################################")
p = Person("Any", "Body", 27)
print(p.age)  
p.age = 2
print(p.age)

###Task 4

class Student:
    def __init__(self, name, course, grade):
        self.name = name
        self.course = course
        self._grade = grade
        self.__student_id = 53164

    def display_public(self):
        print(f"The student {self.name} is on the {self.course} course.")

    def _display_grade(self):
        print(f"The average grade of the {self.name} is: {self._grade}")

    def __display_student_id(self):
        print(f"The privat id of the student {self.name} is: {self.__student_id}")

print("########################################################################")
s = Student("Name", 5, 100)
s.display_public()
s._display_grade()
s._Student__display_student_id()

###Task 5

class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = balance
    
    def deposit(self, amount):
        self._balance += amount
        print(f"Deposit successful. Current balance: ${self._balance}")
        
    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient balance.")
        else:
            self._balance -= amount
            print(f"Hey, {self.account_holder} withdrawal from {self.account_number} account is successful. Current balance: ${self._balance}")        
            
print("########################################################################")
account = BankAccount(1234567899876543, "Holder", 10000)
account.deposit(500)
account.withdraw(1000)

###Task 6

class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._area = length * width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, new_length):

        self._length = new_length
        self._area = self._length * self._width

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        self._width = new_width
        self._area = self._length * self._width

    @property
    def area(self):
        return f"The area is: {self._area}"

print("########################################################################")
rec = Rectangle(5, 5)
print(rec.area)

rec.length = 7
print(rec.area)

rec.width = 2
print(rec.area)


    




