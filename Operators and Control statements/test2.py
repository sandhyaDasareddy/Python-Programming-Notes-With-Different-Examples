'''
Loops in Python
---------------

1. While Loop
-------------
Syntax:
    while (condition):
        # code inside loop

- The loop runs as long as the condition is True.
- You must update the loop variable inside the loop, otherwise it becomes an infinite loop.


2. For Loop
-----------
Used to iterate through sequences like list, tuple, string, range, etc.

Syntax:
    for variable in sequence:
        # body of the loop
'''

# Example of while loop (commented example)
'''
num = int(input("Enter a number: "))
i = 0

while i < num:
    print(i)
    i = i + 1     # update the loop variable
'''

# While loop example with a list
lst = [1, 2, 3, 4, 5]

print("using while loop")
i = 0
while i < len(lst):
    print(lst[i])
    i = i + 1     # increment index

print("using for loop")
for item in lst:
    print(item)


'''
Output:
using while loop
1
2
3
4
5
using for loop
1
2
3
4
5
'''