import os

os.chdir("D:\PP2python\lab6\dir_and_files\exercise6")

for i in range(26):
    with open(f"{chr(i + 65)}.txt", "w"):
        pass