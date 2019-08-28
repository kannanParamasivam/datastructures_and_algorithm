'''Single Source Shortest Path algorithm
Find shortest path from given source node to all other nodes in graph'''

from typing import List
from queue import PriorityQueue
from sys import maxsize

class Graph:


    def __init__(self, vertices: List[str]):
        self.adj_mat = [[-1] * len(vertices) for vertex in iter(vertices)]
        self.vertices = {vertex:pos for pos, vertex in enumerate(vertices) }

    
    def add_edge(self, src, dest, w = 0):
        self.adj_mat[self.vertices[src]][self.vertices[dest]] = w
        self.adj_mat[self.vertices[dest]][self.vertices[src]] = w


    def dijkstra(self, start: str):
        pq = PriorityQueue()
        shortest_paths = [[None,maxsize] for x in self.vertices]
        pq.put((0,self.vertices[start]))
        shortest_paths[self.vertices[start]][0] = None
        shortest_paths[self.vertices[start]][1] = 0
        visited = [False]*len(self.vertices)

        while not pq.empty():
            dist, vertex = pq.get()
            

            if visited[vertex] == False:
                
                for child, weight in enumerate(self.adj_mat[vertex]):
                
                    if weight >= 0 and visited[child] == False:
                        child_dist = dist + weight
                        pq.put((child_dist, child))
                        
                        if shortest_paths[child][1] > child_dist:
                            shortest_paths[child][0] = vertex
                            shortest_paths[child][1] = child_dist
            
            visited[vertex] = True
            
        keys = list(self.vertices.keys())
        return {keys[pos]:self.get_list(data,keys) for pos, data in enumerate(shortest_paths)}


    def get_list(self, data:List,keys):
        l = list()
        l.append(keys[data[0]] if data[0] != None else None)
        l.append(data[1])
        return l

        