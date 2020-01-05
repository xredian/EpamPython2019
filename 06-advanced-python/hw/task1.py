"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной
Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)
"""
from collections import deque


class Graph:
    def __init__(self, E):
        self.E = E

    def __iter__(self):
        self.visited = {}
        self.not_visited = list(self.E.keys())
        self.queue = deque(self.not_visited[0])
        return self

    def __next__(self):
        while self.not_visited:
            if not self.queue:
                self.queue.append(self.not_visited[0])
            vis = self.queue.popleft()
            if not self.visited.get(vis):
                self.visited[vis] = True
                self.not_visited.remove(vis)
            for elem in self.E[vis]:
                if not self.visited.get(elem):
                    self.visited[elem] = True
                    self.not_visited.remove(elem)
                    self.queue.append(elem)
            return list(self.visited)
        raise StopIteration


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
graph = Graph(E)

for vertex in graph:
    print(vertex)
