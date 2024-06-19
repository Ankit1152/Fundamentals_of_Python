# name1 = 'My name is Ankit'
# name2 = "My name is Ankit"
# name3 = '''My name is Ankit 
# Kumar. I am 23  years old'''

# print(name1)
# print(name2)
# print(name3)
# print(type(name3))
# print(type(name3))
# print(type(name3))

# Array like indexing in list
# print(name1[0])
# print(name1[-1])

# traversing in a string
# for i in name1:
#     print(i, end=" ")
# print()
# Using list comprehension
# list = [char for char in name1]
# for i in list:
#     print(i)

# Find the length of the strength
# print(len(name1))

# Find the char or substring 
# print(name1.find("Ank"))   # it returns first occurence of the char or substring

# Slicing a string
# P Y T H O N   P R O G  R  A  M  M  I  N  G
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
# str = "PYTHON PROGRAMMING"
# print(str[7:])
# print(str[7:14])
# print(str[-7:])   # Negative indexing


# Modifying Strings using the string
# str1 = 'new york'
# str2 = str1.upper()
# print(str2)
# str3 = str2.lower()
# print(str3)
# str4 = str3.capitalize()
# print(str4)

# for stripping/removing any trailing whitespaces
# str5 = "      Program         "
# print(str5.strip())
# print(str5)


# replace
# str6 = "Hello world, what a beautiful world this is"
# print(str6.replace("world", "earth"))
# print(str6.replace("world", "earth",1))


# splitting strings
# str1 = "sia,mia,tia,pia,kia,ria"
# list = str1.split(",",2)
# print(list)

# Concatenation
# s1 = "Hello World !"
# s2 = "This is great place"
# print(s1 + s2)


#  String formatting
# name = "Ankit Kumar"
# age = 23
# s3 = "My name is {name} and I am {age} years old".format(name = name, age = age)
# print(s3)


# text1 = "The unexpected always happens "
# print(text1)
# print(len(text1))
# print(text1.find("pp"))
# print(text1[:11])
# print(text1.replace("always", "never"))
# text2 = "no matter what"
# final_string = text1 + text2
# print(final_string)


# String is palindrome or not
def check_Palindrome(str):
    # cleaning string
    cleaned_str = (str.replace(" ","")).lower()

    reverse_str = cleaned_str[::-1]

    return cleaned_str == reverse_str

str = input("Enter the string :- ")

if check_Palindrome(str):
    print("It is palindrome")
else:
    print("Not a paindrome")