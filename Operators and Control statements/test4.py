'''
Break Statement in Python
-------------------------
- The 'break' statement is used to exit a loop immediately.
- When Python encounters 'break', the loop stops even if the loop condition is still True.

Example Program:
Check whether a number is prime or not using 'break'
----------------------------------------------------
Logic:
1. Input a number 'n'
2. Assume the number is prime (status = True)
3. Use a for loop from 2 to n-1
4. If any number divides n, then n is NOT prime
      → Set status = False
      → Use break to stop checking further
5. After loop ends, print result using status


Continue Statement in Python
----------------------------
- The 'continue' statement skips the current iteration of the loop.
- When Python encounters 'continue':
      → It does NOT execute the remaining statements inside the loop
      → Moves to the next iteration directly

Example Program:
Find the sum of even and odd numbers separately using 'continue'
----------------------------------------------------------------
Logic:
1. Take a number 'n'
2. Loop from 1 to n
3. If a number is even → add to even_sum and continue (skip odd_sum part)
4. If it is not even → add to odd_sum
5. Print both sums
'''


# -------- PRIME NUMBER CHECK USING BREAK --------
n = int(input("Enter a number: "))
status = True  # initially assume number is prime

for i in range(2, n):
    if n % i == 0:   # if divisible by any number → not prime
        status = False
        break        # exit loop immediately

if status == True:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")


# -------- SUM OF EVEN & ODD USING CONTINUE --------
n = int(input("Enter a number: "))
even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:        # even number
        even_sum += i
        continue          # skip adding to odd_sum
    odd_sum += i          # runs only for odd numbers

print("Even sum is :", even_sum, "\nOdd sum is :", odd_sum)


'''
Output:
Enter a number: 179
179 is a prime number
Enter a number: 5
Even sum is : 6 
Odd sum is : 9
-----

'''