# 1. Strings are alpha numeric and all characters.
# 2. surrounded by double and single quotes


first_name = 'John'
last_name = "Ng'ang'a"

full_name = first_name +" "+ last_name
print(full_name)
#access methods use dots.

full_name = full_name.lower()
print(full_name.isprintable())
#deaing with numbes and  strins
num1 ="7"
num2= "8"
t = int(num1) + int(num2)
print(t)
#Indexing and Slicing
# Indexing is used when you want to get one part of a string[]
# Slicing is used when you want to get multiple part of a string
# Indexing[int]
print(full_name[-11])

# Slicing uses a colon[]:
#1st part- index(0) where you want to start
#2nd part-count(1)where you want to stop
print(full_name[0:6])
