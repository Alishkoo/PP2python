def squares(a, b):
    while(pow(a,2) <= b):
        yield pow(a,2)
        a += 1

for i in squares(1, 50):
    print(i)