from queue import PriorityQueue
from collections import defaultdict
from pprint import pprint as pp


class Graph:


    def __init__(self, vertices):
        self.vertices = vertices
        self.vertexLbl = {vertex: pos for pos, vertex in enumerate(vertices)}
        self.adjMat = [[-1] * len(vertices) for vertex in vertices]


    def add_edge(self, src, dest, w=0):
        self.adjMat[self.vertexLbl[src]][self.vertexLbl[dest]] = w
        self.adjMat[self.vertexLbl[dest]][self.vertexLbl[src]] = w


    def kruskal(self):
        self.disjointSet = [-1] * len(self.vertexLbl)
        mst = defaultdict(list)
        edgePq = PriorityQueue()
        treeWeight = 0
        mstEdgeCount = 0

        self.add_edges_to_pq(edgePq)

        while not edgePq.empty() and mstEdgeCount < len(self.vertexLbl):
            w, (src, dest) = edgePq.get()

            if not self.union_find_is_cycle(src, dest):
                mst[self.vertices[src]] = (self.vertices[dest], w)
                mst[self.vertices[dest]] = (self.vertices[src], w)
                treeWeight += w
                mstEdgeCount += 1
                print(f'{self.vertices[src]} {self.vertices[dest]} {w} {treeWeight}')

        pp(mst)
        return treeWeight


    def add_edges_to_pq(self, edgePq: PriorityQueue):
        for src, dests in enumerate(self.adjMat):
            for dest, w in enumerate(dests):
                if w >= 0:
                    edgePq.put((w, (src, dest)))
                    

    def union_find_is_cycle(self, src, dest):
        srcParent = self.get_parent(src)
        destParent = self.get_parent(dest)

        if srcParent == destParent:
            return True
        else:
            if abs(self.disjointSet[destParent]) > abs(self.disjointSet[srcParent]):
                self.disjointSet[destParent] += self.disjointSet[srcParent]
                self.disjointSet[srcParent] = destParent
            else:
                self.disjointSet[srcParent] += self.disjointSet[destParent]
                self.disjointSet[destParent] = srcParent
            return False


    def get_parent(self, vertex):
        parent = vertex

        while self.disjointSet[parent] >= 0:
            parent = self.disjointSet[parent]

        if parent != vertex:
            self.disjointSet[vertex] = parent
            self.disjointSet[parent] -= 1

        return parent
