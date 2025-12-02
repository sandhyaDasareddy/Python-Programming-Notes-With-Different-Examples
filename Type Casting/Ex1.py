'''
Type Casting in Python

Type casting means converting one data type into another.
Python provides many built-in casting functions:

int()
float()
complex()
str()
list()
tuple()
set()
dict()
hex()
oct()
chr()
ord()

'''
a = 10
print("a = {a}".format(a=a))
print(type(a))

b = float(a)
print("b = {b}".format(b=b))
print(type(b))

c = str(b)
print("c = {c}".format(c=c))
print(type(c))

d = int(b)
print("d = {d}".format(d=d))
print(type(d))

e = complex(b)
print("e = {e}".format(e=e))
print(type(e))

f = hex(a)
print("f = {f}".format(f=f))
print(type(f))

g = complex(b, 5)
print("g = {g}".format(g=g))
print(type(g))

h = oct(a)
print("h = {h}".format(h=h))
print(type(h))

# chr() and ord() usage example
ch = 'A'
print("ch = {ch}".format(ch=ch))
print(type(ch))

i = ord(ch)     # ord() accepts only a single character
print("i = {i}".format(i=i))
print(type(i))

j = chr(90)     # chr() converts number to character
print("j = {j}".format(j=j))
print(type(j))


'''
Output:-
------
a = 10
<class 'int'>
b = 10.0
<class 'float'>
c = 10.0
<class 'str'>
d = 10
<class 'int'>
e = (10+0j)
<class 'complex'>
f = 0xa
<class 'str'>
g = (10+5j)
<class 'complex'>
h = 0o12
<class 'str'>
ch = A
<class 'str'>
i = 65
<class 'int'>
j = Z
<class 'str'>
'''