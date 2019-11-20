import inspect


def modified_func(func, *fixated_args, **fixated_kwargs):

    def new_func(*fixed_args, **fixed_kwargs):
        """
        A func implementation of func_{func.__name__}
        with pre-applied arguments being:
        fixated_args values: {fixated_args}
        fixated_kwargs values: {fixated_kwargs}
        source_code: {code}
        """
        frame = inspect.currentframe()
        args = inspect.getargvalues(frame)[3]
        code = inspect.getsource(new_func)
        replace = [['{fixated_args}', str(args['fixated_args'])],
                   ['{fixated_kwargs}', str(args['fixated_kwargs'])],
                   ['{code}', code[code.rfind('\"\"\"') + 3:]],
                   ['{func.__name__}', str(func.__name__)]]
        for replace in replace:
            new_func.__doc__ = new_func.__doc__.replace(*replace)
        new_func.__name__ = f'func_{func.__name__}'
        new_args = [*fixed_args, *fixated_args]
        new_kwargs = {**fixed_kwargs, **fixated_kwargs}
        return func(*new_args, **new_kwargs)

    return new_func


def test_function(*args, **kwargs):
    print(args, kwargs)


f1 = modified_func(test_function)
f2 = modified_func(test_function, 1, 0, **{'1': True, '0': False})
f1()
f2()
print(f1.__doc__, f1.__name__)
print(f2.__doc__, f2.__name__)
