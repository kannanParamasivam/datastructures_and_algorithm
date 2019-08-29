'''All pairs shortest path
Find shortest path between all pairs in the graph (i.e., the distance between all pairs should be as short as possible)
Time Complexity = O(n^3)
Space Complexity = O(1) for inplace as here. If result is different graph then it will be O(n^2)
'''
from typing import List
from sys import maxsize


class Graph:


    def __init__(self, vertices: List[str]):
        self.g = [[maxsize] * len(vertices) for vertex in vertices]
        self.vertex_lbl = {vertex:pos for pos, vertex in enumerate(vertices)}

    
    def add_edge(self, src, dest, w = maxsize):
        self.g[self.vertex_lbl[src]][self.vertex_lbl[dest]] = w

    
    def floydwarshall(self):
        
        # make serf loops 0 weight
        for v in range(len(self.g)):
            self.g[v][v] = 0

        # calculate distance to all oter vertices through each vertex and pick minimum distance
        for v in range(len(self.g)):

            for src in range(len(self.g)):

                if src != v:

                    for dest in range(len(self.g)):

                        if dest != v:

                            self.g[src][dest] = min(self.g[src][dest], (self.g[src][v] + self.g[v][dest]))

        # print result
        keys = [vertex for vertex in self.vertex_lbl.keys()]
        for src in range(len(self.g)):
            for dest in range(len(self.g)):
                if self.g[src][dest] == maxsize:
                    self.g[src][dest] = 'inf'
                print(f'{keys[src]} -> {keys[dest]} ({self.g[src][dest]})')
        
        return self.g
