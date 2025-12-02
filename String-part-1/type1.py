'''
s = input("enter a string\n")

for i in range(0,len(s)-2):
    print(s[i:i+3])

s = input("enter a string\n")
print(s[1:len(s)-1])


#reverse given string
s = input("enter a string\n")
res = s[::-1]
print(res)
print(res[len(res)-2:0:-1])


'''
# palindrome string
str1 = input("enter a string\n")
str2 = str1[::-1]
print(str1)
print(str2)
if str1 == str2:
    print("palindrome string")
else:
    print("not palindrome")

'''
Output:
------
Case-1:
enter a string
sandhya
sandhya
ayhdnas
not palindrome

Case-2:
mam
mam
mam
palindrome string

'''






