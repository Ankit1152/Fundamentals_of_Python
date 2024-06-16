# file = open("demo.txt", "r")
# # data = file.read(5)    # It reads the first 5 letters
# line1 = file.readline()   # It reds the first line of the file
# print(line1)
# print(type(line1))
# file.close()


# Writing to a file
# file = open("demo.txt","w")      # It overrites the file content 
# file = open("demo.txt","a")      # It appends the content at the last of the file 
# file.write("I am learning python now")   
# file.write("\nAfter that Django")   
# file.close()

# f = open("sample.txt", "w")
# f.close()

# f = open("demo.txt","r+")    # r+ mode enables the file in read mode and overrites from the beginning  
# f = open("demo.txt","w+")    # w+ mode enables the file in read mode and it truncates the file means overrites the
#                              # whole content of th file  
# f.write("ABC")
# f.read()            # we can also read the file 
# f.close()

# a+ read and append (ptr end) - no truncate


# With syntax  :- Another way to open write some operation done on the file
# with open("demo.txt","r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt", "w") as f:
#     f.write("New Data")


# Deleting a file
# import os

# os.remove("sample.txt")


# Practice Questions
# Q 1.
# with open("practice.txt", "w") as f:
#     f.write("Hii everyone\nwe are learning file I/O\nusing Java\n")
#     f.write("I like programming in Java")


# Q 2.
# with open("practice.txt", "r") as f:
#     data = f.read()
# new_data = data.replace("Java", "Python")

# with open("practice.txt", "w") as f:
#     f.write(new_data)



# Q3. Check for word in a file using file handling
# def check_for_word():
#     word = "learning"
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("found")
#         else:
#             print("not found")

# check_for_word()



# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1

# print(check_for_line())


count = 0
with open("sample.txt", "r") as f:
    data = f.read()
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
    
print(count)