'''
53. Maximum Subarray
Easy

6876

316

Add to List

Share
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''
from typing import List


class Solution:


	def maxSubArray(self, nums: List[int]) -> int:

		if not nums or len(nums) == 0:
			return 0

		max_sum = nums[0]
		l = len(nums)

		for i in range(1,l):
			nums[i] = max(nums[i], nums[i-1]+ nums[i])

			max_sum = nums[i] if nums[i] > max_sum else max_sum

		return max_sum



sol = Solution()
# res = sol.maxSubArray([10, -20, 35, 40, 10, -10, 100, -50])
res = sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(res)










