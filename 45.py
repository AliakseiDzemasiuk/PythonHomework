def remember_result(f):
    lresult=None
    def wrapper(*args, **kwargs):
        nonlocal lresult
        print('Last result: '+str(lresult))
        lresult=f(*args,**kwargs)
        print('Current result: '+str(lresult))
        return lresult
    return wrapper


@remember_result
def sum(a,b):
    return a+b




sum(3,4)
sum(3,6)
sum(4,11)
