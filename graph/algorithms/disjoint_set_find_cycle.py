'''Disjoint Set data structure to group edges of a graph into sets
   Union Find is the algorithm on disjoint set which continously does union operation
   Collapsing Find is another name for Union Find
   Can find cycle in Undirected Graph applying Union Find on Disjoint Set'''


class Graph:

    def __init__(self, vertices, directed = False):
        self.adj_mat = [[0]*len(vertices) for _ in vertices]
        self.vertex_lbl = {vertex: pos for pos,
                           vertex in enumerate(vertices)}
        self.directed = directed


    def add_edge(self, src, dest):

        self.adj_mat[self.vertex_lbl[src]][self.vertex_lbl[dest]] = 1

        if not self.directed:
            self.adj_mat[self.vertex_lbl[dest]][self.vertex_lbl[src]] = 1


    def union_find_cycle(self) -> bool:
        self.parent = [-1] * len(self.vertex_lbl)
        visitedEdges = {}

        for src in range(len(self.vertex_lbl)):
            for dest in range(len(self.vertex_lbl)):

                if self.adj_mat[src][dest] == 1 and (visitedEdges.get(src) == None or visitedEdges.get(src) != dest):
                    src_parent: int = self.get_parent(src)
                    dest_parent: int = self.get_parent(dest)

                    if src_parent == dest_parent:
                        return True
                    else:
                        if abs(self.parent[src_parent]) >= abs(self.parent[dest_parent]):
                            self.parent[dest_parent] = src_parent
                            self.parent[src_parent] -= 1
                        else:
                            self.parent[src_parent] = dest_parent
                            self.parent[dest_parent] -= 1

                    if not self.directed:
                        visitedEdges[dest] = src    

        
        return False


    def get_parent(self, vertex) -> int:

        if self.parent[vertex] == -1:
            return vertex

        p = vertex

        while self.parent[p] > -1:
            p = self.parent[p]

        if p != vertex:
            self.parent[vertex] = p # collapse find
        
        return p
