def f(num):
    while(num >= 0):
        yield num
        num -= 1

for i in f(50):
    print(i)
