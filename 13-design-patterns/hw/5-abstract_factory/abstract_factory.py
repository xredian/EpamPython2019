"""
Представьте, что вы пишите программу по формированию и выдачи комплексных обедов для сети столовых, которая стала
расширяться и теперь предлагает комплексные обеды для вегетарианцев, детей и любителей китайской кухни.

С помощью паттерна "Абстрактная фабрика" вам необходимо реализовать выдачу комплексного обеда, состоящего из трёх
позиций (первое, второе и напиток).
В файле menu.yml находится меню на каждый день, в котором указаны позиции и их принадлежность к
определенному типу блюд.
"""
from abc import ABC, abstractmethod
import yaml


class AbstractMeal(ABC):
    @abstractmethod
    def starter(self, menu, day) -> str:
        pass

    @abstractmethod
    def main_course(self, menu, day) -> str:
        pass

    @abstractmethod
    def drink(self, menu, day) -> str:
        pass


class ConcreteMealVegan(AbstractMeal):
    def starter(self, menu, day) -> str:
        return menu[day]['first_courses']['vegan']

    def main_course(self, menu, day) -> str:
        return menu[day]['second_courses']['vegan']

    def drink(self, menu, day) -> str:
        return menu[day]['drinks']['vegan']


class ConcreteMealChild(AbstractMeal):
    def starter(self, menu, day) -> str:
        return menu[day]['first_courses']['child']

    def main_course(self, menu, day) -> str:
        return menu[day]['second_courses']['child']

    def drink(self, menu, day) -> str:
        return menu[day]['drinks']['child']


class ConcreteMealChinese(AbstractMeal):
    def starter(self, menu, day) -> str:
        return menu[day]['first_courses']['chinese']

    def main_course(self, menu, day) -> str:
        return menu[day]['second_courses']['chinese']

    def drink(self, menu, day) -> str:
        return menu[day]['drinks']['chinese']


class AbstractFactory(ABC):

    @abstractmethod
    def create_meal(self) -> AbstractMeal:
        pass


class ConcreteFactoryVegan(AbstractFactory):
    def create_meal(self) -> ConcreteMealVegan:
        return ConcreteMealVegan()


class ConcreteFactoryChild(AbstractFactory):
    def create_meal(self) -> ConcreteMealChild:
        return ConcreteMealChild()



class ConcreteFactoryChinese(AbstractFactory):
    def create_meal(self) -> ConcreteMealChinese:
        return ConcreteMealChinese()


def client_code(factory: AbstractFactory, menu, day) -> None:

    meal = factory.create_meal()
    starter = meal.starter(menu, day)
    main_course = meal.main_course(menu, day)
    drink = meal.drink(menu, day)

    print(f'Order contains: {starter}, {main_course}, {drink}') # едем


if __name__ == '__main__':
    with open('./menu.yml', 'r') as file:
        menu = yaml.load(file, Loader=yaml.FullLoader)

    day = input('Input the day of the week: ')

    print('Group of clients: vegan')
    client_code(ConcreteFactoryVegan(), menu, day)
    print("\n")
    print('Group of clients: children')
    client_code(ConcreteFactoryChild(), menu, day)
    print("\n")
    print('Group of clients: lovers of chinese cuisine')
    client_code(ConcreteFactoryChinese(), menu, day)
