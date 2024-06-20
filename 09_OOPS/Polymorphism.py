# Polymorphism in Python
# Polymorphism allows objects of different classes to be treated as objects of a common superclass.

# Runtime Polymorphism
class Animal:
    def speaks(self):
        pass

class Dog(Animal):
    def speaks(self):
        print("Barks")

class Cat(Animal):
    def speaks(self):
        print("Meows")

class Cow(Animal):
    def speaks(self):
        print("Moo")

dog = Dog()
cat = Cat()
cow = Cow()

print(dog.speaks())
print(cat.speaks())
print(cow.speaks())

# Compile Time Polymorphism
# Method Overloading
class Add:
    def sum(self, a,b):
        return a + b

    def sum(self, a, b, c):
        return a + b + c
    

# Operator Overloading :- Python supports operator overloading to perform operations on objects of user-defined classes.

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __str__(self):
        return f"{self.real} + {self.img}j"
    
complex1 = Complex(1, 2)

print(complex1 + Complex(3, 4))


# Runtime Polymorphism :- Python supports runtime polymorphism using method overriding.

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Barks"

class Cat(Animal):
    def speak(self):
        return "Meows"

animals = [Dog(), Cat()]    

for animal in animals:
    print(animal.speak()) # Output: Barks, Meows

