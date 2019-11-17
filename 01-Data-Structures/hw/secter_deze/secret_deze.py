pizza = {"dough", "tomatoes", "pepperoni", "ground pepper", "sweet basil",
         "a lot of cheeeese", "onion", "garlic", "salt", "oregano"}
shaverma = {"lavash", "cucumbers", "tomatoes", "sauce", "fried chicken", "onion", "cabbage"}


if pizza.isdisjoint(shaverma) is True:
    print('имеют общие элементы')
else:
    print('не имеют общих элементов')


if pizza.issubset(shaverma) is True:
    print('pizza является подмножеством shaverma')
else:
    print('pizza не является подмножеством shaverma')


if pizza.issubset(shaverma) is True:
    print('shaverma является подмножеством pizza')
else:
    print('shaverma не является подмножеством pizza')


print(f'объединение множеств pizza и shaverma:\n{set.union(pizza, shaverma)}')

print(f'пересечение множества pizza и shaverma:\n{set.intersection(pizza, shaverma)}')

print(f'все элементы исходных множеств, не принадлежащие одновременно обоим исходным множествам:'
      f'\n{pizza.symmetric_difference(shaverma)}')

