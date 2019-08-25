from pprint import pprint as pp
from typing import List


class UnDirectedGraph:

    def __init__(self, vertices: List[str]):
        self.vertex_lbl = {vertex: i for i, vertex in enumerate(vertices)}
        self.adjMatrix = [[-1]*len(vertices) for vertex in iter(vertices)]


    def set_edge(self, src, dest, w):
        self.adjMatrix[self.vertex_lbl[src]][self.vertex_lbl[dest]] = w
        self.adjMatrix[self.vertex_lbl[dest]][self.vertex_lbl[src]] = w


    def get_adj_matrix(self):
        return self.adjMatrix

    
def print_matrix(m:List[List]):
    for row in m:
        print(row)
        print('\n')