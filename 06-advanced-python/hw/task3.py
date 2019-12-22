""""
Реализовать контекстный менеджер, который подавляет переданные исключения
with Suppressor(ZeroDivisionError):
    1/0
print("It's fine")
"""


class Suppressor:
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exctype, excvalue, tb):
        return exctype is not None and issubclass(exctype, self.exceptions)


with Suppressor(ZeroDivisionError):
    print(1/0)
print("It's fine")
