'''
Set:
----
- Set is an unordered collection of data items.
- No indexing (neither +ve nor -ve).
- Set stores only unique elements (duplicates are removed automatically).
- Set is mutable (we can add or remove elements).
'''

s = {10, 20, 30, 40, 50}

print(s)           # Print set
print(type(s))     # Type of set
print(len(s))      # Length of set

s.add(88)          # Add a new element
print(s)

s.remove(88)       # Remove an existing element
print(s)

s.add(21)          # Add another element
print(s)

s.remove(50)       # Remove 50
print(s)

s.add(10)          # Adding duplicate → No change
print(s)


'''
Output:-
-------
{50, 20, 40, 10, 30}
<class 'set'>
5
{50, 20, 40, 10, 88, 30}
{50, 20, 40, 10, 30}
{50, 20, 21, 40, 10, 30}
{20, 21, 40, 10, 30}
{20, 21, 40, 10, 30}

'''