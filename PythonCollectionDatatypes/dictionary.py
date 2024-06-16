phones = {
    "John" : 985642,
    "Ria" : 456235,
    "Joy" : 789562
}

print(phones)
# print(type(phones))
# print(len(phones))

# Access items
# print(phones["John"])
# print(phones.get("John"))
# print(phones.keys())


# update value in dictionary
phones["John"] = 952323
print(phones)
 


# Add elements 
# phones["Kia"] = 956848
# print(phones)


# more_phones = {
#     "Kia" : 423615
# }

# phones.update(more_phones)
# print(phones)

# Remove elements
# phones.pop("John")
# print(phones)
 
# phones.popitem()  # This will remove last item in dict
# print(phones)  

# phones.clear()
# print(phones)

#  Iterating the dictionary
# for x in phones:
#     print(x)

for x in phones:
    print(phones[x])


for x,y in phones.items():
    print(x,y)

# Nested Dictionary
phones = {
    "Area1" : {
        "a" : 0,
        "b" : 1,
        "c" : 2
    },
    "Area2" : {
        "x" : 3,
        "y" : 4,
        "z" : 5
    }
}

print(phones["Area1"]["c"])
print(phones["Area2"]["y"])

# Q Sum of the dictionary values
dict = {
    'a' : 100,
    'b' : 200,
    'c' : 300
}

print("The sum of the dictionary values :-",sum(dict.values()))