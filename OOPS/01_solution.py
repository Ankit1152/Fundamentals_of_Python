# class and object
# Q1. Create a Car class with attributes like brand and model. Then create an instance of the class 
class Car:
    # class variable to keep track of the total number of cars created 
    # Q6. Add a class variable in Car class to keep track of the total number of cars created 
    total_car = 0
    def __init__(self, brand, model):
        # Encapsulation
        # Q4. Modify the car class to encapsulate the brand attribute, making it private and provide a getter method for it
        # self.brand = brand
        self.__brand = brand
        # self.model = model

        # Q8. Use a property decorator in the car class to make the model attribute read only 
        # to make this variable read only 
        self.__model = model
        Car.total_car += 1

    # Polymorphism
    # Q5. Demonstrate polymorphism by defining a method fuel_type in both Car and Electric Car classes , 
    # but with different behaviours
    def fuel_type(self):
        return "Diesel or Petrol"

    def get_brand(self):
        return self.__brand

    # class method and Self
    # Q2. Add a method to the car class that displays the full name of the car (brand and model)
    def getFullName(self):
        return f"{self.__brand} {self.__model}"
    
    # static method :- belongs to the class rather than an instance of the class
    # Q7. Add a static method in Car class that returns a general description of a car
    @staticmethod
    def generaldescription():
        return "This is a general description of a car"
    

    # Property decorators :- allows us to create read-only attributes
    # Q8. Use a property decorator in the car class to make the model attribute read only 
    # to make this variable read only 

    @property  # This property decorator makes the attribute read-only 
    def model(self):
        return self.__model
    

# Inheritance
# Q3. Create an ElectricCar class that inherites from the Car class and has an additional attribute like battery_size
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Power"
    


myTesla = ElectricCar("Tesla","Model S", "85kwh")

# Q9. Check if myTesla object is an instance of both Car and ElectricCar classes.
print(isinstance(myTesla, Car)) 
print(isinstance(myTesla, ElectricCar)) 


# print(myTesla.__brand)
print(myTesla.model, myTesla.battery_size)
print(myTesla.getFullName())   # Output: Tesla Model S
print(myTesla.get_brand())   # Output: Tesla
print(myTesla.fuel_type())   # Output: Electric Power

nexon = Car("Tata", "Nexon")
mercedes = Car("Mercedes", "Benz")
print(nexon.model) # Output: Nexon
print(mercedes.fuel_type()) # Output: Diesel or Petrol
print(Car.total_car) 

print(Car.generaldescription()) # Output: This is a general description of a car



# myCarObj = Car("Tata","Safari")
# print(myCarObj.brand)  
# print(myCarObj.model)   
# print(myCarObj.getFullName())   


# Q10. Multiple Inheritance
class Battery:
    def battery_info(self):
        return "This is a battery"
    
class Engine:
    def engine_info(self):
        return "This is an engine"
    
class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla","Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())