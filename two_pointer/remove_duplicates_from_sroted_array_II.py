'''
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.
'''

from typing import List


class Solution:

    
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        if len(nums) == 1:
            return 1
        
        no_dup_ptr, i = 0, 1
        same = 0
        
        while i < len(nums):
            
            if i < len(nums) and nums[i] == nums[i-1] and same < 1:
                same += 1
                nums[no_dup_ptr + 1] = nums[i]
                no_dup_ptr += 1
                i += 1
                continue
            
            if nums[no_dup_ptr] != nums[i]:
                nums[no_dup_ptr + 1] = nums[i]
                no_dup_ptr += 1
                same = 0
                
            i += 1

        print(nums[:no_dup_ptr + 1])
        
        return no_dup_ptr + 1


sol = Solution()
print(sol.removeDuplicates([1,1,1,2,2,3]))
print(sol.removeDuplicates([0,0,1,1,1,1,2,3,3]))



