from collections import deque

# Creating a deque
d = deque([10, 20, 30, 40, 50])
print("Original deque:", d)

# Add element at right end
d.append(60)
print("After append(60):", d)

# Add element at left end
d.appendleft(5)
print("After appendleft(5):", d)

# Remove element from right
d.pop()
print("After pop():", d)

# Remove element from left
d.popleft()
print("After popleft():", d)

# Reverse the deque
d.reverse()
print("After reverse():", d)

# Rotate right by 2 positions
d.rotate(2)
print("After rotate(2):", d)

# Rotate left by 1 position
d.rotate(-1)
print("After rotate(-1):", d)

# Add multiple elements at right
d.extend([70, 80])
print("After extend([70, 80]):", d)

# Add multiple elements at left
d.extendleft([1, 2])
print("After extendleft([1, 2]):", d)

# Count occurrences
print("Count of 30:", d.count(30))

# Index of element
print("Index of 40:", d.index(40))

# Length of deque
print("Length of deque:", len(d))
