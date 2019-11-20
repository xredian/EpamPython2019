import inspect


def modified_func(func, *fixated_args, **fixated_kwargs):

    def new_func(*fixed_args, **fixed_kwargs):
        frame = inspect.currentframe()
        args = inspect.getargvalues(frame)[3]
        code = inspect.getsource(func)
        if args['fixated_args'] is None and args['fixated_kwargs'] is None:
            return func(*fixated_args, **fixated_kwargs)
        new_func.__name__ = f'func_{func.__name__}'
        doc = f"A func implementation of func_{new_func.__name__} " \
              f"with pre-applied arguments being: " \
              f"{args['fixated_args']}, {args['fixated_kwargs']}; " \
              f"source code:" \
              f"{code}"
        new_func.__doc__ = doc
        new_args = [*fixed_args, *fixated_args]
        new_kwargs = {**fixed_kwargs, **fixated_kwargs}
        return func(*new_args, **new_kwargs)

    return new_func


def test_function(*args, **kwargs):
    print(args, kwargs)


f1 = modified_func(test_function)
f2 = modified_func(test_function, 1, 0, **{'1': True, '0': False})
print(f1(), f1.__doc__, f1.__name__)
print(f2(), f2.__doc__, f2.__name__)
