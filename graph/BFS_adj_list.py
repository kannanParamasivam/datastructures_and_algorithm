from collections import defaultdict, deque
from pprint import pformat
from typing import List

class Graph:


    def __init__(self, vertices: List[str]):
        self.adj_list = {vertex: defaultdict(int) for vertex in vertices}


    def add_edge(self, src, dest):
        self.adj_list[src][dest] = 1


    def breadth_first_search(self, start: str):
        queue = deque([start])
        visited = {vertex: False for vertex, val in self.adj_list.items()}
        visited[start] = True
        res = []

        while len(queue) > 0:
            current_vertex = queue.popleft()

            for child_key, child_value in self.adj_list[current_vertex].items():

                if not visited[child_key]:
                    queue.append(child_key)
                    visited[child_key] = True

            res.append(current_vertex)

        return " ".join(res)


    def __str__(self):
        return pformat(self.adj_list)
