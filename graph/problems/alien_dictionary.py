from typing import List
from collections import defaultdict


class Solution:

    @staticmethod
    def alienOrder(words: List[str]) -> str:
        i = 1
        adj_list = defaultdict(list)

        while i < len(words):
            word = words[i-1]
            nextWord = words[i]

            for charW1, charW2 in zip(word, nextWord):
                if charW1 != charW2:
                    adj_list[charW1].append(charW2)
        
        topSorter = TopologicalSorter(adj_list)
        lettersOrder = topSorter.sort()
        return ''.join(lettersOrder)



class TopologicalSorter:

    self.visited = set()
    self.stack = []
    
    def __init__(self, adjList: defaultdict[str,List[str]]) -> str:
        self.graph = adjList


    def sort(self) -> List[str]:

        for vertex in self.graph:
            if vertex not in self.visited:
                self.top_sort(vertex)

        res = []
        
        while len(self.stack) > 0:
            res.append(self.stack.pop())

        return res

    
    def top_sort(self, vertex):

        self.visited.add(vertex)

        for adjVertex in self.graph[vertex]:
            top_sort(adjVertex)

        self.stack.append(vertex)
        


                


    
    




        