'''
String Operations in Python
---------------------------
1. Concatenation (+)
2. Repetition (*)

Questions to Students:
----------------------
1. What is string concatenation?
2. What happens when you use + with strings?
3. How do you convert lowercase letters to uppercase manually?
4. What does ord() and chr() do?
5. What is the difference between .upper() and .lower()?
'''

# -------------------------------
# 1. String Concatenation Example
# -------------------------------

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Question: What will happen if you add two strings using '+' ?
s1 = s1 + " " + "midhuna"    # adding a word to the string
print("After concatenation:", s1)


# ---------------------------------------------------------
# 2. Convert a single lowercase character to uppercase
# ---------------------------------------------------------

c = input("Enter a character: ")
a = ord(c)    # ord() gives ASCII value

# Question: What is the ASCII range of lowercase letters?
if 97 <= a <= 122:     # ASCII range for 'a' to 'z'
    print("Uppercase:", chr(a - 32))
else:
    print("Not a lowercase letter")


# ---------------------------------------------------------
# 3. Convert full string to uppercase manually (no .upper())
# ---------------------------------------------------------

s = input("Enter a string: ")
s_upper = ""

# Question: Why are we looping through each character?
for c in s:
    a = ord(c)
    if 97 <= a <= 122:       # lowercase
        s_upper += chr(a - 32)
    else:
        s_upper += c

print("Original string :", s)
print("Converted string:", s_upper)


# ---------------------------------------------------------
# 4. Using Built-in string methods: upper() and lower()
# ---------------------------------------------------------

text = input("Enter any string: ")

upper_str = text.upper()   # converts to uppercase
lower_str = text.lower()   # converts to lowercase

print("Original :", text)
print("Uppercase:", upper_str)
print("Lowercase:", lower_str)

# Question: Is 'Hello' equal to 'hello' if both are converted to uppercase?
if upper_str.upper() == lower_str.upper():
    print("Both are equal after conversion")
else:
    print("Not equal")

'''
Output:
------
Enter first string: Sandhya
Enter second string: devi
After concatenation: Sandhya midhuna
Enter a character: R
Not a lowercase letter
Enter a string: Priya
Original string : Priya
Converted string: PRIYA
Enter any string: Dinesh
Original : Dinesh
Uppercase: DINESH
Lowercase: dinesh
Both are equal after conversion
'''