# Tuples
# Creating a tuples

colors = ("Red", "Yellow", "Green")

# creating a tuple with 1 item
# fruit = ("fruit",)
fruit = tuple(("Apple"))

# Check type of tuple
print(type("fruit"))
print(fruit)

print(len(fruit))
print(len(colors))

# Accessing items
print(colors[1])
print(colors[-1])
print(colors[1 : 3])
print(colors[-2:])

# Check if an element is exist 
if "Yellow" in colors:
    print("Yellow is part of the tuple")


# Traverse the tuple
for i in colors:
    print(i)


# Concatenates two tuples
# more_colors = ("blue" , "brown")
# colors = colors + more_colors
# print(colors)


# Unpacking the tuples
color1, color2, color3 = colors
print(color1)
print(color2)
print(color3)


# Q. reverse a tuple
input_tuple = (1,2,3,4,5,6)

list = []

for x in reversed (input_tuple):
    list.append(x)

output_tuple = tuple(list)
print(output_tuple)