def get_pairs(listje):
    return list(zip(listje[:-1],listje[1:])) if len(list(zip(listje[:-1],listje[1:]))) else None

print(get_pairs([3]))

