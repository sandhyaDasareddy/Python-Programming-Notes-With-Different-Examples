from collections import ChainMap

# Individual category dictionaries
clothes = {'shirts': 5, 'pants': 3, 'blazers': 10}
electronics = {'laptops': 2, 'phones': 4, 'tablets': 3}
food = {'fruits': 10, 'vegetables': 15, 'meat': 5}

# Combine using ChainMap
inv = ChainMap(clothes, electronics, food)

print("Original ChainMap:")
print(inv)
print()

# Accessing values
print("Number of shirts:", inv['shirts'])
print("Number of laptops:", inv['laptops'])
print()

# Updating using ChainMap (always updates first dictionary)
inv['laptops'] = 55
print("After updating laptops using ChainMap:")
print(inv)
print("Clothes dictionary:", clothes)  # laptops added here
print()

# Updating original electronics dictionary directly
inv.maps[1]['phones'] = 20
print("After updating phones in electronics:")
print(inv)
print("Electronics dictionary:", electronics)
print()

# Adding a new item
inv['jackets'] = 7
print("After adding new item (jackets):")
print(inv)
print()

# Display individual dictionaries
print("Final Dictionaries:")
print("Clothes:", clothes)
print("Electronics:", electronics)
print("Food:", food)
