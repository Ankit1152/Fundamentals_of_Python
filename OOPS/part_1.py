# Student class
# class Student:
#     name = "Karan"

# s1 = Student()
# print(s1.name)
# s2 = Student()
# print(s2.name)

# class Student:
#     college_name = "BITS Pilani"     # class attribute
#     # Default constructor
#     def __init__(self):                     # self parameter always refer to the current instance of the class
#         pass

#     # Parameterized constructor
#     def __init__(self, name, marks):        # self parameter always refer to the current instance of the class
#         self.name = name   # object attribute
#         self.marks = marks  # object attribute
#         print('Adding new student in Database...')

#     def welcome(self):
#         print("Welcome Student, ",self.name)

#     def get_marks(self):
#         return self.marks

# s1 = Student("Ankit", 95)
# print(s1.name, s1.marks)
# s1.welcome()
# print(s1.get_marks())

# s2 = Student("Saumya", 85)
# print(s2.name, s2.marks)

# Car class
# class Car:
#     color = "blue"
#     brand = "Mercedes"

# car1 = Car()
# print(car1.brand)
# print(car1.color)



# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hii ", self.name, "your avg score is ", sum/3)

#     # Static methods 
#     @staticmethod      # decorator
#     def hello():  
#         print("Hello Ankit")

# s1 = Student("Ankit" , [98,99,97])
# s1.get_avg()
# s1.hello()

# Abstraction :- hiding the implementation details of a class from the user and showing only the esential features to the user
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brake = False
#         self.clutch = False

#     def car_Start(self):
#         self.acc = True
#         self.clutch = True
#         print("Car started")

# car1 = Car()
# car1.car_Start()


# Encapsulation
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs ",amount,"is debited")
        print("Total balance is Rs ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs ",amount, "is credited")
        print("Total balance is Rs", self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1 = Account(10000, 4955101002918)
print(acc1.balance)
print(acc1.account_no)

acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)
