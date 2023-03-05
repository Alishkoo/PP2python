import os

path = "D:\PP2python"

if os.path.exists(path):
    print(f"{path} exists.")
else:
    print(f"{path} does not exist.")