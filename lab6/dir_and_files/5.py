list = input("enter a numbers ").split(" ")

with open("writed.txt", "w") as file:
    for i in list:
        file.write(str(i) + " ")