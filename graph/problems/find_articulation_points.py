from collections import defaultdict
from typing import List

class Node:
    def __init__(self, val):
        self.val = val
        self.dfn_no = -1
        self.low_dfn_no = -1
        self.children = []
        

class ArticulationFinder:
    
    def __init__(self):
        self.nodes = defaultdict(list)
        
    
    def find_articulation_point(self,connections: List[List[int]]):
        for connection in connections:
            src = None
            if connection[0] in self.nodes:
                src = self.nodes[connection[0]]
            else:
                src = Node(connection[0])
                
            dest = None
            
            if connections[1] in self.nodes:
                dest = self.nodes[connection[1]]
            else:
                dest = Node(connection[1])
                
            src.children.a