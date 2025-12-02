'''
DRY Principle (Do Not Repeat Yourself)
--------------------------------------
The DRY principle means: Avoid repeating the same code again and again. 
Instead, use functions to reuse logic.

Benefits of DRY
---------------
1. Reusability – write once, use multiple times  
2. Modularity – break code into smaller logical parts

Types of Functions in Python
-----------------------------
1. User-defined functions (Created by the programmer)
2. Built-in functions (Already available in Python, e.g., print(), len(), sum())
3. Lambda functions (Anonymous single-line functions created using lambda keyword)
4. Recursive functions (A function that calls itself)

Syntax of a Function
--------------------
def nameOfFunction(parameters):
    # body
    return value

Types of User-Defined Functions
-------------------------------
1. No Input and No Return Value
   def greet():
       print("Hello Python!")

2. No Input but Return Value
   def getNumber():
       return 100

3. Take Input but No Return Value
   def showSquare(num):
       print(num * num)

4. Take Input and Return Value
   def findSum(a, b):
       return a + b
'''

#1. No Input and No Return Value

def mul():
    a = 10
    b = 20
    c = a * b
    print("Multiplication result:", c)

mul()

'''
Output:
------
Multiplication result: 200
'''
