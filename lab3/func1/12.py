def histogram(l):
    word = ''
    for i in range(0, len(l)):
        for j in range(0, l[i]):
            word = word + '*'
        print(word)
        word = ''

histogram([4, 9, 7])