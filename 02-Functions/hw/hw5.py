from time import time
import math


def calls(func):
    counter = {}
    counter[func] = 0

    def wrapper(*args, **kwargs):
        counter[func] += 1
        tmp = time()
        result = func(*args, **kwargs)
        return f'функция {func.__name__} вызывалась {counter[func]} раз, ' \
               f'время выполнения: {time() - tmp}, результат: {result}'

    return wrapper


@calls
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


@calls
def fib1(n):
    if n < 3:
        return 1
    return fib1(n-1) + fib1(n-2)


@calls
def fib2(n):
    s = math.sqrt(5)
    phi = (s + 1) / 2
    return int(phi ** n / s + 0.5)


print(fib(10))
print(fib(50))
print(fib(100))


print(fib2(10))
print(fib2(50))
print(fib2(100))

print(fib1(10))

