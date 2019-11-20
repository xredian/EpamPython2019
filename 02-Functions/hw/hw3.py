counter_name = 0


def make_it_count(function, counter_name):

    def new_func():
        function()
        global counter_name
        counter_name += 1
        return counter_name

    return new_func()


def func():
    print('func done')


print(make_it_count(func, counter_name))
print(make_it_count(func, counter_name))
print(make_it_count(func, counter_name))
