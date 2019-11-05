def swap(string,substr1='"',substr2="'"):
    return (substr1).join(a.replace(substr1,substr2) for a in string.split(substr2))

string=input("Enter a string: ")
print(swap(string))
