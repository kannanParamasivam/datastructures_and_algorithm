from collections import defaultdict
from pprint import pprint, pformat
from typing import List


class UndirectedGraph:

    def __init__(self, vertices: List[str]):
        self.adj_list = {vertex: defaultdict(int) for vertex in iter(vertices)}

    def add_edge(self, src, dest, w):
        self.adj_list[src][dest] = w
        self.adj_list[dest][src] = w

    def __str__(self):
        return pformat(self.adj_list)
