import string as str

def isPalindrome(string):
    string=('').join(a for a in string.lower() if a in str.ascii_lowercase)
    return string==string[::-1]

string=input('Enter string: ')
print(isPalindrome(string))


