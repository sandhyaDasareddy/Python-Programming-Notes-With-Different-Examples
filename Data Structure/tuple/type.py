# Tuples – Immutable Data Type
# ---------------------------

'''
Problem Statement:
------------------
Write a Python program to demonstrate that tuples are immutable
and do not support modification operations like append().

Input:
------
A predefined tuple of integers.

Output:
-------
Print the tuple and its type.
Demonstrate how to create a single-element tuple.

Explanation:
------------
- Tuples are immutable (cannot be modified after creation)
- Tuples do not support append(), remove(), insert(), etc.
- A single-element tuple must end with a comma (,)
'''

# Program Code

# Normal tuple
t = (10, 20, 30, 40)
print(t)
print(type(t))

# Single-element tuple
t1 = (10,)
print(t1)
print(type(t1))

# ❌ Not allowed (tuple is immutable)
# t.append(50)
# t[0] = 100
#-------------------------------------------------------------------------------------------------------------


# Tuple with Nested and Heterogeneous Elements (All-in-One Program)
# ---------------------------------------------------------------

'''
Concepts Covered:
-----------------
1. Tuple is an immutable data type
2. Tuple can contain heterogeneous elements
3. Tuple can contain mutable objects (like list)
4. Mutable objects inside a tuple CAN be modified
5. Tuple elements themselves CANNOT be reassigned

Important Note:
---------------
- Tuple is immutable
- List inside tuple is mutable
'''

# Creating a tuple with int, list, and tuple
tup = (0, [1, 2], (3, 4))

print("Original Tuple:", tup)

# -------------------------
# Accessing tuple elements
# -------------------------
print("tup[0] =", tup[0])        # int
print("tup[1][0] =", tup[1][0])  # list element
print("tup[1][1] =", tup[1][1])
print("tup[2][0] =", tup[2][0])  # nested tuple
print("tup[2][1] =", tup[2][1])

# -------------------------------------------------
# Allowed operations (list inside tuple is mutable)
# -------------------------------------------------
tup[1].append(3)        # add element
tup[1].insert(1, 8)     # insert element
tup[1][0] = "hello"     # update element
tup[1].remove(8)        # remove specific element

print("After append, insert, update, remove:", tup)

tup[1].pop()            # remove last element
print("After pop():", tup)

tup[1].pop(1)           # remove element at index 1
print("After pop(1):", tup)

# -------------------------------------------------
# NOT ALLOWED operations (tuple is immutable)
# -------------------------------------------------
# tup[1] = 30           # ❌ TypeError
# tup[0] = 100          # ❌ TypeError
# tup.append(50)        # ❌ AttributeError

print("Final Tuple:", tup)
#-------------------------------------------------------------------------------------------------------------


# Tuple Traversal Techniques
# --------------------------

'''
Problem Statement:
------------------
Write a Python program to demonstrate different ways
to traverse elements of a tuple.

Concepts Covered:
-----------------
1. Tuple creation
2. Tuple with strings
3. Traversing tuple using:
   - for-each loop
   - index-based loop
   - skipping elements
   - reverse traversal
'''

# Tuple of integers
t = (10, 20, 30, 40, 50)

# Tuple of strings (parentheses optional)
t1 = "hello", "ok", "oh gandhi tatha"
print("Tuple t1:", t1)

print("\nTraversal using for-each loop:")
for i in t:
    print(i)

print("\nTraversal using index (from index 1 to end):")
for i in range(1, len(t)):
    print(t[i], end=" ")
print()

print("\nTraversal using index (same as above, repeated):")
for i in range(1, len(t)):
    print(t[i], end=" ")
print()

print("\nTraversal by skipping alternate elements (step = 2):")
for i in range(0, len(t), 2):
    print(t[i], end=" ")
print()

print("\nReverse traversal of tuple:")
for i in range(len(t) - 1, -1, -1):
    print(t[i], end=" ")
