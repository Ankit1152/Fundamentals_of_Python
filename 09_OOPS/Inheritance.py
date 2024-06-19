class Parent:
    def __init__(self):
        print("Parent class Constructor")
        self.super_attribute = 50

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child class Constructor")
        print("Super atrribute" , self.super_attribute)

child1 = Child()


# Q 
class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def get_Fare(self):
        return self.seating_capacity * 100
    
class Bus(Vehicle):
    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)

    def get_Fare(self):
        vehicle_fare = super().get_Fare()
        maintainence_fee = vehicle_fare * 0.1
        total_fare = vehicle_fare + maintainence_fee
        return total_fare
    
vehicle1 = Vehicle(50)
vehicle1.get_Fare()  # Output: 5000

bus1 = Bus(50)
bus1.get_Fare()  # Output: 5500.0
        
