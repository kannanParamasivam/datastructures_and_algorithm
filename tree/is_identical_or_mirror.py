'''
Check if two trees are same. It should satisfying any of the following conditions

1. Both trees are identical
2. One tree is mirror of another
3. Some of the subtrees are mirror and some are identical
'''

from helpers import TreeHelper
from helpers import Node


class Solution:
    
    
    def isSameTree(self, r1: Node, r2: Node) -> bool:
        
        if not r1 and not r2:
            return True
        
        if (not r1 and r2) or (r1 and not r2) or r1.val != r2.val:
            return False
        
        return (self.isSameTree(r1.left, r2.left) and self.isSameTree(r1.right, r2.right)) or (self.isSameTree(r1.left, r2.right) and self.isSameTree(r1.right, r2.left))
    

r1 = TreeHelper.create_tree(['A','B','C','D','E', None, None])
r2 = TreeHelper.create_tree(['A','C','B',None,None,'D','E'])

sol = Solution()
assert sol.isSameTree(r1, r2) == True

r3 = TreeHelper.create_tree(['A','B','C','D','E', None, None])
r4 = TreeHelper.create_tree(['A','C','F',None,None,'D','E'])
assert sol.isSameTree(r3, r4) == False