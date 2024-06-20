
# Abstraction in Python :- Abstraction is a process of hiding the internal details and showing only the essential features 
# or properties of 

class Car:
    def __init__(self):
        self.acc = False
        self.brake = False
        self.clutch = False
    
    def car_start(self):
        self.acc = True
        self.clutch = True
        print("Car started")

car1 = Car()

# Abstract method
class Vehicle:
    def start(self):
        pass

class ToyotaCar(Vehicle):
    def start(self):
        print("Toyota car started")

car2 = ToyotaCar()

car1.car_start()

car2.start()

# Encapsulation in Python :- Encapsulation is a process of bundling data and methods into a single unit called a class.
