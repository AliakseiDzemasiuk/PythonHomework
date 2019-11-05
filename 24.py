def get_pairs(listje):
    return list(zip(listje[:-1],listje[1:]))

def split_by_index(str, indexes):
    indexes=[0]+sorted([a for a in indexes if a>0 and a<len(str)])+[len(str)]
    return [str[a:b] for (a,b) in get_pairs(indexes)]
