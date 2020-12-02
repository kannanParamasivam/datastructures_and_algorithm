'''
Check if original seq can be constructed using sequences uniquely
'''

from collections import defaultdict
from typing import List
from pprint import pprint


class Solution:

    
    def can_construct(self, originalSeq:List[int], sequences:List[List[int]]) -> bool:
        
        if not originalSeq:
            return True
        
        if originalSeq and not sequences:
            return False

        graph = defaultdict(list)
        inDeg = defaultdict(int)

        # a) Construct graph of numbers form sequences
        # b) Construct in-degree map
        for seq in sequences:

            for i in range(1, len(seq)):
                n1, n2 = seq[i-1], seq[i]
                graph[n1].append(n2)
                inDeg[n2] += 1

                if n2 not in graph:
                    graph[n2] = []
                
                if n1 not in inDeg:
                    inDeg[n1] = 0

        # c) create sources queue
        sources = [x for x in inDeg.keys() if inDeg[x] == 0]

        sortOrder:List[int] = []

        # d) process srouces queue
        while sources:
            
            # ensure number of sources is 1
            if len(sources) > 1:
                return False

            # e) decrement in-degree for children of sources
            source = sources.pop(0)

            if source not in graph:
                return False

            for child in graph[source]:
                inDeg[child] -= 1
                
                # f) if degree of any child gets to 0 add it to sources queue
                if inDeg[child] == 0:
                    sources.append(child)

            # g) add current source to sort-order
            sortOrder.append(source)

            # h) remove current source - node from graph
            del graph[source]
            
        # i) check sort-order has all numbers
        return True if len(sortOrder) == len(inDeg) else False


sol = Solution()
assert sol.can_construct([1,2,3,4],[[1,2], [2,3], [3, 4]]) == True
assert sol.can_construct([1,2,3,4],[[1,2], [2,3], [2, 4]]) == False
assert sol.can_construct([3,1,4,2,5],[[3,1,5], [1,4,2,5]]) == True
