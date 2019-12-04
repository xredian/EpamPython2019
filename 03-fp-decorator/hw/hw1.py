import functools

# problem 9

print([a*b * (a**2 + b**2)**0.5 for a in range(500) for b in range(500)
       if a+b + (a**2 + b**2)**0.5 == 1000][0])

# problem 6

print(sum(i for i in range(101))**2 - sum(i**2 for i in range(101)))

# problem 48

print(sum(i**i for i in range(1, 1001)) % 10**10)

# problem 40


def func(n: list):

    number = str().join(str(i) for i in range(0, n[-1]))

    return functools.reduce(lambda x, y: int(x) * int(y), [number[i] for i in n])


print(func([1, 10, 100, 1000, 10000, 100000, 1000000]))
