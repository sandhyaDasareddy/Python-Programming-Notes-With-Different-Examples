'''
Check Even or Odd
-----------------
num = int(input("enter number: "))
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

Comparison Operators:
---------------------
==  equal to
!=  not equal to
>   greater than
<   less than
>=  greater than or equal to
<=  less than or equal to

Logical Operators:
------------------
and   → both conditions must be true
or    → at least one condition must be true
not   → reverses the condition (True → False, False → True)
'''

# ------------------------------
# AND Operator: find greatest of 3 numbers
# ------------------------------

a = int(input("enter first number : "))
b = int(input("enter second number : "))
c = int(input("enter third number : "))

if (a > b and a > c):
    print(a, "is greater")
elif (b > c):
    print(b, "is greater")
else:
    print(c, "is greater")


# ------------------------------
# OR Operator: divisible by 3 or 5
# ------------------------------
num = int(input("Enter a number: "))
if num % 3 == 0 or num % 5 == 0:
    print(num, "is divisible by either 3 or 5")
else:
    print(num, "is not divisible by either 3 or 5")


# ------------------------------
# NOT Operator: reverse the OR condition
# ------------------------------
num = int(input("Enter a number: "))
if not (num % 3 == 0 or num % 5 == 0):
    print(num, "is NOT divisible by 3 or 5")
else:
    print(num, "IS divisible by 3 or 5")


# ------------------------------
# Truthy and Falsy Values in Python
# ------------------------------

# Any non-zero number → True
if 8:
    print("8 is true")
else:
    print("8 is false")

# Empty list → False
if []:
    print("[] is true")
else:
    print("[] is false")

# Empty dictionary → False
if {}:
    print("{} is true")
else:
    print("{} is false")

# Empty tuple → False
if ():
    print("() is true")
else:
    print("() is false")

# None → False
if None:
    print("None is true")
else:
    print("None is false")


'''
Output:
------
enter first number : 15
enter second number : 14
enter third number : 85
85 is greater
Enter a number: 54
54 is divisible by either 3 or 5
Enter a number: 35
35 IS divisible by 3 or 5
8 is true
[] is false
{} is false
() is false
None is false
'''