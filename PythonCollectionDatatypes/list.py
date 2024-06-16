fruits = ['mangoes',"Apple","banana","Kiwi"]
# print(fruits)
# print(len(fruits))
# print(type(fruits))


# Checking if an element is present in the list 
# if "banana" in fruits:
#     print("part of the fruits list")

# Checking if an element is not present in the list or not
# if "Pomegranate" not in fruits:
#     print("Not part of the list")



# Accessing the elemenst of the list
# print(fruits[1])
# print(fruits[-3])
# print(fruits[-3 : -1])
# print(fruits[1:3])


# Adding the elements to alist
# fruits.append("Pineapple")
# print(fruits)

# fruits.insert(2, "Guava")
# print(fruits)

# more_fruits = ["Cherry","Oranges"]
# fruits.extend(more_fruits)
# print(fruits)

# Removing elements from a list
# fruits.remove("banana")
# print(fruits)

# fruits.pop()   # or pop(2)
# print(fruits)


# Changing / updating item in a list
# fruits[1] = "Mosummi"
# print(fruits)

# fruits[1:3] = ["papaya"]
# # fruits[1:3] = "papaya"
# print(fruits)


# Sorting a list
# fruits.sort()
# print(fruits)

# fruits.sort(reverse=True)
# print(fruits)

# fruits.reverse()
# print(fruits)



# List Comprehension
# new_fruits = [fruit for fruit in fruits if "a" in fruit]
# print(new_fruits)

# Copy a list
# new_fruits = fruits.copy()
# print(new_fruits)

# Nested List
# fruits.insert(2, ["Pineapple", "Avocado"])  
# print(fruits)
# print(fruits[2][0])

# Q1. Swapping the list
n = int(input('Enter the size of the list :- '))
list = []
for _ in range(n):
    num = int(input())
    list.append(num)

idx1 = int(input("Enter the idx 1 : "))
idx2 = int(input("Enter the idx 2 : "))
print(list)

temp = list[idx1]
list[idx1] = list[idx2]
list[idx2] = temp

print(list)


# Q2.

