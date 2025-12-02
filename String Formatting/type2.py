'''
String Formatting:

Syntax:
string.format(*args)
'''

from math import *

# Right-align the number 999 in a width of 10 spaces
s = "{0:>10}".format(999)
print(s)  # Output: "       999"

# Left-align the number, fill remaining space with '+' symbols, width = 10
s1 = "{0:+<10}".format(999)
print(s1)  # Output: "999+++++++"

# Center-align the number, fill extra space with '+', width = 10
s = "{0:+^10}".format(999)
print(s)  # Output: "+++999++++"

# Format pi to 4 decimal places with width 10, padded with zeros
print("{0:010.4f}".format(pi))
# Output: "00003.1416"

# Scientific notation with 3 decimal places
ew = 57965000000000000000000000000
s = "{0:.3e}".format(ew)
print(s)  # Output: "5.797e+28"

# Simple formatting using positional arguments
a = "{} {} {}".format(1, 2, 3)
print(a)  # Output: "1 2 3"

'''
Output:
-------
       999
999+++++++
+++999++++
00003.1416
5.796e+28
1 2 3
'''
