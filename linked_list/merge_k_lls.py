from typing import List
from queue import PriorityQueue

class Node:
    
    def __init__(self, val:int, nxt = None):
        self.val = val
        self.next = nxt


def merge_linked_lists(lists:List[Node]) -> List[Node]:
    
    pq = PriorityQueue()
    res_head = res_node = Node(-1);
    
    for node in lists:
        pq.put((node.val, node))
        
    while not pq.empty():
        val, node = pq.get();
        res_node.next = node;
        res_node = node
        
        if node != None and node.next != None:
            pq.put((node.next.val, node.next))
            
    return res_head.next
        