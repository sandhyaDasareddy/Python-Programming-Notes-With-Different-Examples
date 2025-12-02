x = 10
y = 20
z = 30

print(x, y, z)                    # Prints values with default separator (space)
print(x, y, z, sep='*')           # Prints values separated by '*'
print(x, y, z, sep='=', end="??") # Separator '=' and custom end string "??"

'''
Output:
------
10 20 30
10*20*30
10=20=30??
'''