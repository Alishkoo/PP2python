import re

with open('row.txt', 'r', encoding="utf-8") as file:
    text = file.read()

Pattern = "[А-Я][а-я]+"

t = re.findall(Pattern, text)

print(t)