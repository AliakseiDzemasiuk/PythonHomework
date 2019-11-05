def generate_squares(numb):
    return {a: a*a for a in range(1,numb+1)}


print(generate_squares(5))
