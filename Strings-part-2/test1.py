# List of programming languages
lst = ["python", "java", "c"]

# Empty string to store the combined result
s = ""

# Loop through each item in the list and concatenate to string s
for i in lst:
    s = s + i

# Print the final combined string
print(s)

# Another list of names
lst1 = ["sandhya", "devi", "priya"]

# Join all items in the list into a single string with no separator
str = "".join(lst1)

# Print the joined string
print(str)

'''
Output:
------
pythonjavac
sandhyadevipriya

'''