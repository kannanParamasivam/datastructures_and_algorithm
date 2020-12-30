'''
Gven an array find sum of any contiguous sub array of size K.

'''


from math import inf
from typing import List


class Solution:


    def max_sub_array_sum(self, arr: List[int], K: int) -> int:

        if not arr:
            return -1

        if not K:
            return -1

        max_sum = -inf
        window_start = 0
        window_sum = 0

        for window_end in range(len(arr)):

            window_sum += arr[window_end]

            if window_end >= K-1:
                max_sum = max(max_sum, window_sum)
                window_sum -= arr[window_start]
                window_start += 1

        return max_sum 


sol = Solution()
print(sol.max_sub_array_sum([2,1,5,1,3,2], 3))