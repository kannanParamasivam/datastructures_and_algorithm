from typing import List
from sys import maxsize

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    
    def isValidBST(self, root: TreeNode) -> bool:
        return self.check_node(root, -maxsize, maxsize)
    
    
    def check_node(self, node:TreeNode, min_val:int, max_val:int) -> bool:
        
        if node == None:
            return True
        
        if node.val >= min_val and node.val <= max_val and self.check_node(node.left, min_val, node.val) and self.check_node(node.right, node.val, max_val):
            return True
        
        return False
        
    
    def get_tree(self, tree_nodes:List[int], i):
        
        if i >= len(tree_nodes):
            return
        
        cur_node = TreeNode(tree_nodes[i])
        cur_node.left = self.get_tree(tree_nodes, (i*2)+1)
        cur_node.right = self.get_tree(tree_nodes, (i*2)+2)
        
        return cur_node