from typing import List
from pprint import pprint


class Solution:


    def find_tree(self, nodes, edges) -> List[int]:
        
        if not edges:
            return

        # a) initialize graph
        g = {n:[] for n in range(nodes)}

        # b) initialize in-degree counter
        inDeg = {n:0 for n in range(nodes)}

        # c) populate graph and in-degree counter
        for edge in edges:
            src, dest = edge[0], edge[1]
            
            g[src].append(dest)
            g[dest].append(src)
            
            inDeg[src] += 1
            inDeg[dest] += 1
        
        # d) find leaves
        leaves = [x for x in inDeg if inDeg[x] <= 1]

        total_nodes = nodes

        # e) propcess the leaves untill total nodes <= 2
        while total_nodes > 2:
            leaf_nodes = len(leaves)
            total_nodes -= leaf_nodes

            for _ in range(leaf_nodes):

                leaf = leaves.pop(0)

                # f) process children of leaf
                for child in g[leaf]:
                    inDeg[child] -= 1

                    if inDeg[child] == 1:
                        leaves.append(child)

        return list(leaves)


sol = Solution()
print(sol.find_tree(5, [[0,1], [1,2], [1,3], [2,4]])) 