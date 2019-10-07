from queue import PriorityQueue as pq
from collections import defaultdict
from pprint import pprint as pp


class Graph:

    def __init__(self, vertices):
        self.vertexLbl = {vertex: pos for pos, vertex in enumerate(vertices)}
        self.vertices = vertices
        self.adjMat = [[-1] * len(vertices) for vertex in vertices]

    def add_edge(self, src, dest, w=0):
        self.adjMat[self.vertexLbl[src]][self.vertexLbl[dest]] = w
        self.adjMat[self.vertexLbl[dest]][self.vertexLbl[src]] = w

    def prims(self):
        mst = defaultdict(list)
        cost = 0
        visited = set()
        q = pq()

        q.put((0, (0, 0)))

        while not q.empty() and len(mst) < len(self.vertexLbl):
            weight, (src, dest) = q.get()

            if src != dest and dest not in visited:
                mst[self.vertices[src]].append((self.vertices[dest], weight))
                mst[self.vertices[dest]].append((self.vertices[src], weight))
                cost += weight
                print(f'{self.vertices[src]} -> {self.vertices[dest]} ({weight} ({cost}))')

            visited.add(dest)

            for adjVertex in range(len(self.adjMat[dest])):

                if adjVertex not in visited and dest != adjVertex and self.adjMat[dest][adjVertex] >= 0:
                    q.put((self.adjMat[dest][adjVertex], (dest, adjVertex)))

            

        pp(mst)

        return cost
