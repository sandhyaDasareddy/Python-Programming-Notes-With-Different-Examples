'''
Basic Data types:-
----------------------------
Integer type data: int
Real number type data: float
Character type data: str
Yes/No type data: bool
Complex number type: complex
'''

# Python is a dynamically typed programming language
# No need to specify data type before creating a variable

a = 10        # integer
b = 22.8      # float
c = 'a'       # string (Python does not have a separate char type)
d = 3 + 4j    # complex number

# triple-quoted string (multiline string)
e = '''python
Java
C
'''

# print() is used to display values using format()
print("a = {a}".format(a=a))
print("b = {b}".format(b=b))
print("c = {c}".format(c=c))
print("d = {d}".format(d=d))
print("e = {e}".format(e=e))

# type() is used to identify the data type of a variable
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

'''
Output:-
-------
a = 10
b = 22.8
c = a
d = (3+4j)
e = python
Java
C

<class 'int'>
<class 'float'>
<class 'str'>
<class 'complex'>
<class 'str'>


'''