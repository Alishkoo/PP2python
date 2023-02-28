import re

with open('row.txt', 'r', encoding="utf-8") as file:
    text = file.read()

Pattern = "\s|,"

t = re.sub(Pattern, ":", text)

print(t)