# Number conversions
a = 70
print("Number:", a)
print("Binary   :", "{:b}".format(a))
print("Octal    :", "{:o}".format(a))
print("Hexadecimal:", "{:x}".format(a))

# User input
name = input("Enter your name: ")
place = input("Enter your place: ")

# Using f-string
print(f"My name is {name} and my place is {place}")

# Raw string literal
raw_name = r"Ro\nhit"
print("Raw string output:", raw_name)

'''
Output:
------
Number: 70
Binary   : 1000110
Octal    : 106
Hexadecimal: 46
Enter your name: sandhya
Enter your place: kadapa
My name is sandhya and my place is kadapa
Raw string output: Ro\nhit
'''