'''
String Formatting in Python

There are two common ways to format strings:

1. Using format() method
2. Using string literals (f-strings)

Why do we need string formatting?
---------------------------------
String formatting allows us to insert variables into a sentence or message
in a clean and readable way, instead of using multiple + operators.
It helps write dynamic text that includes user input or variable values.
'''

# Taking user input
name = input("Enter your name: ")
place = input("Enter your city: ")

# Using format() method
message = "Hello {}, how is the weather in {}?".format(name, place)

# Printing the formatted string
print(message)


'''
Output:
------
Enter your name: sandhya
Enter your city: mydukur
Hello sandhya, how is the weather in mydukur?

'''