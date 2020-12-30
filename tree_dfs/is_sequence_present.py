from helpers import Node, TreeHelper
from typing import List


class Solution:

    def is_path_present(self, nums:List[int], root: Node) -> bool:
 
        if not root and not nums:
            return True
        elif not root:
            return False

        res = self.is_path_present_rec(root, nums)
        print(res)

    
    def is_path_present_rec(self, root, nums) -> bool:

        if not root:
            return False

        if not root.left and not root.right and len(nums) == 1 and nums[0] ==  root.val:
            return True

        if root.val == nums[0]:
            num = nums.pop(0)
            is_present = self.is_path_present_rec(root.left, nums) or self.is_path_present_rec(root.right, nums)
            nums.insert(0,num)
            return is_present
        else:
            return False

        
sol: Solution = Solution()

root:Node = TreeHelper.create_tree([5,2,3,1,4,None,None,None,None,6,8])
TreeHelper.print_tree(root)

sol.is_path_present([5,2,4,8], root)
sol.is_path_present([5, 3, 4, 9], root)


