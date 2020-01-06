"""
Написать свое property c кэшем и таймаутом
полностью повторяет поведение стандартной property за исключением:
    * хранит результат работы метода некоторое время, которое передается
      параметром в инициализацию проперти
    * пересчитывает значение, если таймер истек
"""

import time
import uuid


def timer_property(t: int):

    class Property:

        def __init__(self, fget=None, fset=None, fdel=None, doc=None):
            self.fget = fget
            self.fset = fset
            self.fdel = fdel
            self.__doc__ = doc
            self.timer = 0
            self.result = 0

        def __get__(self, obj, objtype=None):
            if obj is None:
                return self
            if self.fget is None:
                raise AttributeError("can't read attr")
            if not self.timer or time.time() - self.timer > t:
                self.result = self.fget(obj)
                self.timer = time.time()
            return self.result

        def __set__(self, obj, result):
            if self.fset is None:
                raise AttributeError("can't set attr")
            self.result = result
            self.timer = time.time()

        def __delete__(self, obj):
            if self.fdel is None:
                raise AttributeError("can't del attr")
            self.fdel(obj)

        def getter(self, fget):
            return type(self)(fget, self.fset, self.fdel, self.__doc__)

        def setter(self, fset):
            return type(self)(self.fget, fset, self.fdel, self.__doc__)

        def deleter(self, fdel):
            return type(self)(self.fget, self.fset, fdel, self.__doc__)

    return Property


class Message:

    @timer_property(t=10)
    def msg(self):
        self._msg = self.get_message()
        return self._msg

    @msg.setter  # reset timer also
    def msg(self, param):
        self._msg = param

    def get_message(self):
        """
        Return random string
        """
        return uuid.uuid4().hex


if __name__ == '__main__':
    m = Message()
    initial = m.msg
    assert initial is m.msg
    time.sleep(10)
    assert initial is not m.msg
