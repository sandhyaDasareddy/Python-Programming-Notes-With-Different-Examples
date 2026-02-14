from collections import Counter

s = "hello how are you"

# Counter from string
cs = Counter(s)
print("Character count:", cs)

# Manual Counter
c = Counter({'a':4, 'b':2, 'c':1, 'd':1, 'e':2, 'f':1, 'g':1})
print("Most common:", c.most_common(1))

# Two counters
c1 = Counter(a=4, b=2, c=1)
c2 = Counter(a=1, b=3, d=2)

# Addition
print("Addition:", c1 + c2)

# Subtraction
print("Subtraction:", c1 - c2)

# Union (max)
print("Union:", c1 | c2)

# Intersection (min)
print("Intersection:", c1 & c2)

# Elements
print("Elements:", list(c1.elements()))
