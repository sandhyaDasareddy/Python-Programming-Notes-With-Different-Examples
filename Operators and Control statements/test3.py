'''
Program: Demonstration of range(), for loop, list creation using range,
         and while loop example with balance deduction.

This file contains:
1. Basic use of range() in a for loop
2. Converting range() into lists
3. Using range() with step value
4. While loop example (balance deduction)
'''

# ---------------------------------------------------------
# 1. range() Example with for loop
# ---------------------------------------------------------
'''
In this example:
- We print "hello world"
- Then use a for loop with range(1, 501)
- This prints numbers from 1 to 500
'''

print("hello world")
# for i in range(1,501):
#     print(i)   # Uncomment to print 1 to 500


# ---------------------------------------------------------
# 2. Printing the range() object
# ---------------------------------------------------------
'''
range(5) generates numbers: 0,1,2,3,4
Printing range(5) directly shows a range object.
'''

print(range(5))



# ---------------------------------------------------------
# 3. Converting range() to list
# ---------------------------------------------------------
'''
list(range(2,11)) → creates a list from 2 to 10
'''

lst = list(range(2, 11))
print(lst)   # Output: [2,3,4,5,6,7,8,9,10]


'''
list(range(11)) → creates a list from 0 to 10
'''

lst1 = list(range(11))
print(lst1)  # Output: [0,1,2,3,4,5,6,7,8,9,10]


'''
list(range(0,11,2)) → creates even numbers from 0 to 10
step = 2, so it skips every two numbers
'''

lst2 = list(range(0, 11, 2))
print(lst2)  # Output: [0,2,4,6,8,10]



# ---------------------------------------------------------
# 4. While Loop Example: Bank Balance Deduction
# ---------------------------------------------------------
'''
This program:
- Starts with balance = 15500
- Minimum  balance allowed = 500
- Deducts 1000 each time while balance is greater than min_balance
- Stops when balance becomes 500
'''

balance = 15500
min_balance = 500
print("before balance", balance)

while (min_balance < balance):
    balance = balance - 1000

print("after balance", balance)  # Final balance = 500

'''
Output:
------
hello world
range(0, 5)
[2, 3, 4, 5, 6, 7, 8, 9, 10]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[0, 2, 4, 6, 8, 10]
before balance 15500
after balance 500

'''