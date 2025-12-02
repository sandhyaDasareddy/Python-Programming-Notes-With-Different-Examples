import math

# help(math)              # shows full documentation of math module
# print(dir(math))        # shows all functions and constants inside math module


# Example: factorial()
# a = math.factorial(5)
# print(a)


# Example: ceil()
# help(math.ceil)
# a = math.ceil(-1.2)
# print(a)


# Example: floor()
# help(math.floor)
# b = math.floor(1.7)
# print(b)


# ------------------------------------------
# Function Example (Docstring Fixed)
# ------------------------------------------


def power_of(a, b):
    '''
    This function returns the power of two numbers.
    It calculates a raised to the power b.
    '''
    c = a ** b
    print(c)

if __name__ == '__main__':
    power_of(4, 2)


# ------------------------------------------
# Function to get quotient
# ------------------------------------------

def get_quotient(a, b):
    '''
    This function prints the quotient of two numbers.
    It performs integer division using a // b.
    '''
    quotient = a // b
    print(quotient)
'''
Output:
-------
16
'''