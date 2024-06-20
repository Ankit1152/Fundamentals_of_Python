a = int(input("Enter the first Number "))
b = int(input("Enter the second number "))

try:
    result = a / b
    print("The result is: ", result)
except ZeroDivisionError:
    result = None
    print("Error: Division by zero is not allowed.")
finally:
    print("Division execution completed: ", result)   
