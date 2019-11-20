counter = 0


def make_it_count(function, counter_name: str):

    def new_func():
        globals()[counter_name] += 1
        function()

    return new_func()


def func():
    print('func done')


make_it_count(func, 'counter')
print(counter)
make_it_count(func, 'counter')
print(counter)
make_it_count(func, 'counter')
print(counter)
