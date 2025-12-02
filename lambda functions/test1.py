'''
Lambda Functions in Python
--------------------------
A lambda function is a small anonymous (nameless) function.

Syntax:
    lambda arguments : expression
'''

from math import factorial

# ---------------------------------------------------
# 1. Lambda for power (x^y) — takes input from user
# ---------------------------------------------------
a = int(input("Enter base number (a): "))
b = int(input("Enter exponent number (b): "))

power_result = (lambda x, y: x ** y)(a, b)
print("Result of", a, "raised to the power", b, "is:", power_result)


# ---------------------------------------------------
# 2. Lambda for division — takes input from user
# ---------------------------------------------------
num = int(input("\nEnter numerator: "))
den = int(input("Enter denominator: "))

division_result = (lambda x, y: x / y)(num, den)
print("Quotient of", num, "/", den, "is:", division_result)


# ---------------------------------------------------
# 3. Lambda for addition — takes input from user
# ---------------------------------------------------
x = int(input("\nEnter first number to add: "))
y = int(input("Enter second number to add: "))

add = lambda a, b: a + b
print("Addition of", x, "and", y, "is:", add(x, y))


# ---------------------------------------------------
# 4. Lambda for factorial — takes input from user
# ---------------------------------------------------
n = int(input("\nEnter a number to find factorial: "))

fact = lambda k: factorial(k)
print("Factorial of", n, "is:", fact(n))


'''
Output:
------
Enter base number (a): 5
Enter exponent number (b): 2
Result of 5 raised to the power 2 is: 25

Enter numerator: 4
Enter denominator: 2
Quotient of 4 / 2 is: 2.0

Enter first number to add: 4
Enter second number to add: 6
Addition of 4 and 6 is: 10

Enter a number to find factorial: 5
Factorial of 5 is: 120

'''