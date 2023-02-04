from itertools import permutations


def perm(s):
    l = list(permutations(s))
    for i in l:
        print(i)

perm('abc')