from collections import defaultdict
from typing import List
from pprint import pprint


class Solution:


    def topological_sort(self, connections: List[List]) -> List[int]:

        # Create graph (adj list)
        g = defaultdict(list)

        for connection in connections:
            g[connection[0]].append(connection[1])
            
            if connection[1] not in g:
                g[connection[1]] = []

        # create degree map
        deg = defaultdict(int)

        for parent in g.keys():
            
            if parent not in deg:
                deg[parent] = 0
            
            for child in g[parent]:
                deg[child] += 1

        # append queue with sources
        q  = [x for x in deg.keys() if deg[x] == 0]

        # process the queue
        result:List[int] = []

        while q:
            source = q.pop(0)

            if source not in g:
                return

            # reduce in degree for children
            for child in g[source]:
                deg[child] -= 1

                if deg[child] == 0:
                    q.append(child)

            # remove source from graph
            del g[source]

            # add source to result
            result.append(source)

        pprint(result)
        return result
            
    
            


        
        
        


sol: Solution = Solution()
sol.topological_sort([[3, 2], [3, 0], [2, 0], [2, 1]])
