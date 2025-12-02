'''
Advanced Data Types:
--------------------
1. List
2. Tuple
3. Set
4. Dict

1. List:
- Used to store multiple values of different data types.
- List is mutable (changeable).
- Mutable means we can add, remove, or modify elements.
- List is an ordered data type.
- Both +ve and -ve indexes are available.
'''

# Creating a list with mixed data types
lst = ["kk", "hello", 56, 98.87, True, "kk"]

print(lst[-3])     # Negative index -> third element from the end
print(lst[2])      # Positive index -> third element from the beginning

print(type(lst))   # Shows that lst is of type 'list'
print(lst)         # Print full list
print(len(lst))    # Length of the list

lst.append(6)       # Add new value at the end
print(lst)

lst.remove("hello") # Remove first occurrence of "hello"
print(lst)

lst[2] = 23         # Modify element at index 2
print(lst)


'''
Output:-
-------
98.87
56
<class 'list'>
['kk', 'hello', 56, 98.87, True, 'kk']
6
['kk', 'hello', 56, 98.87, True, 'kk', 6]
['kk', 56, 98.87, True, 'kk', 6]
['kk', 56, 23, True, 'kk', 6]
'''