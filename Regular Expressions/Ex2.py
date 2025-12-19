import re
from idlelib.colorizer import prog_group_name_to_tag

'''
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

'''
text='''gogle
google
gooogle
goooogle
gooooogle
goooooogle
gooooooogle
'''
'''
regex = r"go{2,5}gle"
lst = re.findall(regex, text)
print(lst)
print("no of occurances: ",len(lst))


text ="python has nothing to do  with the snake python"

regex = r"python$"

match = re.search(regex, text)
print(match)
start,end = match.span()
print(text[start:end])





str ="python java a data scence"

regex = "[aeiou]"
l = re.findall(regex, str)
print(l)
print("no of occurances: ",len(l))

'''

str = "my name is sandhya and this is mu number:"
















































