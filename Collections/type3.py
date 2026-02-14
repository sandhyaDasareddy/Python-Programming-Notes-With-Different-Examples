from collections import namedtuple

Student = namedtuple('Student', ('name', 'age', 'Stream', 'avg_marks'))

s1 = Student('Sandhya', 26, 'AI&ML', 87)

print("Student:", s1)
print("Name (index):", s1[0])
print("Age (field):", s1.age)

# Additional operations
print("Stream:", s1.Stream)
print("As dictionary:", s1._asdict())

# Replace value
s2 = s1._replace(age=27)
print("Updated Student:", s2)

# Field names
print("Fields:", Student._fields)
