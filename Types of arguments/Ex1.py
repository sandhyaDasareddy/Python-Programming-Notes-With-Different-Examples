'''
Types of Arguments in Python
----------------------------
1. Positional Arguments
2. Keyword Arguments
3. Default Arguments (Optional Arguments)
4. Variable-Length Arguments (*args)
5. Variable-Length Keyword Arguments (**kwargs)
'''

# 1. POSITONAL ARGUMENTS
# ----------------------
# In positional arguments, values are passed IN ORDER.
# The position of each argument decides which parameter it goes to.

def power_of(a, b):
    print("Positional Arguments Output:", a ** b)

power_of(2, 5)    # a = 2, b = 5
power_of(5, 2)    # a = 5, b = 2


# 2. KEYWORD ARGUMENTS
# --------------------
# Arguments are passed using PARAMETER NAMES.
# Order does NOT matter because names are used.

def student_info(name, age):
    print("Keyword Arguments Output:", name, age)

student_info(name="John", age=20)         # keyword arguments
student_info(age=25, name="Alice")        # order changed but works


'''
Output:
------
Positional Arguments Output: 32
Positional Arguments Output: 25
Keyword Arguments Output: John 20
Keyword Arguments Output: Alice 25

'''