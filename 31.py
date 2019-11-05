from string import ascii_lowercase
from functools import reduce

def test_1_1(strings):
    arg=list(map(set,strings))
    return reduce(lambda x,y: x & y, arg)

def test_1_2(strings):
    arg=list(map(set,strings))
    return reduce(lambda x,y: x | y, arg)

def test_1_3(strings):
    dicto={a: 0 for a in ascii_lowercase}
    for string in strings:
        for b in set(string):
            dicto[b]+=1
    return set(a for a in dicto if dicto[a]>1)

def test_1_4(strings):
    return set(ascii_lowercase)-test_1_2(strings)

