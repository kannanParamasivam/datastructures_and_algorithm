'''
how many number of ways to express n as sum of 1, 3, or 4
'''

from typing import List
from pprint import pprint


class RecursiveSolution:


    def num_ways(self, n) -> int:

        if n == 0:
            return 1 # no subtractions needed. Only one way to achieve 0

        if n == 1:
            return 1 # 1 can be achieved as one time 1

        if n == 2:
            return 1 # 2 can be achieved by adding 1 two times (1+1)

        if n == 3: # 3 can be achieved two ways which are by adding 1 3 times (1+1+1) and 3 1 time (3) 
            return 2

        one_ways = self.num_ways(n-1)
        three_ways = self.num_ways(n-3)
        four_ways = self.num_ways(n-4)

        return one_ways + three_ways + four_ways


class MemoRecursiveSolution:


    def num_ways(self, n) -> int:

        if n == 0:
            return 1

        if n == 1:
            return 1

        if n == 2:
            return 1

        if n == 3:
            return 2

        memo = [-1 for _ in range(n+1)]
        memo[0], memo[1], memo[2], memo[3] = 1,1,1,2

        return self.rec(memo, n)

    
    def rec(self, memo, n) -> int:

        if memo[n] == -1:
            memo[n] = self.rec(memo, n-1) + self.rec(memo, n-3) + self.rec(memo, n-4)

        return memo[n]


class DPSolution:


    def num_ways(self, n) -> int:

        if n <= 2:
            return 1

        if n == 3:
            return 2

        dp = [-1 for _ in range(n+1)]

        dp[0], dp[1], dp[2], dp[3] = 1, 1, 1, 2

        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-3] + dp[i-4]

        return dp[n]


rec_sol = RecursiveSolution()
assert rec_sol.num_ways(4) == 4
# 4 = {1,1,1,1}, {3, 1}, {1, 3}, {4}
assert rec_sol.num_ways(5) == 6
# 6 = {1,1,1,1,1}, {1,1,3}, {1,3,1}, {3,1,1}, {4, 1}, {1, 4}

memo_rec_sol = MemoRecursiveSolution()
assert memo_rec_sol.num_ways(4) == 4
# 4 = {1,1,1,1}, {3, 1}, {1, 3}, {4}
assert memo_rec_sol.num_ways(5) == 6
# 6 = {1,1,1,1,1}, {1,1,3}, {1,3,1}, {3,1,1}, {4, 1}, {1, 4}

dp_sol = DPSolution()
assert dp_sol.num_ways(4) # == 4
# 4 = {1,1,1,1}, {3, 1}, {1, 3}, {4}
assert dp_sol.num_ways(5) #  == 6
# 6 = {1,1,1,1,1}, {1,1,3}, {1,3,1}, {3,1,1}, {4, 1}, {1, 4}


    

        
            