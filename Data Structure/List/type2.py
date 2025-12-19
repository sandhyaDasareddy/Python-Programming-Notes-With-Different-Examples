#---------------------------------------------------------------------------------------------------
# Create copy of list (Shallow Copy)

lst1 = [10, 20, 30, 40, 50, 60, 70, 80]

# Method 1: Using slicing
lst2 = lst1[:]

# Method 2: Using list() constructor
lst3 = list(lst1)

# Check memory location
print(lst1 is lst2)
print(lst1 is lst3)


# Example with nested list
l1 = [[10,20], [30,40]]
l2 = list(l1)

print(l1)
print(l2)
print(l1 is l2)

#---------------------------------------------------------------------------------------------------
# append list to nested list
l1 = [[10,20,30],[40,50,60],[70,80,90]]
print(l1)
l2 = list(l1)
print(l2)
print(l1.append([100,110]))
print(l1)

print(l1[1][0])

print(l1)
l1[1][0] = 344
print(l1)
print(l2)


#---------------------------------------------------------------------------------------------------
import copy   # Import copy module to use deepcopy()

# Create a nested list (list inside a list)
l1 = [[1, 2], [3, 4]]

# Create a deep copy of l1
# deepcopy() creates a completely independent copy
l2 = copy.deepcopy(l1)

# Print original list
print(l1)    # Output: [[1, 2], [3, 4]]

# Print copied list
print(l2)    # Output: [[1, 2], [3, 4]]

# Check whether both variables refer to the same object
print(l1 is l2)   # Output: False (different memory locations)

# Append a new sublist to the original list
l1.append([5, 6])

# Modify an element inside the nested list
l1[0][1] = 344

# Print modified original list
print(l1)    # Output: [[1, 344], [3, 4], [5, 6]]

# Print copied list (remains unchanged)
print(l2)    # Output: [[1, 2], [3, 4]]


#---------------------------------------------------------------------------------------------------
# Create a list
lst = [1, 3, 4, 9, 1, 2]

# count() → counts how many times 2 appears in the list
c = lst.count(2)

# index() → returns the index position of value 9
index = lst.index(9)

# Print count of 2
print(c)          # Output: 1

# Print index of 9
print(index)      # Output: 3

# Uncommenting below line causes ValueError because 80 is not in list
# print(lst.index(80))

# index(value, start, end)
# Finds index of 1 between index 0 and 4 (4 excluded)
print(lst.index(1, 0, 4))   # Output: 0

# sorted() → returns a new list in descending order
lst1 = sorted(lst, reverse=True)

# clear() → removes all elements from the original list
lst.clear()

# Print cleared list (empty list)
print(lst)        # Output: []

# Print sorted list (descending)
print(lst1)       # Output: [9, 4, 3, 2, 1, 1]

# Sort lst1 again in ascending order
lst2 = sorted(lst1)

# Print sorted list (ascending)
print(lst2)       # Output: [1, 1, 2, 3, 4, 9]


#---------------------------------------------------------------------------------------------------
# Create a list
lst = [9, 4, 3, 2, 1, 1]

# sort() → sorts the list in ascending order (modifies original list)
lst.sort()
print(lst)        # Output: [1, 1, 2, 3, 4, 9]

# sort(reverse=True) → sorts the list in descending order
lst.sort(reverse=True)
print(lst)        # Output: [9, 4, 3, 2, 1, 1]


#---------------------------------------------------------------------------------------------------
# Create a list of strings
lst = ["devi", "sheela", "malli", "nandhu"]

# Print original list
print(lst)
# Output: ['devi', 'sheela', 'malli', 'nandhu']

# reversed() returns an iterator with elements in reverse order
# list() converts the iterator into a new list
lst_rev = list(reversed(lst))
print(lst_rev)
# Output: ['nandhu', 'malli', 'sheela', 'devi']

# reverse() reverses the list in place (modifies original list)
lst.reverse()
print(lst)
# Output: ['nandhu', 'malli', 'sheela', 'devi']


#---------------------------------------------------------------------------------------------------
# Program to take all integer values from the user (space separated)

# input()           → reads input as a string
# split()           → splits the string by spaces into a list of strings
# map(int, ...)     → converts each string into an integer
# list(...)         → converts the map object into a list

lst = list(map(int, input().split()))

# Print the list of integers
print(lst)


#---------------------------------------------------------------------------------------------------
# Program to find the sum of a sublist (subpart of the list)

# Take list input from the user in [] format
# Example input: [10, 20, 30, 40, 50]
lst = input("Enter a list between []\n")

# eval() converts the input string into a Python list
lst = eval(lst)

# Take starting index from the user
start = int(input("Enter the start index: "))

# Take ending index from the user
stop = int(input("Enter the stop index: "))

# lst[start:stop+1] → extracts sublist from start index to stop index
# sum() → calculates the sum of elements in the sublist
print("Sum =", sum(lst[start:stop + 1]))
