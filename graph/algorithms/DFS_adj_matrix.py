from pprint import pformat
from typing import List

class Graph:


    def __init__(self, vertices:List[str]):
        self.adj_mat = [[-1]*len(vertices) for vertex in vertices]
        self.vertex_lbl = {vertex:pos for pos, vertex in enumerate(vertices)}
    

    def add_edge(self, src, dest, w = 1):
        self.adj_mat[self.vertex_lbl[src]][self.vertex_lbl[dest]] = w


    def depth_first_search(self, start):
        visited = [False]*len(self.vertex_lbl)
        visited[self.vertex_lbl[start]] = True
        res = []
        self.DFS_util(self.vertex_lbl[start], visited, res)
        keys = list(self.vertex_lbl.keys())
        return " ".join([keys[res_item] for res_item in res])
    

    def DFS_util(self, v, visited, res):
        res.append(v)
        
        for child_pos, child_val in enumerate(self.adj_mat[v]):
            if not visited[child_pos]:
                visited[child_pos] = True
                self.DFS_util(child_pos, visited, res)



    def __str__(self):
        return pformat(self.adj_mat)

    
