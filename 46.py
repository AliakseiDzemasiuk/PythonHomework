def decorator(f):
    def wrapper(*args,**kwargs):
        if not wrapper.is_called:
            wrapper.is_called=True
            return f(*args, **kwargs)
    wrapper.is_called=False
    return wrapper


