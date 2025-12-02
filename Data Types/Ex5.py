'''
Dictionary:
-----------
- Used to store data in the form of key–value pairs.
- Keys must be unique.
- Values can be duplicate.
- Dictionary is mutable (we can add, update, or remove items).
'''

d = {
    "Dennis Ritchie": "C",
    "James Gosling": "Java",
    "Guido Van Rossum": "Python"
}

print(d)                       # Print entire dictionary
print(type(d))                 # Type of dictionary
print(d["Dennis Ritchie"])     # Access value using key

d["Brendan Eich"] = "JavaScript"   # Adding a new key-value pair
print(d)

d.pop("Dennis Ritchie")        # Remove key-value pair
print(d)

'''
Output:-
------
{'Dennis Ritchie': 'C', 'James Gosling': 'Java', 'Guido Van Rossum': 'Python'}
<class 'dict'>
C
{'Dennis Ritchie': 'C', 'James Gosling': 'Java', 'Guido Van Rossum': 'Python', 'Brendan Eich': 'JavaScript'}
{'James Gosling': 'Java', 'Guido Van Rossum': 'Python', 'Brendan Eich': 'JavaScript'}

'''