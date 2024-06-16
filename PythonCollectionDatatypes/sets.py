# Creating a set
names = {"Sia", "Mia", "Tia"}
print(names)
print(len(names))
print(type(names))

# Accesing 
for x in names:
    print(x)

# check if an element is exist
if "Sia" in names:
    print("Sia is part of the set")


# Add elements in the set
names.add("Sia")
print(names)

# Add another sequence in a set
names_list = ["Ria", "Kia"]
names.update(names_list)
print(names)

# Removing element from a set
names.remove("Ria")
# names.remove("Ria")   # It will thow an error 
names.discard("Ria")  # this function will not throw an error if value is not present in set
print(names)


# Join 2 sets
s1 = {'a','b','c'}
s2 = {'d','e','a'}
print(s1, s2)

# s3 = s1.union(s2)
# print(s3)

# s1.update(s2)
# print(s1)

# Keep only duplicates while joining
# s1.intersection_update(s2)
# print(s1)


# Keep all values except duplicates
s1.symmetric_difference_update(s2)
print(s1)


# to find the common elements in three sorted lists
l1 = [1,5,5,10]
l2 = [3,4,5,5,10]
l3 = [5,5,10,20]

s1 = set(l1)
s2 = set(l2)
s3 = set(l3)

s1s2 = s1.intersection(s2)
final_set = s1s2.intersection(s3)
final_list = list(final_set)
print(final_list)


