# class and object
# Q1. Create a Car class with attributes like brand and model . Then create an instance of the class 
class Car:
    def __init__(self, brand, model):
        # Encapsulation
        # Q4. Modify the car class to encapsulate the brand attribute, making it private and provide a getter method for it
        # self.brand = brand
        self.__brand = brand
        self.model = model

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
        return f"{self.__brand} {self.model}"
    

# Inheritance
# Q3. Create an ElectricCar class that inherites from the Car class and has an additional attribute like battery_size
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Power"

myTesla = ElectricCar("Tesla","Model S", "85kwh")
# print(myTesla.__brand)
print(myTesla.model, myTesla.battery_size)
print(myTesla.getFullName())   # Output: Tesla Model S
print(myTesla.get_brand())   # Output: Tesla
print(myTesla.fuel_type())   # Output: Electric Power

mercedes = Car("Mercedes", "Benz")
print(mercedes.fuel_type()) # Output: Diesel or Petrol



# myCarObj = Car("Tata","Safari")
# print(myCarObj.brand)  
# print(myCarObj.model)   
# print(myCarObj.getFullName())   

