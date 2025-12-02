import re

from watchdog.utils.patterns import match_any_paths

# ?---> 0 or 1
text = "a whole hole is not a whole"
regex = r"w?hole"
res = re.findall(regex, text)
print(res)
for item in res:
    print(item)

#*------> 0 or many

regex = r"w*hole"
l = re.findall(regex, text)
print(l)

#   +----> 1 or many
regex = r"w+hole"
l1 = re.findall(regex, text)
print(l1)

str = "I know that no one is there in the school now"
regex = r"k?now?"
lst = re.findall(regex, str)
print(lst)
print("no of occurances: ",len(lst))

