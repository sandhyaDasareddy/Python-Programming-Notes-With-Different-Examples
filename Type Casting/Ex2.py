'''
Data types are classified into 2 types:
--------------------------------------
1. Immutable data types  
   (Once you assign a value, you cannot change the object in memory)
   Examples:
   int
   float
   str
   bool
   tuple

2. Mutable data types  
   (You can change the object in memory)
   Examples:
   list
   set
   dict
'''

# Immutable Example
a = 10
print(a)
print(type(a))
print(id(a))

b = 10
print(b)
print(type(b))
print(id(b))
print(id(a))

print(a is b)   # checks if both refer to same memory

# Mutable Example
lst = [1, 2, 3]
print(lst)
print(type(lst))

lst.append(56)  # modifies the same list
print(lst)

lst1 = lst.copy()  # creates a new list
print(lst1)

print(lst is lst1)  # False because they are different objects

print(id(lst))
print(id(lst1))

'''
Output:-
------
10
<class 'int'>
140725882071768
10
<class 'int'>
140725882071768
140725882071768
True
[1, 2, 3]
<class 'list'>
[1, 2, 3, 56]
[1, 2, 3, 56]
False
2313343603008
2313343889920

'''