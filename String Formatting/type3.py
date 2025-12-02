from functools import reduce

# Take input as space-separated numbers
nums = input("enter the numbers: ").split(" ")
print(nums)              # Shows the list of strings
print(type(nums))        # Shows it's a list of strings

# Convert each element to integer
l = list(map(int, nums))
print(l)

# Use reduce() to find the sum of the numbers
res = reduce(lambda x, y: x + y, l)
print(res)

# Calculate average
avg = res / len(l)

# Print average with 4 decimal places, centered (^) inside the field
print("{:^.4f}".format(avg))


'''
Output:
-------
enter the numbers: 1 2 3 4 5
['1', '2', '3', '4', '5']
<class 'list'>
[1, 2, 3, 4, 5]
15
3.0000

'''