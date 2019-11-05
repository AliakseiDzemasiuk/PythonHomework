import re

def kindasplit(string,separator=None):
    if not isinstance(string,str):
        raise TypeError("must be str or None")
    if separator=="":
        raise ValueError("empty separator")
    if not separator:
        return [string]
    start=[0]
    end=[]
    for m in re.finditer(separator,string):
        start.append(m.start())
        end.append(m.end())
    end.append(len(string))
    return [string[a:b] for (a,b) in zip(start,end)]



string=input("Enter string: ")
separator=input("Enter separator: ")
print(kindasplit(string,separator))
