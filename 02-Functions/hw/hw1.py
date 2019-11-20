import string


def letters_range(start, stop=None, step=1, **change):

    alphabet = list(string.ascii_lowercase)
    for i in change:
        alphabet[alphabet.index(i)] = change[i]
    if stop and step == 1:
        return alphabet[alphabet.index(start):alphabet.index(stop)]
    if step != 1:
        return alphabet[alphabet.index(start):alphabet.index(stop):step]

    return alphabet[:alphabet.index(start)]


print(letters_range('b', 'w', 2))
print(letters_range('g'))
print(letters_range('g', 'p'))
print(letters_range('g', 'p', **{'l': 7, 'o': 0}))
print(letters_range('p', 'g', -2))
print(letters_range('a'))
