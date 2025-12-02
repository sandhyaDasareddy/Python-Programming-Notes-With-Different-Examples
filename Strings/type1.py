'''
Strings in Python
-----------------
A string is a sequence of characters.
You can create a string using:
1. Single quotes
2. Double quotes
3. Triple quotes (for multiline strings)
'''

# -----------------------
# 1. STRING CREATION
# -----------------------
s1 = " "               # an empty space string
print("s1 =", s1)

s2 = "p"
print("s2 =", s2)

s3 = "python"
print("s3 =", s3)

# Multiline string using triple quotes
s4 = """c
java
python"""
print("s4 =", s4)

# Converting a number into a string
s5 = str(99.9)
print("s5 =", s5)
print("Type of s5 =", type(s5))



# -----------------------
# 2. ACCESSING CHARACTERS
# -----------------------
s = "python"
print("\nString =", s)
print("Character at index 1 =", s[1])      # 'y'

print("Characters in string:")
for ch in s:
    print(ch)



# -----------------------
# 3. STRING IMMUTABILITY + MEMORY IDs
# -------------------------------------
# Strings are immutable → cannot change characters directly
# Python sometimes reuses memory for identical strings
# id() helps to see memory address
# -------------------------------------
s1 = "hello"
print("\ns1 =", s1)
print("Memory ID of s1 =", id(s1))

s2 = "world"
print("s2 =", s2)
print("Memory ID of s2 =", id(s2))



# -----------------------
# 4. STRING CONCATENATION
# -----------------------
res = s1 + " " + s2     # creates a NEW string
s3 = "hello world"

print("\ns3 =", s3)
print("res =", res)

print("Memory ID of res =", id(res))
print("Memory ID of s3  =", id(s3))



# -----------------------
# 5. MEMORY IDs OF CHARACTERS
# -----------------------
print("\nID of s1[4] =", id(s1[4]))    # 'o' from "hello"
print("ID of s2[1] =", id(s2[1]))      # 'o' from "world"



# -----------------------
# 6. STRING INTERNING (same value = same memory)
# -----------------------
s1 = "p"
s2 = "p"
print("\nID of s1 =", id(s1))
print("ID of s2 =", id(s2))            # SAME memory → interning



# -----------------------
# 7. MEMORY IDs INSIDE ANOTHER STRING
# -----------------------
print("\nID of res[1] =", id(res[1]))
print("ID of s3[1]  =", id(s3[1]))



# -----------------------
# 8. MEMORY IDs OF REPEATED CHARACTERS
# -------------------------------------
# Here both a[2] and a[3] are 'l'
# Python may reuse memory for same characters
# -------------------------------------
a = "hello"
print("\nID of a[2] =", id(a[2]))      # 'l'
print("ID of a[3] =", id(a[3]))        # 'l'


'''
Output:
-------
s1 =  
s2 = p
s3 = python
s4 = c
java
python
s5 = 99.9
Type of s5 = <class 'str'>

String = python
Character at index 1 = y
Characters in string:
p
y
t
h
o
n

s1 = hello
Memory ID of s1 = 2343915674080
s2 = world
Memory ID of s2 = 2343915674560

s3 = hello world
res = hello world
Memory ID of res = 2343915748912
Memory ID of s3  = 2343915739504

ID of s1[4] = 140717886349536
ID of s2[1] = 140717886349536

ID of s1 = 140717886349584
ID of s2 = 140717886349584

ID of res[1] = 140717886349056
ID of s3[1]  = 140717886349056

ID of a[2] = 140717886349392
ID of a[3] = 140717886349392

'''