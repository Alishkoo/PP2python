def f(num):
    n = 0
    while(n < num):
        if(n % 2 == 0):
            yield n
        n += 1
x = int(input())

for i in f(x):
    print(i, end= ', ')