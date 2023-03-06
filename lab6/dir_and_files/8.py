import os

path = os.getcwd()
file_name = "copy.txt"
if(os.path.exists(path) and os.path.exists(file_name)):
    os.remove(file_name)
    print("File deleted")
else:
    print("File or path in this directory does not exists ")
