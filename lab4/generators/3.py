def f(num):
    n = 1
    while(n <= num):
        if(n % 3 == 0 or n % 4 == 0):
            yield n
        n += 1

a = f(15)
print(next(a))
print(next(a))
print(next(a))
