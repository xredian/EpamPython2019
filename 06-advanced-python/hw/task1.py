"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной
Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)
"""


class Graph:
    def __init__(self, E):
        self.E = E

    def __iter__(self):
        self.visited = {}
        self.queue = [list(self.E.keys())[0]]
        return self

    def __next__(self):
        while self.queue:
            vis = self.queue.pop(0)
            self.visited[vis] = True
            for elem in self.E[vis]:
                if elem not in self.queue:
                    try:
                        if not self.visited[elem]:
                            self.queue.append(elem)
                    except KeyError:
                        self.queue.append(elem)
            return vis
        raise StopIteration


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
graph = Graph(E)

for vertex in graph:
    print(vertex)

