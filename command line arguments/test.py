from sys import argv
print(argv[1])

'''
How to Run This Program
-----------------------

1. Save this file as: test3.py

2. Run the program from command line by passing one argument:

   Example 1:
   -----------
   python test3.py hello
   Output:
   hello

   Example 2:
   -----------
   python test3.py 123
   Output:
   123

Note:
- argv[0] → name of the file (test3.py)
- argv[1] → first argument given by the user
- If you don't pass any argument, program will give:
  IndexError: list index out of range
'''
