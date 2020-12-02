from collections import defaultdict
from typing import List
from pprint import pprint


class Solution:


    def find_order(self, words) -> str:
        
        if not words:
            return

        n_words = len(words)

        # a. create graph of letters and in-degree dictionary
        graph = defaultdict(list)
        inDegree = defaultdict(int)

        for i in range(n_words - 1):
            word1, word2 = words[i], words[i+1]

            for l1, l2 in zip(word1, word2):
                
                if l1 != l2:
                    graph[l1].append(l2)
                    inDegree[l2] += 1
                
                    if l2 not in graph:
                        graph[l2] = []

                    if l1 not in inDegree:
                        inDegree[l1] = 0
                    
                    break

        # b. create sources queue
        sources = [x for x in inDegree.keys() if inDegree[x] == 0]

        result = []

        # c. process the sources
        while sources:
            source = sources.pop(0)
            
            if source not in graph:
                return

            # c.a. decrease in-degrees of children
            for child in graph[source]:
                inDegree[child] -= 1

                # c.a.a. add child when its in-degree gets to 0
                if inDegree[child] == 0:
                    sources.append(child)

            # c.b. add source to the result
            result.append(source)

            # c.c. remove source from graph
            del graph[source]

        # check if all letters are included into the result
        if len(result) == len(inDegree):
            return ''.join(result)


sol = Solution()
assert sol.find_order(["wrt","wrf","er","ett","rftt"]) == "wertf"
assert sol.find_order(["z","x"]) == "zx"
assert sol.find_order(["cab","aaa", "aab"]) == "cab"
assert sol.find_order(["ywx","wz", "xww", "xz", "zyy", "zwz"]) == "ywxz"
