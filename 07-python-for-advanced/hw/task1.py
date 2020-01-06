"""

Реализовать такой метакласс, что экземпляры класса созданного с помощью него
будут удовлетворять следующим требованиям:

* объекты созданные с одинаковыми аттрибутами будут одним и тем же объектом
* объекты созданные с разными аттрибутами будут разными объектами
* у любого объекта есть мозможность получить доступ к другим объектам
    того же класса


>>> unit1 = SiamObj('1', '2', a=1)
>>> unit2 = SiamObj('1', '2', a=1)
>>> unit1 is unit2
True
>>> unit3 = SiamObj('2', '2', a=1)
>>> unit3.connect('1', '2', 1).a = 2
>>> unit2.a == 2
True
>>> pool = unit3.pool
>>> print(len(pool))
2
>>> del unit3
>>> print(len(pool))
1

"""
import weakref


class Meta(type):

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls._insts = {}
        cls.pool = cls._insts

    def connect(cls, *args, **kwargs):
        con_args = args + tuple(kwargs.values())
        for key, value in cls._insts.items():
            if value == con_args:
                return key()
        else:
            print(f'There is no instance with attributes {con_args}')

    def __call__(cls, *args, **kwargs):

        setattr(cls, 'connect', cls.connect)

        def delete(instance):
            try:
                del cls._insts[weakref.ref(instance)]
            except KeyError:
                pass

        cls.__del__ = delete
        inst = super().__call__(*args, **kwargs)
        con_args = args + tuple(kwargs.values())
        for key, value in cls._insts.items():
            if value == con_args:
                return key()
        else:
            cls._insts[weakref.ref(inst)] = con_args
            return inst


class SiamObj(metaclass=Meta):
    def __init__(self, *args, a: int, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.a = a


if __name__ == '__main__':
    unit1 = SiamObj('1', '2', a=1)
    unit2 = SiamObj('1', '2', a=1)
    print(unit1 is unit2)

    unit3 = SiamObj('2', '2', a=1)
    unit3.connect('1', '2', 1).a = 2
    print(unit2.a == 2)

    pool = unit3.pool
    print(len(pool))

    del unit3
    print(len(pool))
