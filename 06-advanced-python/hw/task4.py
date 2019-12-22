"""
Реализовать метод __str__, позволяющий выводить все папки и файлы из данной, например так:
> print(folder1)
V folder1
|-> V folder2
|   |-> V folder3
|   |   |-> file3
|   |-> file2
|-> file1
А так же возможность проверить, находится ли файл или папка в другой папке:
> print(file3 in folder2)
True
"""


class PrintableFolder:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def __contains__(self, item):
        values = []
        result = False
        for elem in self.content:
            if isinstance(elem, PrintableFolder):
                result = item in elem
                values.append(elem)
            else:
                values.append(elem)

        if item in values:
            result = True

        return result

    def __str__(self, tabs=0):
        tab = '/   ' * tabs
        string = ''
        for elem in self.content:
            if isinstance(elem, PrintableFolder):
                string = f'{string}\n{tab}|->{elem.__str__(tabs+1)}'
            else:
                string = f'{string}\n{tab}|->{elem}'
        return f'V {self.name}{string}'


class PrintableFile:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)


if __name__ == '__main__':
    file1 = PrintableFile("file1")
    file2 = PrintableFile("file2")
    file3 = PrintableFile("file3")

    folder3 = PrintableFolder("folder3", [file3])
    folder2 = PrintableFolder("folder2", [folder3, file2])
    folder1 = PrintableFolder("folder1", [folder2, file1])

    print(folder1)
    print(file3 in folder2)
    print(file2 in folder3)
