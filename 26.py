def get_shortest_word(text):
    return sorted(text.split(' '),key=len,reverse=True)[0]

