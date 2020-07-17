'''
283. Move Zeroes
Easy

3315

110

Add to List

Share
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

from typing import List


class Solution:


	def moveZeroes(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""

		if not nums:
			return

		l = len(nums)
		zero_count = 0

		for i in range(l):

			if nums[i] == 0:
				zero_count += 1
			elif zero_count > 0:
				nums[i-zero_count] = nums[i]
				nums[i] = 0



sol = Solution()
lst = [0,1,0,3,12]
#lst = [1]
sol.moveZeroes(lst)
print(lst)
