# how to take input from the user

'''
Two ways to take input in Python:

1. During program execution  → using input(prompt)
2. Before program execution → using command line arguments (sys.argv)
'''

'''
# Example 1: Taking two numbers from the user
print("enter first number")
num1 = int(input())        # input is always string → convert into int

print("enter second number")
num2 = int(input())

res = num1 + num2
print(res)                  # prints sum


# Example 2: Taking input with prompt
a = int(input("Enter a numerator: "))
b = int(input("Enter a denominator: "))
c = a + b
print(c)
'''

# Example 3: Taking a full mathematical expression using eval()
exp = input("enter an expression\n")   # e.g., 10 + 20 * 3
res = eval(exp)                        # evaluates the expression
print(res)
