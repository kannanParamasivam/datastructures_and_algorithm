'''
Given a Binary Tree, we need to print the bottom view from left to right. A node x is there in output if x is the bottommost node at its horizontal distance. Horizontal distance of left child of a node x is equal to horizontal distance of x minus 1, and that of right child is horizontal distance of x plus 1.

Examples:

                      20
                    /    \
                  8       22
                /   \      \
              5      3      25
                    / \      
                  10    14

For the above tree the output should be 5, 10, 3, 14, 25.

If there are multiple bottom-most nodes for a horizontal distance from root, then print the later one in level traversal. For example, in the below diagram, 3 and 4 are both the bottom-most nodes at horizontal distance 0, we need to print 4.

                   
                      20
                    /    \
                  8       22
                /   \    /   \
              5      3 4     25
                    / \      
                  10    14 
For the above tree the output should be 5, 10, 4, 14, 25.
'''
from typing import List
from helpers import TreeHelper, Node
from sys import maxsize


class Solution:

    def bottom_view(self, root: Node) -> List[int]:
        
        if not root:
            return
        
        res = []
        self.pre_order(root, res)
        
        return res
        
    
    def pre_order(self, root, res):
        
        if not root:
            return
        
        if root.val and ((not root.left and not root.right) or (not root.left.val and not root.right.val)):
            res.append(root.val)
            
        self.pre_order(root.left, res)
        self.pre_order(root.right, res)


sol = Solution()
root = TreeHelper.create_tree([20, 8, 22, 5, 3, None, 25, None, None, 10, 14, None, None, None, None])
TreeHelper.print_tree(root)
print(sol.bottom_view(root))