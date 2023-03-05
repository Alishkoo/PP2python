s = input("Enter a string: ")

def count(word):
    up = 0
    un = 0
    for i in range(len(word)):
        if(word[i] <= 'Z' and word[i] >= 'A'):
            up += 1
        else:
            un += 1
    return up, un

print(count(s))
