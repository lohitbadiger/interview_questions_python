# input=> abc
# op=> abc, acb, bca, bac, cab, cba
def permutaion(s):
    output=[]
    if len(s)<=1:
        return s
    else:
        for i, letter in enumerate(s):
            for perm in permutaion(s[:i]+s[i+1:]):
                output+=[letter+perm]
    return output
s='abc'
print(permutaion(s))
print('-------------------------------------------------')

from itertools import permutations

def permutation_of_letters(s):
        string=permutaion(s)
        return string
print(permutation_of_letters(''))
