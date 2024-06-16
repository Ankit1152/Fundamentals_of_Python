# del keyword
# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Ankit")
# print(s1.name)
# del s1.name          # del keyword is basically is used to delete the object properties and object itself
# print(s1.name)


# private attribute and methods
# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass    #  __ used to make a attribute private

#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1 = Account("4955101002918", "abcde")
# print(acc1.acc_no)
# print(acc1.reset_pass())


# class Person:
#     __name = "Anonymous"

#     def __hello(self):
#         print("Hello Person")

#     def welcome(self):
#         self.__hello()

# p1 = Person()
# p1.welcome()


# Inheritance
# Single Inheritance example
# class Car:
#     color = "Blue"

#     @staticmethod
#     def start():
#         print("Car started")

#     @staticmethod
#     def stop():
#         print("Car stopped")

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("Mercedes")
# car2 = ToyotaCar("BMW")
# print(car1.name)
# car1.start()
# print(car1.color)


# Multilevel Inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("Car started")

#     @staticmethod
#     def stop():
#         print("Car stopped")

# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.brand = brand


# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("Diesel")
# car1.start()



# Multiple Inheritance
# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"

# class C(A, B):
#     varC = "welcome to class C"

# c1 = C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)



# super method
# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("Car started")

#     @staticmethod
#     def stop():
#         print("Car stopped")

# class ToyotaCar(Car):
#     def __init__(self, name,type):
#         super().__init__(type)
#         self.name = name
#         super().start()

# car1 = ToyotaCar("Audi" , "Electric")
# print(car1.type)


# class method decorator
# class Person:
#     name = "ss"

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name

# p1 = Person()
# p1.changeName("Rahul Kumar")
# print(p1.name)
# print(Person.name)


# property decorator
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((self.phy + self.chem + self.math)/3)+"%"

    # def calcPercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math)/3)+"%"

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3)+"%"

s1 = Student(98,97,99)
print(s1.percentage)

s1.phy = 86
print(s1.percentage)



# Operator Overloading   + meaning has different with different datatypes
print(1+2+3)
print("Learning"+"Pyhton")
print([1,2,3] + [4,5,6])



# class for creating complex number
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
    
num1 = Complex(1,8)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()


num3 = num1 + num2
num3.showNumber()

# num3 = num1 - num2
# num3.showNumber()


# Q1. 
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius
    
c1 = Circle(21)
print(c1.area())
print(c1.perimeter())


# Q2
class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("Role = ",self.role)
        print("Department = ",self.department)
        print("Salary = ",self.salary)


class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Enginner","IT", 80000)


engg1 = Engineer("Elon Musk", 40)
engg1.showDetails()


# Q2. 
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price

    
ord1 = Order("Chips", 20)
ord2 = Order("Tea", 15)

print(ord1 > ord2)

