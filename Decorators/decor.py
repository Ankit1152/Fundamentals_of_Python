# Decorators in Python :-  Decorators are a way to modify the behavior of a function or class. 
# 1. Function Decorators :- A function decorator takes a function as input and returns a new function.
#  They can be used to add functionality to existing functions.

# 2. Class Decorators :- A class decorator takes a class as input and returns a new class. 
# They can be used to add functionality to existing classes.

# 1. Function Decorators
def decor_result(result_function):
    def distinction(marks):
        for m in marks:
            if m >= 75:
                print("Distinction")
        result_function(marks)
    
    return distinction

@decor_result
def result(marks):
    for m in marks:
        if m >= 33:
            pass
        else:
            print("Failed")
    else:
        print("Pass")

result([50, 70, 80, 75])