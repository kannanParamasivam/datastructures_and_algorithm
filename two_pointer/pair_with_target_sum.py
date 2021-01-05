'''
Given an array of sorted numbers and a target sum find a parir in the array whose sum is equal to the given target.

Write a function to return the indices of the two number such that they add up to the given target.
'''

from typing import List


class Solution:

    def pair_with_target_sum(self, arr: List[int], target_sum: int) -> List[int]:

        left_ptr = 0
        right_ptr = len(arr) - 1

        while left_ptr < right_ptr:

            left_val = arr[left_ptr]
            right_val = arr[right_ptr]
            s = left_val + right_val

            if s == target_sum:
                return [left_ptr, right_ptr]
            elif s < target_sum:
                left_ptr += 1
            elif s > target_sum:
                right_ptr -= 1

        return [-1, -1]



sol = Solution()
print(sol.pair_with_target_sum(arr=[1, 2, 3, 4, 6], target_sum=6))
print(sol.pair_with_target_sum(arr=[2, 5, 9, 11], target_sum=11))
