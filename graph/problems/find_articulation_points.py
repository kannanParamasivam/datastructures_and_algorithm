from collections import defaultdict
from typing import List

class Node:
    def __init__(self, val):
        self.val = val
        self.dfn = -1
        self.low_dfn = -1
        self.children = []
        

class ArticulationFinder:
    
    def __init__(self):
        self.nodes = defaultdict(list)
        self.ap = set()
        self.dfn = 1
        self.visited = set()
        self.root = None
        
    def find_articulation_point(self,connections: List[List[int]]):
        
        for connection in connections:
            self.create_connection(connection)
            
        self.root = 1
        self.nodes[1].low_dfn = 1
        self.dfs(1)
        return list(self.ap)
        
        
    def dfs(self, parent):
        node = self.nodes[parent]
        node.dfn = self.dfn
        node.low_dfn = self.dfn
        self.dfn += 1
        self.visited.add(node.val)
        
        for child in node.children:
            if child.val in self.visited:
                node.low_dfn = child.dfn if node.low_dfn > child.dfn else node.low_dfn
            else:
                low_dfn = self.dfs(child.val)
                node.low_dfn = low_dfn if node.low_dfn > child.low_dfn else node.low_dfn
                
                if child.low_dfn >= node.dfn and node.val != self.root:
                    self.ap.add(node.val)
                
            
        
        return node.low_dfn
            
    
    def create_connection(self, connection:List[int]):
        src = None
        if connection[0] in self.nodes:
            src = self.nodes[connection[0]]
        else:
            src = Node(connection[0])
            self.nodes[connection[0]] = src
            
        dest = None
        
        if connection[1] in self.nodes:
            dest = self.nodes[connection[1]]
        else:
            dest = Node(connection[1])
            self.nodes[connection[1]] = dest
            
        src.children.append(dest)
        dest.children.append(src)