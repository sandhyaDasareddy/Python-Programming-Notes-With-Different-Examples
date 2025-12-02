'''
Types of Variables in Python
----------------------------

1. Local Variable:
   - Created inside a function.
   - Can be used only inside that function.
   - Scope → limited to the function.

2. Global Variable:
   - Created outside any function.
   - Can be accessed anywhere in the program.
   - Scope → entire file.

Using the 'global' Keyword:
---------------------------
- If a function wants to MODIFY a global variable,
  we must use the 'global' keyword inside the function.
'''

# ------ Global Variables ------
x = 99
y = 98
z = 90


def fun():
    # ------ Modify a Global Variable ------
    global y        # Now this 'y' refers to the global y, not local
    y = 999         # Updating global variable y
    a = 10
    # Accessing global variables
    print("Value of global variable x =", x)
    print("Updated global variable y =", y)

    # locals() → variables inside the function
    print("\nLocal variables inside fun():")
    print(locals())

    # globals() → all global variables in the program
    print("\nGlobal variables in the program:")
    print(globals())


# Calling the function
fun()

# Printing updated global variable outside function
print("\nValue of y outside function =", y)


'''
Output:
------
Value of global variable x = 99
Updated global variable y = 999

Local variables inside fun():
{'a': 10}

Global variables in the program:
{'__name__': '__main__', '__doc__': "\nTypes of Variables in Python\n----------------------------\n\n1. Local Variable:\n   - Created inside a function.\n   - Can be used only inside that function.\n   - Scope → limited to the function.\n\n2. Global Variable:\n   - Created outside any function.\n   - Can be accessed anywhere in the program.\n   - Scope → entire file.\n\nUsing the 'global' Keyword:\n---------------------------\n- If a function wants to MODIFY a global variable,\n  we must use the 'global' keyword inside the function.\n", '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002252D72BC80>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:\\Users\\sandhya\\OneDrive\\Desktop\\CRT\\Python_Programming\\Types of variables\\type1.py', '__cached__': None, 'x': 99, 'y': 999, 'z': 90, 'fun': <function fun at 0x000002252D71A2A0>}

Value of y outside function = 999
'''