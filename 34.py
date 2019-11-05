def combine_dicts(*args):
    res={}
    for nu in args:
        for a in nu:
            try:
                res[a]+=nu[a]
            except:
                res[a]=nu[a]
    return res
