from typing import List


'''
581. Shortest Unsorted Continuous Subarray
Medium

3357

164

Add to List

Share
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

 

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0
'''

from math import inf

class Solution:
    
    
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        
        left = 0
        
        #find left unsorted pos
        while left < len(nums) - 1:
            
            if nums[left] > nums[left + 1]:
                break
                
            left += 1
                
        # find right unsotred position
        right = len(nums) - 1
        
        while right > 0:
            
            if nums[right] < nums[right - 1]:
                break
                
            right -= 1
            
        if left >= right:
            return 0
        
        # find min and max of window
        win_min, win_max = inf, -inf
        
        for i in range(left, right + 1):
            
            win_min = min(win_min, nums[i])
            win_max = max(win_max, nums[i])
        
        
        # expand window left and check for greater than win_min
        
        i = left
        
        while i >= 0:
            
            if nums[i] > win_min:
                left = i
                
            i -= 1
            
        # expand window right and check for less than win_max
        
        i = right
        
        while i < len(nums):
            
            if nums[i] < win_max:
                right = i
                
            i += 1
            
        return (right - left) + 1


sol = Solution()
print(sol.findUnsortedSubarray(nums=[2,6,4,8,10,9,15]))
print(sol.findUnsortedSubarray(nums=[1,2,3,4]))
print(sol.findUnsortedSubarray(nums=[1]))
print(sol.findUnsortedSubarray(nums=[1,2,4,3,-1,2,2,2]))
        
    