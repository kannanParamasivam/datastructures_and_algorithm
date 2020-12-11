'''
Given an array of number which represents the fee you need to pay to reach there. You can tak 1, 2 or 3 steps
'''

from typing import List
import math


class Solution:


    def jump_with_min_fee(self, fee: List[int]) -> int:

        if not fee:
            return 0

        if len(fee) == 1:
            return fee[0]

        dp = [math.inf] * (len(fee) + 1)

        dp[0] = 0
        dp[1] = fee[0]
        dp[2] = fee[0]

        for i in range(3, len(fee)+1):

            dp[i] = min(dp[i-3] + fee[i-3], dp[i-2] + fee[i-2], dp[i-1] + fee[i-1])

        return dp[-1]


sol = Solution()
print(sol.jump_with_min_fee([1, 2, 5, 2, 1, 2]))