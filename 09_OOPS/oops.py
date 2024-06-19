class Student:
    def setName(self, name):  
        self.name = name        # class attribute

    def getName(self):
        return self.name
    
student1 = Student()
student1.setName("Vikash")
print(student1.getName())
student1.eng_marks = 52     
print(student1.eng_marks)    # instance attribute

student2 = Student()
student2.setName("Riyan")
print(student2.getName())



# Q 
class Rectangle:

    # class Constructor
    def __init__(self, width, height):
        # print("Width = {width} and Height = {height}".format(width = width, height = height))
        print(f"Width = {width} and Height = {height}")
        self.width = width
        self.height = height

    # def set_Dimensions(self, width, height):
    #     self.width = width
    #     self.height = height

    def calculate_Area(self):
        return self.width * self.height
    
    def calculate_Perimeter(self):
        return 2 * (self.height + self.width)
    
rectangle1 = Rectangle(5,10)
rectangle2 = Rectangle(4,10)
rectangle3 = Rectangle(8,9)
# rectangle1.set_Dimensions(5, 10)

print("Width =",rectangle1.width)
print("Length =",rectangle1.height)
print("Area =",rectangle1.calculate_Area())
print("Perimeter =",rectangle1.calculate_Perimeter()) 


#  Access Modifier 
# public 
# class ABC:
#     def __init__(self):
#         self.public_attribute = None   # public attribute

#     def public_function(self):    # this is a public function
#         pass


# private 
# class ABC:
#     def __init__(self):
#         self.__private_attribute = 10   # private attribute

#     def __private_function(self):    # this is a private function
#         pass

# obj1 = ABC()
# # print(obj1.__private_attribute)
# print(obj1.__private_function)


# protected  
class ABC:
    def __init__(self):
        self._protected_attribute = 10   # protected attribute

    def _potected_function(self):    # this is a protected function
        print("Protected function")

obj1 = ABC()
# print(obj1._public_attribute)
print(obj1._protected_attribute)
print(obj1._potected_function)


