from typing import List

class Solution:

    @staticmethod
    def regionsCutBySlashes(grid:List[str]) -> int:
        n = len(grid)
        djs = DisjointSet(n)

        for i in range(n):
            for j in range(n):
                root = ((i*n) + j) * 4
                c = grid[i][j]
                
                if c == '/':
                    djs.union(src=root, dest=root+1)
                    djs.union(src=root+2, dest=root+3)
                elif c == '\\':
                    djs.union(sr=root, dest=root+2)
                    djs.union(src=root+1, dest=root+3)
                else:
                    djs.union(src = root, dest=root+1)
                    djs.union(src = root, dest=root+2)
                    djs.union(src = root, dest=root+3)
                

                if i<n-1:
                    bottom_root = ((i+1) * n + j) * 4
                    djs.union(src=root+3, dest=bottom_root)

                if j<n-1:
                    right_root = ((i*n) + (j+1)) * 4 
                    djs.union(src=root+2, dest=right_root+1)

                if i > 0 and i < n:
                    top_root = ((i-1) * n + j) * 4
                    djs.union(root, top_root+3)

                if j > 0 and j < n:
                    left_root = ((i*n) + (j-1)) * 4 
                    djs.union(root+1, left_root+2)


        return djs.getParentsCount()
                    
    
    


class DisjointSet:


    def __init__(self, n:int):
        self.parents = [-1] * (n*n*4)


    def union(self, src, dest):
        src_parent = self.getParent(src)
        dest_parent = self.getParent(dest)

        if src_parent != dest_parent:
            if abs(self.parents[dest_parent]) > abs(self.parents[src_parent]):
                self.parents[dest_parent] += self.parents[src_parent]
                self.parents[src_parent] = dest_parent

            else:
                self.parents[src_parent] += self.parents[dest_parent]
                self.parents[dest_parent] = src_parent

    
    def getParent(self, vertex):
        parent = vertex

        while self.parents[parent] >= 0:
            parent = self.parents[parent]

        if parent != vertex:
            # self.parents[parent] -= 1
            self.parents[vertex] = parent

        return parent

    
    def getParentsCount(self) -> int:
        return len(list(filter(lambda x: x < 0, self.parents)))