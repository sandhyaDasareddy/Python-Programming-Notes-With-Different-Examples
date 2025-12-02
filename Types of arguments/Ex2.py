# 3. DEFAULT ARGUMENTS (OPTIONAL ARGUMENTS)
# -----------------------------------------
# A parameter with a default value becomes OPTIONAL.
# If no value is passed, the default value is used.

def greet(name="Guest"):
    print("Default Argument Output:", "Hello", name)

greet("Rahul")    # name = Rahul
greet()           # name takes default value "Guest"


# Another example
def fun(a, c, b=1):
    # 'b' is optional because it has a default value
    print("Default Argument Example Output:", a, b)

fun(10, 20)       # b uses default value → 1


# 4. VARIABLE-LENGTH ARGUMENTS (*args)
# ------------------------------------
# *args allows you to pass ANY number of positional values.
# It stores values in a TUPLE.

def add_all(*args):
    print("Variable-Length (*args) Received:", args)
    total = sum(args)
    print("Sum:", total)

add_all(1, 2, 3)
add_all(10, 20, 30, 40, 50)


# 5. VARIABLE-LENGTH KEYWORD ARGUMENTS (**kwargs)
# -----------------------------------------------
# **kwargs allows ANY number of keyword arguments.
# It stores data in a DICTIONARY.

def show_details(**kwargs):
    print("Variable-Length Keyword Arguments (**kwargs):", kwargs)

show_details(name="Python", version=3.11)
show_details(id=101, grade="A", passed=True)


'''
Output:
------
Default Argument Output: Hello Rahul
Default Argument Output: Hello Guest
Default Argument Example Output: 10 1
Variable-Length (*args) Received: (1, 2, 3)
Sum: 6
Variable-Length (*args) Received: (10, 20, 30, 40, 50)
Sum: 150
Variable-Length Keyword Arguments (**kwargs): {'name': 'Python', 'version': 3.11}
Variable-Length Keyword Arguments (**kwargs): {'id': 101, 'grade': 'A', 'passed': True}'''


