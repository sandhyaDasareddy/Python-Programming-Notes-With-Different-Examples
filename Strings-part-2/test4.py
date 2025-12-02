'''
# Given string
s = "STAY HOME stay safe"

# Empty string to store the converted result
s1 = ""

# Toggle each character's case manually using ASCII values
for i in s:
    res = ord(i)  # Get ASCII value of character

    # Check if character is uppercase (A–Z)
    if 65 <= res <= 90:
        ch = chr(res + 32)  # Convert to lowercase
        s1 += ch

    # Check if character is lowercase (a–z)
    elif 97 <= res <= 122:
        ch = chr(res - 32)  # Convert to uppercase
        s1 += ch

    # Keep spaces or special characters unchanged
    else:
        s1 += i

# Print original and toggled string
print(s)
print(s1)

------------------or----------------------------

# Word-by-word toggle using split()
lst = s.split()   # Split string into words
print(lst)

lst1 = []         # List to store converted words

for word in lst:
    if word.isupper():          # If entire word is uppercase
        lst1.append(word.lower())
    else:                        # Otherwise convert to uppercase
        lst1.append(word.upper())

print(lst1)
'''

# Using built-in string functions for case conversion
s = "STAY HOME stay safe"

# swapcase(): converts uppercase to lowercase and vice versa
s1 = s.swapcase()
print(s)
print(s1)

# title(): converts each word to Title Case (first letter uppercase, rest lowercase)
s2 = s1.title()
print(s2)

# capitalize(): only first character uppercase, rest lowercase
print("python".capitalize())
