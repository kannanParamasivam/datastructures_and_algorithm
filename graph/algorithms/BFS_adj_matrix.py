from typing import List
from collections import deque
from pprint import pformat

class Graph:

    def __init__(self, vertices: List[str]):
        self.vertex_lbl = {vertex: pos for pos, vertex in enumerate(vertices)}
        self.adj_mat = [[0]*len(vertices) for x in iter(vertices)]

    def add_edge(self, src, dest):
        self.adj_mat[self.vertex_lbl[src]][self.vertex_lbl[dest]] = 1

    def breadth_first_search(self, start: str):
        res = []
        queue = deque([self.vertex_lbl[start]])
        visited = [False] * len(self.vertex_lbl)
        visited[self.vertex_lbl[start]] = True

        while len(queue) > 0:
            item_in_progress = queue.popleft()

            for pos, child in enumerate(self.adj_mat[item_in_progress]):

                if child > 0 and not visited[pos]:
                    queue.append(pos)
                    visited[pos] = True

            res.append(item_in_progress)

        dic_keys = list(self.vertex_lbl.keys())
        return " ".join([dic_keys[x] for x in res])

    
    def __str__(self):
        return pformat(self.adj_mat)
