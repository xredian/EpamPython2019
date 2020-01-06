"""
Реализовать класс Quaternion, позволяющий работать с кватернионами
https://ru.wikipedia.org/wiki/%D0%9A%D0%B2%D0%B0%D1%82%D0%B5%D1%80%D0%BD%D0%B8%D0%BE%D0%BD
Функциональность (магическими методами):
- сложение
- умножение
- деление
- сравнение
- нахождение модуля
- строковое представление и repr
По желанию:
- взаимодействие с числами других типов
"""


class Quaternion:

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__(self, other):
        if isinstance(other, Quaternion):
            a = self.a + other.a
            b = self.b + other.b
            c = self.c + other.c
            d = self.d + other.d
            return Quaternion(a, b, c, d)
        else:
            raise TypeError

    def __mul__(self, other):

        if isinstance(other, Quaternion):

            a1, a2 = self.a, other.a
            b1, b2 = self.b, other.b
            c1, c2 = self.c, other.c
            d1, d2 = self.d, other.d

            a = a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2
            b = a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2
            c = a1 * c2 + c1 * a2 + d1 * b2 - b1 * d2
            d = a1 * d2 + d1 * a2 + b1 * c2 - c1 * b2

            return Quaternion(a, b, c, d)

        elif isinstance(other, (int, float)):
            return Quaternion(self.a * other, self.b * other, self.c * other, self.d * other)

        else:
            raise TypeError

    def __abs__(self):
        return (self.a**2 + self.b**2 + self.c**2 + self.d**2)**0.5

    def __truediv__(self, other):
        adjoint = Quaternion(other.a, - other.b, - other.c, - other.d)
        norm = abs(other)**2
        other = adjoint / norm
        return self * other

    def __eq__(self, other):
        return (self.a, self.b, self.c, self.d) == (other.a, other.b, other.c,
                                                    other.d)

    def __str__(self):
        return f'{self.a} + {self.b}i + {self.c}j + {self.d}k'

    def __repr__(self):
        return f'Quaternion({self.a}, {self.b}, {self.c}, {self.d})'

