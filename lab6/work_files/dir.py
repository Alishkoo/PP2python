import os

print(os.getcwd())

os.chdir("D:\PP2python\lab6\dir_and_files")

with open("text.txt" , "w") as f:
    f.write("Hello bro\n")
    f.write("its interesting")

