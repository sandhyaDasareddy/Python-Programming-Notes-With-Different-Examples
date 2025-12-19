'''
1. What is a List?
------------------
What is a List in Python?
A list is used to store multiple values in a single variable.
Lists are:
Ordered (elements have position)
Indexed (start from 0)
Mutable (can be changed)
'''
lst = []
print(lst)      # empty list


#---------------------------------------------------------------------------------------------------
'''
2. Adding Elements to a List (append)
-------------------------------------
append() adds an element at the end of the list.

Indexing starts from 0.

Accessing an index that does not exist causes IndexError:

'''
lst = []
lst.append(10)
print(lst[0])


#---------------------------------------------------------------------------------------------------
'''
3. Creating Lists (Homogeneous & Heterogeneous)
----------------------------------------------
Homogeneous list → same type elements
Example: [1, 2, 3]

Heterogeneous list → different types
Example: integers, float, boolean, string, complex
'''

lst = [10, 20.2, True, 'hello', 2+3j]
print(lst)


#---------------------------------------------------------------------------------------------------
'''
4. Nested Lists and Mixed Data Types
------------------------------------
A list can contain:
List inside list
Tuple
Set
Dictionary
'''

lst1 = [12, 45, 87,
        [20,50,56],
        [743,0,5],
        (3,7,3),
        {3,2,1},
        {1:"devi", 2:"manasa"}]
print(lst1)


#---------------------------------------------------------------------------------------------------
'''
5. Traversing a List (Using for loop)
------------------------------------
1. Loops access elements one by one
2. end=" " prints in the same line
'''

for j in lst1:
    print(j, end=" ")


#---------------------------------------------------------------------------------------------------
'''
6. Accessing Nested Elements
----------------------------
list[index][inner_index]
'''

lst1 = [12,[20,50,56],[743,0,5],(3,7,3),{3,2,1},{1:"devi",2:"manasa"}]

print(lst1[3])        # (3,7,3)
print(lst1[3][0])     # 3
print(lst1[1][2])     # 56
print(lst1[5][1])     # devi


#---------------------------------------------------------------------------------------------------
'''
7. List Concatenation (+) and List Replication (*)
--------------------------------------------------
+ joins two lists
Original lists remain unchanged
'''

lst1 = [10,20,30,40]
lst2 = [40,50,60]
lst3 = lst1 + lst2

print(lst3)

lst = [1,2,3] * 5
print(lst)


#---------------------------------------------------------------------------------------------------
'''
8. List Slicing
---------------
syntax: list[start : stop : step]
'''

lst1 = [10,20,30,40,50,60]

print(lst1[1:5:2])      # [20, 40]
print(lst1[::-1])       # reverse list



#---------------------------------------------------------------------------------------------------
#9. Traversing Using Index
#-------------------------
for i in range(0, len(lst1)):
    print(lst1[i])


#---------------------------------------------------------------------------------------------------
#10. List is Mutable (Modification Possible)
-------------------------------------------
#lst = [10, 20, 30, 40 , 50]

#Adding Elements 
lst.append("ramana")
lst.append("kasi")
print(lst)

#Modifying Elements 
lst[5] = "sandhya"
lst[0] = True
lst[2] = 'A'
print(lst)

#Removing Elements
lst.remove(50)
lst.remove("kasi")
print(lst)

#remove() deletes first occurrence
#Raises error if element not found


#---------------------------------------------------------------------------------------------------

#11. List is Mutable (Can Change Data)
#------------------------------------
#Modify Value

lst = [10, 20, 30, 40 , 50]

lst[0] = True
lst[2] = "A"

print(lst)


#---------------------------------------------------------------------------------------------------
'''
12. Removing Elements from List
-------------------------------
remove()-Removes first occurrence of element

remove() 
1) We can use  to remove special element from the List.  
2) It can’t return any value.
3) If special element not available then we  get VALUE ERROR. 
'''

lst = [True, 20, 'A', 40, 50]

lst.remove(50)
lst.remove('A')

print(lst)


#---------------------------------------------------------------------------------------------------
'''
13. extend() vs +
----------------
extend() - Adds elements one by one
'''

lst = [True, 20, 'A', 40, 50]

lst.extend([70,80,90])
print(lst)

#' + ' Creates a new list
lst = lst + [10,20]
print(lst)


#---------------------------------------------------------------------------------------------------
#14. insert() Method
#------------------
lst = ["pallavi", "geetha", "varsha", "radhi", "mani"]
lst.insert(2, "hello")
print(lst)

#Slice Assignment - Replaces multiple elements at once
lst = [1,2,3,4,5,6,7]
lst[1:4] = [87,9,66,23]


#---------------------------------------------------------------------------------------------------
#15. Removing All Occurrences of an Element
#-----------------------------------------
lst = [1,2,3,3,3,4,5]
n = 3

while n in lst:
    lst.remove(n)

print(lst)


#---------------------------------------------------------------------------------------------------
'''
16. Remove elements from a list using pop() and del
--------------------------------------------------
Deletion in a list can be done in two ways:
1. Value-based deletion  -> remove()
2. Index-based deletion  -> pop(), del

pop() 
1) We can use  to remove last element from the List. 
2) It returned removed element. 
3) If List is empty then we get Error. 

'''
lst = [10, 20, 30, 40, 50, 60]
print("Original list:", lst)

lst.pop()
print("After pop():", lst)

lst.pop(2)
print("After pop(2):", lst)

removed_element = lst.pop(0)
print("Removed element:", removed_element)

print("List after pop operations:", lst)

del lst[1]
print("After del:", lst)


#Removing multiple elements using del with slicing
#-------------------------------------------------
lst1 = [10, 20, 30, 40, 50, 60, 70, 80]
print("Original lst1:", lst1)

lst2 = lst1[2:7]
print("Sliced list (lst2):", lst2)

del lst1[2:7:2]
print("lst1 after del slicing:", lst1)

del lst1[-2:-5:-1]
print("Final lst1:", lst1)

