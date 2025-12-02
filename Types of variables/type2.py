'''
Python Program to Find Factorial (Two Methods)
1. Using Recursion

Recursion → A function calling itself repeatedly until a stopping condition is reached.
'''
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
res = factorial(num)
print("factorial of", num, "is", res)

#2. Using Loop (Iterative Method)
fact = 1
for i in range(1, num + 1):
    fact *= i
print("factorial of", num, "is", fact)

'''
Output:
------
Enter a number: 4
factorial of 4 is 24
factorial of 4 is 24
'''