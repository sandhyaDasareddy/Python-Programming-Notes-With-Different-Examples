import re

# ----------- 1. re.match() -----------
text = "python is super easy"
regex = r"python"

match = re.match(regex, text)
print("Match object:", match)

start, end = match.span()
print("Match span:", start, end)

res = text[start:end]
print("Matched text (match):", res)


# ----------- 2. re.search() -----------
match = re.search(regex, text)
print("Matched text (search):", text[match.start():match.end()])


# ----------- 3. META-CHARACTERS EXPLANATION -----------
print("\nMeta-character example: DOT ( . ) → matches any single character\n")


# ----------- 4. DOT (.) META-CHARACTER -----------
text = "python is super easy"
regex = r"."

res = re.findall(regex, text)
print("All characters using '.':", res)

joined = ""
for i in res:
    joined = joined + i
print("Joined characters:", joined)


# ----------- 5. ESCAPED DOT (\.) -----------
text = "python is super easy."
regex = r"\."

res = re.findall(regex, text)
print("Escaped dot matches:", res)
print("First match:", res[0])


# ----------- 6. OR ( | ) META-CHARACTER -----------
text = "python is super easy."
regex = r"python|super"

res = re.findall(regex, text)
print("Matches using OR (python|super):", res)
