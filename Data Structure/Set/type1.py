# Set – Unordered Collection Using Hashing
# ----------------------------------------

'''
Problem Statement:
------------------
Write a Python program to demonstrate the properties of sets:
1. Unordered collection
2. Duplicate elements are not allowed
3. Set elements must be immutable (hashable)

Explanation:
------------
- Sets internally use hashing
- Duplicate elements are automatically removed
- Mutable objects like list cannot be stored in a set
'''

# Program Code

# Duplicate elements are automatically removed
s = {10, 20, 40, 50, 40}
print("Set s:", s)
print("Type of s:", type(s))

# ❌ NOT ALLOWED: list inside set (mutable)
# s1 = {1, 2, 3, [12]}   # TypeError

# ✅ ALLOWED: tuple inside set (immutable)
s2 = {1, 2, 3, (12,)}
print("Set s2:", s2)
print("Type of s2:", type(s2))
#-------------------------------------------------------------------------------------------------


# Set Operations in Python
# -----------------------

'''
Problem Statement:
------------------
Write a Python program to demonstrate various operations
that can be performed on a set.

Concepts Covered:
-----------------
1. Sets are unordered collections
2. Duplicate elements are not allowed
3. Set elements must be immutable (hashable)
4. Demonstrates the following methods:
   - add()
   - remove()
   - pop()
   - discard()
   - update()
'''

# Program Code

# Creating a set
s = {5, 7, 55, 67, 88, 98}
print("Original set:", s)

# add() → adds a single element to the set
s.add(999)
print("After add(999):", s)

# remove() → removes specified element (raises error if not present)
s.remove(5)
print("After remove(5):", s)

# pop() → removes a random element (no argument allowed)
s.pop()
print("After pop():", s)

# pop() does not accept any argument
# s.pop(999)   # ❌ TypeError

print("Set after pop():", s)

# remove() raises KeyError if element not found
# s.remove(3232)   # ❌ KeyError

# discard() → removes element safely (no error if element not present)
s.discard(433)
print("After discard(433):", s)

# update() with a set → adds multiple elements
s.update({1, 2, 3, 4, 5})
print("After update({1,2,3,4,5}):", s)

# update() with a list → adds multiple elements
s.update([10, 20, 30, 40, 50])
print("After update([10,20,30,40,50]):", s)
#--------------------------------------------------------------------------------------------------



# Set Operations in Python
# -----------------------

'''
Problem Statement:
------------------
Write a Python program to demonstrate basic set operations
such as union and intersection.

Concepts Covered:
-----------------
1. Sets are unordered collections
2. Duplicate elements are not allowed
3. Set operations:
   - Union (|, union())
   - Intersection (&, intersection())
'''

# Program Code

s1 = {1, 2, 3, 4, 5, 6, 7, 8}
s2 = {5, 6, 7, 8, 9, 10, 71, 12, 13, 14}

print("Set s1:", s1)
print("Set s2:", s2)

# ----------------
# Union operation
# ----------------
# Using | operator
s3 = s1 | s2
print("Union using | :", s3)

# Using union() method
s4 = s1.union(s2)
print("Union using union():", s4)

# -----------------------
# Intersection operation
# -----------------------
# Using & operator
s5 = s1 & s2
print("Intersection using & :", s5)

# Using intersection() method
s6 = s1.intersection(s2)
print("Intersection using intersection():", s6)

# ------------------
# Difference operation
# ------------------
s7 = s1 - s2
print("Difference using - :", s7)

s8 = s1.difference(s2)
print("Difference using difference():", s8)
#--------------------------------------------------------------------------------------------------



# Symmetric Difference in Sets
# ----------------------------

'''
Problem Statement:
------------------
Write a Python program to demonstrate symmetric difference
operation on two sets.

Definitions:
------------
- Symmetric difference returns elements that are present
  in either of the sets but NOT in both.
- intersection_update() updates the set with common elements only.
- symmetric_difference_update() updates the set with non-common elements.
'''

# Program Code
s1 = {1, 2, 3, 4, 5, 6, 7, 8}
s2 = {1, 2, 3, 6, 7, 10, 12, 13}

print("Set s1:", s1)
print("Set s2:", s2)

# -----------------------------
# Symmetric Difference
# -----------------------------
s3 = s1 ^ s2
print("Symmetric difference using ^ :", s3)

s4 = s1.symmetric_difference(s2)
print("Symmetric difference using method:", s4)

# -----------------------------
# Intersection Update
# -----------------------------
s1.intersection_update(s2)
print("s1 after intersection_update:", s1)

# -----------------------------
# Symmetric Difference Update
# -----------------------------
s1.symmetric_difference_update(s2)
print("s1 after symmetric_difference_update:", s1)
#--------------------------------------------------------------------------------------------------



# Set Functions in Python
# ----------------------

'''
Problem Statement:
------------------
Write a Python program to demonstrate set relationship
functions such as subset, superset, and disjoint sets.

Concepts Covered:
-----------------
1. Subset        (<=, issubset())
2. Superset      (>=, issuperset())
3. Disjoint sets (isdisjoint())
'''

# Program Code

s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13}
s2 = {3, 11, 4, 7}

# ----------------
# Subset check
# ----------------
print(s2 <= s1)                 # Using operator
print(s2.issubset(s1))          # Using method

# ----------------
# Superset check
# ----------------
print(s1 >= s2)                 # Using operator
print(s1.issuperset(s2))        # Using method

# ----------------
# Disjoint check
# ----------------
s3 = {90, 70, 80}
print(s1.isdisjoint(s3))


