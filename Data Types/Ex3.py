'''
Tuple:
------
- Tuple is immutable in Python.
- We cannot modify a tuple (no adding, removing, or updating elements).
- Indexing is available (both +ve and -ve).
- Duplicates are allowed in tuples.
'''

t = (1, "python", 3, 7.0, True)

print(t)          # Print entire tuple
print(type(t))    # Type of tuple
print(len(t))     # Length of tuple

print(t[0])       # Access first element
print(t[1])       # Access second element
print(t[-1])      # Access last element using negative index

# The following lines will cause errors because tuple is immutable:
# t.remove(1)      # ❌ Error: tuple has no remove()
# t[0] = 2         # ❌ Error: tuple does not support item assignment

print("Tuples cannot be modified! They are immutable.")

'''
Output:-
------
98.87
56
<class 'list'>
['kk', 'hello', 56, 98.87, True, 'kk']
6
['kk', 'hello', 56, 98.87, True, 'kk', 6]
['kk', 56, 98.87, True, 'kk', 6]
['kk', 56, 23, True, 'kk', 6]
'''