#----------------------
# Dictionary creation
#----------------------
# A dictionary stores data in key-value pairs
'''
--> A dictionary is created using curly braces {}
--> Data is stored in key : value format
--> Keys must be unique
--> Values can be duplicated
--> Dictionaries are mutable (can be changed)
'''
d = {
    1: "sandhya",   # key 1 maps to value "sandhya"
    2: "mounika",   # key 2 maps to value "mounika"
    3: "varsha",    # key 3 maps to value "varsha"
    4: "nandhu",    # key 4 maps to value "nandhu"
    5: "shiva"      # key 5 maps to value "shiva"
}
print(d)
print(d[2])
print(d[1])
print("mounika" in d)
print(1 in d)
#--------------------------------------------------------------------------



#---------------------------
# Add elements to dictionary
#---------------------------
# Creating a dictionary with initial key-value pairs
d = {1: "c", 2: "java", 3: "python"}
print(d)

# Adding a single element using a new key
d[4] = "c++"
print(d)

# Adding another element using a new key
d[5] = "java script"
print(d)

# Add multiple elements to dictionary using update()
# update() adds multiple key-value pairs at once
d.update({6: "c#", 7: "visual basics"})
print(d)

# Adding elements using keyword arguments
# Keys are treated as strings automatically
d.update(seven="ruby", eight="php")
print(d)
#--------------------------------------------------------------------------



#---------------------------------
# Modify the value of a dictionary
#---------------------------------
# Creating a dictionary
d = {1: "c", 2: "java", 3: "python"}
print(d)

# Modifying the value of an existing key
# The value of key 2 is changed from "java" to "python"
d[2] = "python"

# Printing the updated dictionary
print(d)
#--------------------------------------------------------------------------



#------------------------------------
# Delete elements from the dictionary
#------------------------------------
# Creating a dictionary
d = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
print(d)

# Removing an element using pop(key)
# Removes the key-value pair with key 3
d.pop(3)
print(d)

# Removing an element using pop(key) and storing its value
# Removes key 4 and returns its value
value = d.pop(4)
print(value)
print(d)

# Removing the last inserted key-value pair using popitem()
d.popitem()
print(d)

# Deleting a specific key-value pair using del keyword
del d[1]
print(d)

# pop(key, default)
# Tries to remove key 4
# If key 4 is not found, it returns the default value (0)
print(d.pop(4, 0))

# Removing all elements from the dictionary using clear()
d.clear()
print(d)
#--------------------------------------------------------------------------



#--------------------------------------------
#Dictionary with Immutable and Mutable Values
#--------------------------------------------
d = {1: 'a', 2: [10, 20, 30]}

# Accessing value using key 1
print(d[1])        # Output: a

# Assigning the value of d[1] to variable x
x = d[1]
print(x)           # Output: a

# Changing x does NOT change the dictionary
# Because strings are immutable
x = 'b'
print(d[1])        # Output: a (no change)

# Accessing first element of list stored at key 2
print(d[2][0])     # Output: 10

# Assigning first list element to x
x = d[2][0]
print(x)           # Output: 10

# Assigning entire list to x
x = d[2]
print(x)           # Output: [10, 20, 30]

# Modifying the list using x
# Lists are mutable, so this affects the dictionary
x.append(50)
print(d)           # Output: {1: 'a', 2: [10, 20, 30, 50]}
#--------------------------------------------------------------------------



#------------------------------------------------------
# Different ways to access elements from the dictionary
#------------------------------------------------------
d = {1: "java", 2: "python", 3: "c", 4: "c++", 5: "javascript"}

# Accessing all keys
print(d.keys())

# Accessing all values
print(d.values())

# Accessing all key-value pairs
print(d.items())

# Converting keys to list
print(list(d.keys()))

# Converting values to list
print(list(d.values()))

# Converting items to list
print(list(d.items()))
#--------------------------------------------------------------------------



#--------------------------------------
# Access keys and values using for loop
#--------------------------------------
d = {1: "java", 2: "python", 3: "c", 4: "c++", 5: "javascript"}

# Printing all keys
for i in d.keys():
    print(i, end=" ")
print()

# Printing all values
for value in d.values():
    print(value, end=" ")
print()

# Printing keys and values together
for key, value in d.items():
    print(key, value)
#--------------------------------------------------------------------------



#---------------------------------------
# Count of occurrences of each character
#---------------------------------------
str = input("Enter your name: ")
d = {}

# Converting string to uppercase and counting characters
for i in str.upper():
    if i not in d:
        d[i] = 1        # First occurrence
    else:
        d[i] = d[i] + 1  # Increment count

# Printing the dictionary
print(d)
#--------------------------------------------------------------------------



#--------------------------------
# Number of pairs in a given list
#--------------------------------
lst = list(map(int, input("Enter your values: ").split()))

d = {}

# Counting frequency of each element
for i in lst:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1

# Calculating total number of pairs
res = 0
for i in d.values():
    res = res + i // 2

# Printing the result
print(res)
