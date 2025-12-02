# Map Function in Python
# ----------------------
# The map() function applies a given function to every element in a sequence.
# Syntax:
#     map(function, iterable)
# It returns a map object, which we convert to a list using list().


# Example list
lst = [1, 2, 3, 4, 5]

'''
Example 1: Using normal function with map()
-------------------------------------------

def fun(x):
    return x**2

sq_list = list(map(fun, lst))
print(sq_list)

Example 2: Using lambda with map()
----------------------------------
sq_lst = list(map(lambda x: x**2, lst))
print(sq_lst)
'''


# Example 3: Lambda returning another lambda (Nested Lambda)
# ---------------------------------------------------------
# fun1(num) → returns another lambda
# The returned lambda takes x and performs x * num

def fun1(num):
    return lambda x: x * num


# Take input from user
num = int(input("Enter a number (multiplier): "))

# Generate the inner lambda function
fun2 = fun1(num)

# Call fun2 with value 2
res = fun2(2)

# Final output
print("Result of multiplying", num, "with 2 is:", res)

'''
Output:
------
Enter a number (multiplier): 2
Result of multiplying 2 with 2 is: 4


'''