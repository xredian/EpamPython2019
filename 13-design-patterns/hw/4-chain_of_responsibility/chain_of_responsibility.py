"""
С помощью паттерна "Цепочка обязанностей" составьте список покупок для выпечки блинов.
Необходимо осмотреть холодильник и поочередно проверить, есть ли у нас необходимые ингридиенты:
    2 яйца
    300 грамм муки
    0.5 л молока
    100 грамм сахара
    10 мл подсолнечного масла
    120 грамм сливочного масла

В итоге мы должны получить список недостающих ингридиентов.
"""
from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class AbstractHandler(Handler):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


INGREDIENTS = {'eggs': 2, 'flour': 300, 'milk': 0.5,
               'sugar': 100, 'oil': 10, 'butter': 120}


class Fridge:
    def __init__(self, eggs, flour, milk, sugar, oil, butter):
        self._eggs = eggs
        self._flour = flour
        self._milk = milk
        self._sugar = sugar
        self._oil = oil
        self._butter = butter


class EggsHandler(AbstractHandler):
    def handle(self, fridge: Fridge):
        if fridge._eggs < INGREDIENTS['eggs']:
            print(f"Need to add {INGREDIENTS['eggs'] - fridge._eggs} eggs")
        else:
            print(f"Enough eggs in the fridge")
        if self._next_handler:
            return self._next_handler.handle(fridge)


class FlourHandler(AbstractHandler):
    def handle(self, fridge: Fridge):
        if fridge._flour < INGREDIENTS['flour']:
            print(f"Need to add {INGREDIENTS['flour'] - fridge._flour} grams of flour")
        else:
            print(f"Enough flour in the fridge")
        if self._next_handler:
            return self._next_handler.handle(fridge)


class MilkHandler(AbstractHandler):
    def handle(self, fridge: Fridge):
        if fridge._milk < INGREDIENTS['milk']:
            print(f"Need to add {INGREDIENTS['milk'] - fridge._milk} liters of milk")
        else:
            print(f"Enough milk in the fridge")
        if self._next_handler:
            return self._next_handler.handle(fridge)


class SugarHandler(AbstractHandler):
    def handle(self, fridge: Fridge):
        if fridge._sugar < INGREDIENTS['sugar']:
            print(f"Need to add {INGREDIENTS['sugar'] - fridge._sugar} grams of sugar")
        else:
            print(f"Enough sugar in the fridge")
        if self._next_handler:
            return self._next_handler.handle(fridge)


class OilHandler(AbstractHandler):
    def handle(self, fridge: Fridge):
        if fridge._oil < INGREDIENTS['oil']:
            print(f"Need to add {INGREDIENTS['oil'] - fridge._oil} milliliters of oil")
        else:
            print(f"Enough oil in the fridge")
        if self._next_handler:
            return self._next_handler.handle(fridge)


class ButterHandler(AbstractHandler):
    def handle(self, fridge: Fridge):
        if fridge._butter < INGREDIENTS['butter']:
            print(f"Need to add {INGREDIENTS['butter'] - fridge._butter} grams of butter")
        else:
            print(f"Enough butter in the fridge")
        if self._next_handler:
            return self._next_handler.handle(fridge)


def fill_fridge(fridge):
    eggs_handler = EggsHandler()
    flour_handler = FlourHandler()
    milk_handler = MilkHandler()
    sugar_handler = SugarHandler()
    oil_handler = OilHandler()
    butter_handler = ButterHandler()

    eggs_handler.set_next(flour_handler).set_next(milk_handler).set_next(
        sugar_handler).set_next(oil_handler).set_next(butter_handler)

    eggs_handler.handle(fridge)


fridge = Fridge(eggs=1, flour=200, milk=0.1, sugar=50, oil=5, butter=90)
print(fill_fridge(fridge))

