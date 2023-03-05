s = input("enter a word: ")

def is_palindrom(word):
    return word == word[::-1]


if(is_palindrom(s)):
    print('yes')
else:
    print('no')
