from typing import List


class Solution:

    
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        if len(nums) == 1:
            return 1
        
        non_dupe_ptr, i = 0, 1
        
        while i < len(nums):
            
            if nums[non_dupe_ptr] != nums[i]:
                nums[non_dupe_ptr + 1] = nums[i]
                non_dupe_ptr += 1
        
            i += 1
            
        return non_dupe_ptr + 1
        

sol = Solution()
print(sol.removeDuplicates([2, 3, 3, 3, 6, 9, 9]))
print(sol.removeDuplicates([2, 2, 2, 11]))