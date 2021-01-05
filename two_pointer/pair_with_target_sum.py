'''
Given an array of sorted numbers and a target sum find a parir in the array whose sum is equal to the given target.

Write a function to return the indices of the two number such that they add up to the given target.
'''

from typing import List


class Solution:

    def pair_with_target_sum(self, arr: List[int], target_sum: int) -> List[int]:

        nums_dict = {}
        i = 0

        for i in range(len(arr)):
            num = arr[i]
            rem = target_sum - num

            if rem in nums_dict:
                return [i, nums_dict[rem]]

            nums_dict[num] = i


sol = Solution()
print(sol.pair_with_target_sum(arr=[1, 2, 3, 4, 6], target_sum=6))
print(sol.pair_with_target_sum(arr=[2, 5, 9, 11], target_sum=11))
