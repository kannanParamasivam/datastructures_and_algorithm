from collections import defaultdict


class Graph:


    def __init__(self):
        self.adjLst = defaultdict(list)


    def add_edge(self, src, dest):
        self.adjLst[src].append(dest)


    def topological_sort(self, startVertex):
        self.visited = set()
        self.stack = []

        self.top_sort(startVertex)

        for vertex in self.adjLst:
            self.top_sort(vertex)

        i = 0-len(self.stack)
        while i < 0:
            print(self.stack[i])
            i += 1

        return list(reversed(self.stack))


    def top_sort(self, vertex):

        if vertex not in self.visited:
            self.visited.add(vertex)

            for adjVtx in self.adjLst[vertex]:
                self.top_sort(adjVtx)

            self.stack.append(vertex)
