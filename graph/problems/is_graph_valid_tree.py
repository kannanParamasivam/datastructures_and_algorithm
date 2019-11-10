'''
Graph is valid tree when it has no cycle and all nodes are connected
'''

from typing import List

visited:set
graph:List[List[int]]

def is_valid_tree(graph: List[List[int]]) -> bool:
    
    visited = set()
    
    # DFS
    has_cycle = DFS(0, graph, visited)
    is_connected = len(visited) == len(graph)
    
    if not has_cycle and is_connected:
        return True
    else:
        return False
    

def DFS(node, graph, visited):
    
    if node in visited:
        # has_cycle = True
        return True
    
    visited.add(node)
        
    for child_node in range(len(graph[node])):
        if graph[node][child_node] == 1:
            if DFS(child_node, graph, visited):
                return True
           
    return False
