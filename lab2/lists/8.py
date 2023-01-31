fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)


newlist = [x for x in fruits if "a" in x]

print(newlist)

newlist = [x.upper() for x in fruits] # newlist = [expression for item in iterable if condition == True]

print(newlist)