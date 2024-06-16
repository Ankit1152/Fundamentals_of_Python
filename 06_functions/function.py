# def calc_Sum(a,b):
#     s = a + b
#     return s 

# Positional Arguements
# print(calc_Sum(52,25))

# def calc_avg(a,b,c):
#     sum = a + b + c
#     avg = sum / 3
#     return avg

# print(calc_avg(5,10,15))

# cities = ["Delhi","Gurgaon","Chennai","Dhaka","Mumbai"]

# def print_len(list):
#     print(len(list))

# print_len(cities)

# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(cities)

# Recursion
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)

# show(5)

# Factorial
# def factorial(n):
#     if(n == 1 or n == 0):
#         return 1
#     else:
#         return factorial(n-1) * n
    
# print(factorial(5))



# Sum of first n natural numbers
# def sum(n):
#     if(n == 0):
#         return 0
#     else:
#         return sum(n-1) + n

# print(sum(10))

# Printing a list elemnts using recursive function
# hint : function takes two parameters list, and idx
# fruits = ["Apple","Pomegranate","Watermelon","Oranges"]
# def print_list(list, idx=0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)

# print_list(fruits)


# Arbitary Arguements
# def sum(*args):
#     sum = 0
#     for val in args:
#         sum += val
#     return sum

# output = sum(2,5,6,4,8,9,7)
# print(output)



# **kwargs
# def studentInfo(**kwargs):
#     for x,y in kwargs.items():
#         print(x,"is",y)

# studentInfo(name="Ankit", age = 22, city="Patna")
# studentInfo(name="Saumya", age = 24, city="Delhi")


# nested function
# def outer_function():
#     x = 4

#     def inner_funtion():
#         y = 5
#         s = x + y

#         return s
    
#     return inner_funtion()

# output = outer_function()
# print(output)


# pass by value  :- Immutable objects
def sumOne(a):
    a = a + 1
    print("Inside the function",a)

a = 5
print("Outside the function",a)
sumOne(a)


# pass by reference :- Mutable Objects (list, dictionaries)
def modifyList(list):
    list.append(5)
    print("Inside the function ",list)

list = [1,2,3,4]
modifyList(list)
print("Outside the function", list)


# Q Factorial


