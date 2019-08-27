from typing import List
from collections import defaultdict
from pprint import pformat

class Graph:


    def __init__(self, vertices:List[str]):
        self.adj_lst = {vertex:defaultdict(int) for vertex in vertices}
        self.vertices = vertices

    
    def add_edge(self, src, dest, w = 1):
        self.adj_lst[src][dest] = w


    def depth_first_search(self, start):
        visited = {vertex:False for vertex in self.vertices}
        visited[start] = True
        res = []
        self.DFS_util(start, visited, res)
        return " ".join(res)

    
    def DFS_util(self, v, visited, res):
        res.append(v)

        for child in self.adj_lst[v]:
            if not visited[child]:
                visited[child] = True
                self.DFS_util(child, visited, res)


    def __str__(self):
        return pformat(self.adj_lst)