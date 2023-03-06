import os

with open("text.txt", "r") as file:
    text = file.read()
    file.close()

with open("copy.txt", "w") as f:
    f.write(text)
    f.close()