'''
# Take input string from the user
s = input("Enter a string: ")

# Initialize counters for lowercase, uppercase, special characters, and numbers
low_count, up_count, sp_count, num_count = 0, 0, 0, 0

# Loop through each character in the string
for char in s:
    ch = ord(char)  # Convert character to ASCII value

    # Check if character is uppercase (ASCII range 65–90)
    if ch >= 65 and ch <= 90:
        up_count += 1

    # Check if character is lowercase (ASCII range 97–122)
    elif ch >= 97 and ch <= 122:
        low_count += 1

    # Check if character is a digit (ASCII range 48–57)
    elif ch >= 48 and ch <= 57:
        num_count += 1

    # If not upper/lower/digit → it is a special character
    else:
        sp_count += 1

# Print the results using formatted string
print("lower case character : {}\nupper case characters : {}\nnumeric count : {}\nspecial characters count : {}".format(
    low_count, up_count, num_count, sp_count
))

'''

# Take input string from the user
s = input("Enter a string: ")

# Initialize counters for uppercase, lowercase, digits, and special characters
upper_count, lower_count, num_count, special_count = 0, 0, 0, 0

# Loop through each character in the string
for ch in s:

    # Count uppercase letters
    if ch.isupper():
        upper_count += 1

    # Count lowercase letters
    elif ch.islower():
        lower_count += 1

    # Count digits
    elif ch.isdigit():
        num_count += 1

    # Any other character is a special character
    else:
        special_count += 1

# Print counts using f-string formatting
print(f"Upper count: {upper_count}\n"
      f"Lowercase count: {lower_count}\n"
      f"Number count: {num_count}\n"
      f"Special count: {special_count}")

'''
Output:
------
Enter a string: radha@1234
Upper count: 0
Lowercase count: 5
Number count: 4
Special count: 1


'''