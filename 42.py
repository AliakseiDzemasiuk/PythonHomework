from string import ascii_lowercase
from collections import Counter

def most_common_words(path,number_of_words):
    fil=open(path,'r')
    data=''.join([string for string in fil])
    data=''.join(a for a in data.lower() if a in (ascii_lowercase+' '))
    fil.close()
    ctuples=Counter(data.split(' ')).most_common(number_of_words)
    return [a for (a,_) in ctuples]

print(most_common_words('lorem_ipsum.txt',3))
