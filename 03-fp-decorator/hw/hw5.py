from time import time
import math


def counter(counter_name):
    def calls(func):
        def wrapper(*args, **kwargs):
            globals()[counter_name]['count'] += 1
            tmp = time()
            globals()[counter_name]['duration'] += time() - tmp
            result = func(*args, **kwargs)
            return f"функция {func.__name__} вызывалась " \
                   f"{globals()[counter_name]['count']} раз, " \
                   f"время выполнения: {globals()[counter_name]['duration']}, " \
                   f"результат: {result}"
        return wrapper
    return calls


@counter('counter_1')
def fib1(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


@counter('counter_2')
def fib2(n):
    if n < 3:
        return 1
    res = fib2(n-1) + fib2(n-2)
    return res


@counter('counter_3')
def fib3(n):
    s = math.sqrt(5)
    phi = (s + 1) / 2
    return int(phi ** n / s + 0.5)


counter_1 = {'count': 0, 'duration': 0}
counter_2 = {'count': 0, 'duration': 0}
counter_3 = {'count': 0, 'duration': 0}


fib2(5), counter_2
fib2(10), counter_2
print(fib2(25), counter_2)

fib3(5), counter_3
fib3(10), counter_3
print(fib3(25), counter_3)

fib1(5), counter_1
fib1(10), counter_1
print(fib1(25), counter_1)


if counter_1['duration'] > counter_2['duration']:
    if counter_3['duration'] > counter_2['duration']:
        print(f'Наиболее оптимальный метод: fib2')
    else:
        print(f'Наиболее оптимальный метод: fib3')
else:
    if counter_3['duration'] > counter_1['duration']:
        print(f'Наиболее оптимальный метод: fib1')
    else:
        print(f'Наиболее оптимальный метод: fib3')
