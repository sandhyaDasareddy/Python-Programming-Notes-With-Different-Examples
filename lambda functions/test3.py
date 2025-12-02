# Program: Multiplication Table using Lambda Function
# ---------------------------------------------------
# Step 1: Take a number from the user
num = int(input("Enter a number: "))

# Step 2: Define a function that returns a lambda
# fun(num) → returns lambda x: x * num
# The lambda will multiply any given x with the number 'num'
def fun(num):
    return lambda x: x * num

# Step 3: math_table becomes a lambda function
math_table = fun(num)

# Step 4: Print multiplication table using a loop
for i in range(1, 11):
    print(num, " x ", i, " = ", math_table(i))


'''
Output:-
-------
Enter a number: 5
5  x  1  =  5
5  x  2  =  10
5  x  3  =  15
5  x  4  =  20
5  x  5  =  25
5  x  6  =  30
5  x  7  =  35
5  x  8  =  40
5  x  9  =  45
5  x  10  =  50

'''