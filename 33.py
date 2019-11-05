def count_letters(text):
    return {a:text.count(a) for a in set(text)}


print(count_letters('stringsample'))
