from functools import wraps


def applydecorator(decorator):

    def decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return decorator(func, *args, **kwargs)

        return wrapper

    return decor


@applydecorator
def saymyname(f, *args, **kwargs):
    print('Name is', f.__name__)
    return f(*args, **kwargs)

# saymyname is now a decorator
@saymyname
def foo(*whatever):
    return whatever


print(*(foo(40, 2)))
