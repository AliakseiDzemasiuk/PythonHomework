from functools import reduce

def foo(numbers):
    oneless=[[numbor for e, numbor in enumerate(numbers) if e!=i] for i, number in enumerate(numbers)]
    return [reduce(lambda x,y: x*y, arr) for arr in oneless]

