import re

with open('row.txt', 'r', encoding="utf-8") as file:
    text = file.read()

Pattern = "[а-я].*_.*[а-я]"

t = re.findall(Pattern, text)

print(t)