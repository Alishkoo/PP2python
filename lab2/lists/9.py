thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23] # how close is number close to 50
thislist.sort(key = myfunc)
print(thislist)