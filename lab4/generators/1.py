def f(num):
    n = 1
    while(pow(n, 2) < num):
        yield pow(n, 2)
        n += 1

for i in f(50):
    print(i)