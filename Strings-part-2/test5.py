'''
String translation example using maketrans() and translate()
'''

# Original string
s = "Error 404 page not found"

# Create a translation table:
# 1. Convert vowels a,e,i,o,u → uppercase A,E,I,O,U
# 2. Remove digits 0–9 from the string
table = s.maketrans("aeiou", "AEIOU", "0123456789")

# Apply translation using the created table
s_table = s.translate(table)

# Print original and translated string
print(s)        # Original string
print(s_table)  # Translated output

'''
Output:
------
Error 404 page not found
ErrOr  pAgE nOt fOUnd

'''