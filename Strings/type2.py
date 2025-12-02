'''
String Slicing
--------------
Definition:
String slicing is used to access a part (substring) of a string.

Syntax:
-------
string_name[start : end : step]

Rules:
------
- start → starting index (included)
- end → ending index (excluded)
- step → jump value (default = 1)

Examples:
---------
s = "Guido van Rossum"

s[0:2]   → characters from index 0 to 1
s[2:]    → from index 2 to end
s[:9]    → from start to index 8
s[::]    → full string
s[0:9:3] → every 3rd character from index 0 to 8
s[::-1]  → reverse string
'''
# ---------------------------------------------------------

s = "Guido van Rossum"

# Print reverse string
print("Reverse string :", s[::-1])

# Print complete string using step 1
print("Normal string  :", s[::1])


'''
Output:
------
Reverse string : mussoR nav odiuG
Normal string  : Guido van Rossum

'''