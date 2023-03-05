tup = input().split(' ')
tup = tuple([eval(i) for i in tup])
print(all(tup))