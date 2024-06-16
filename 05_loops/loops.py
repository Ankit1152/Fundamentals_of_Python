# while loop

# count = 1
# while count <= 10:
#     print("Hello World")
#     count += 1
# print("Loop ended")

# Q1 Print Numbers from 1 to 100
# i = 1
# while i<=100:
#     print(i)
#     i += 1


# Q2 Print numbers from 100 to 1
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# Q3 . Multipliction of n
# n = int(input("Enter the number : "))
# i = 1
# while i <= 10:  
#     print(n*i)
#     i += 1


# Q4. Print the elements nums = [1,4,9,16,25,36,49,64,81,100]
# nums = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx <= len(nums)-1:
#     print(nums[idx])
#     idx += 1


# Q5. Print the elements tuples and find the element x in :-   nums = (1,4,9,16,25,36,49,64,81,100)
# nums = (1,4,9,16,25,36,49,64,81,100)

# x = int(input("Enter the number you have to find in the tuple :- " ))
# idx = 0
# while idx <= len(nums)-1:
#     if(nums[idx] == x):
#         print("Found at index value : ", idx)
#         break
#     else:
#         print("Finding")
#     idx += 1    

# print("End of loop")


# i = 0
# while i <= 5:
#     if(i == 3):
#         i+=1
#         continue
#     print(i)
#     i += 1

# Q6. Even number printing
# i = 0
# while i <= 10:
#     if(i % 2 != 0):
#         i += 1
#         continue
#     print(i)
#     i += 1


# Q7. Odd number printing
# x = 0
# while x <= 10:
#     if(x % 2 ==  0):
#         x += 1
#         continue
#     print(x)
#     x += 1


# for Loop  :- 
# nums = [2,4,6,5,8,9,7,8,9,10]
# for num in nums:
#     print(num)

# veggies = ["potatoes","Brinjal","Onion"]
# for veg in veggies:
#     print(veg)

# Tuples 
# tuples = (2,4,6,5,8,9,7,8,9,10)
# for tup in tuples:
#     print(tup)

# string = "ApnaCollege"
# for str in string:
#     print(str)

# nums = [1,4,9,16,25,36,49,64,81,100]
# for el in nums:
#     print(el)

# nums = (1,4,9,16,25,36,49,64,81,100,49)
# x = 49
# idx = 0
# for num in nums:
#     if(num == x):
#         print("Element found at index :- ",idx)
#         break
#     idx += 1


# range(start? , stop , step?)
for i in range(10):
    print(i)


# Odd number
for i in range(1,100,2):
    print(i)

# Even number
for i in range(2,101,2):
    print(i)    

# Multplication table
n = int(input("Enter the value of n :- "))
for i in range(1,11):
    print(n * i)


# pass statement
for i in range(5):
    pass

print("pass statement is a null statement that does nothing. It is used as a placeholder for future code")


# Q8. sum of first n natural numbers
n = int(input("Enter the number :- "))
sum = 0
for i in range(1, n+1):
    sum += i
    
print(sum)


# Q9. factorial of n
number = int(input("Enter the number :- "))
fact = 1
i = 1

# while i <= number:
#     fact *= i
#     i += 1

# print(fact)


for i in range(1, n+1):
    fact *= i

print(fact)



