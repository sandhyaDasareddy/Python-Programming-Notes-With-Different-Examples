'''
Lambda Functions with filter(), map(), and reduce()
---------------------------------------------------

In Python, lambda is used to create small one-line functions.

There are three important functions commonly used with lambda:

1. filter()  → Selects items based on a condition
2. map()     → Applies a function to each item
3. reduce()  → Reduces a sequence into a single value
               (requires functools module)
'''

from functools import reduce   # reduce() must be imported

# -----------------------------------------
# 1. filter() Function
# -----------------------------------------
'''
filter(function, sequence)

- Used to filter items from a list based on a condition.
- Returns only those elements for which the function returns True.
'''

lst = [23, 56, 98, 12, 10, 11, 9]

# Using lambda to filter odd numbers
odd_lst = list(filter(lambda x: x % 2 != 0, lst))
print("Odd numbers:", odd_lst)   # Output example: [23, 11, 9]


# -----------------------------------------
# 2. reduce() Function
# -----------------------------------------
'''
reduce(function, sequence)

- Used to apply a rolling computation.
- Reduces the list to a single value.
'''

lst1 = [1, 2, 3, 4, 5]

# Sum of all elements
res = reduce(lambda x, y: x + y, lst1)
print("Sum:", res)   # Output: 15

# Product of all elements
res1 = reduce(lambda x, y: x * y, lst1)
print("Product:", res1)   # Output: 120


'''
Output:
------
Odd numbers: [23, 11, 9]
Sum: 15
Product: 120

'''