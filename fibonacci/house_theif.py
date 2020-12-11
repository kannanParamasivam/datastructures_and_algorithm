'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''

from typing import List
from time import time


class Solution:


    '''
    Recursive solution
    Time Complexity = O(2^n)
    Space Complexity = O(n)
    '''
    def recursive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        max_money = self.rob_rec(nums, len(nums)-1)

        return max_money

    
    def rob_rec(self, nums:List[int], cur_house) -> int:

        if cur_house == 0:
            return nums[cur_house]

        if cur_house == 1:
            return max(nums[0], nums[1])

        max_amount = max(nums[cur_house] + self.rob_rec(nums, cur_house - 2), self.rob_rec(nums, cur_house-1))

        return max_amount


    def recursive_with_memo(self, nums: List[int]) -> int:

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        memo = [-1] * len(nums)

        money: int = self.rob_rec_with_memo(nums, len(nums) - 1, memo)

        return money

    
    def rob_rec_with_memo(self, nums, cur_house, memo: List[int]) -> int:

        if cur_house == 0:
            return nums[0]

        if cur_house == 1:
            return max(nums[0], nums[1])

        if memo[cur_house] == -1:
            memo[cur_house] = max(nums[cur_house] + self.rob_rec_with_memo(nums, cur_house - 2, memo), self.rob_rec_with_memo(nums, cur_house - 1, memo))
        
        return memo[cur_house]

    
    def rob_dp(self, nums: List[int]) -> int:

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        n1 =  nums[0]
        n2 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            n1, n2 = n2, max(nums[i] + n1, n2)

        return n2


sol = Solution()
start_time = time()
assert sol.recursive([2,5,1,3,6,2,4]) == 15
assert sol.recursive([2,10,14,8,1]) == 18
print(time() - start_time)

start_time = time()
assert sol.recursive_with_memo([2,5,1,3,6,2,4]) == 15
assert sol.recursive_with_memo([2,10,14,8,1]) == 18
print(time() - start_time)

start_time = time()
assert sol.rob_dp([2,5,1,3,6,2,4]) == 15
assert sol.rob_dp([2,10,14,8,1]) == 18
print(time() - start_time)