def collatz_steps(n: int, steps=0):
    return collatz_steps(n / 2 if n % 2 == 0 else n * 3 + 1, steps=steps + 1) \
        if n != 1 else steps


assert collatz_steps(16) == 4
assert collatz_steps(12) == 9
assert collatz_steps(1000000) == 152
