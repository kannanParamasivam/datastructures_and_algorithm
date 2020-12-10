'''
Given a stair with 'n' steps, implement a method to find howmany ways to reach top of the stairs, given that, at every step you can either take
1 step, 2 steps or 3 steps 
'''

class Solution:


    def count_ways(self, n: int) -> int:

        if n == 0:
            return 1

        if n == 1:
            return 1

        if n == 2:
            return 2

        one_step = self.count_ways(n-1)
        two_steps = self.count_ways(n-2)
        three_steps = self.count_ways(n-3)

        return one_step + two_steps + three_steps

    
    def count_ways_dp(self, n) -> int:

        if n == 0:
            return 1

        if n == 1:
            return 1

        if n == 2:
            return 2

        n1, n2, n3 = 1, 1, 2

        for i in range(3, n+1):
            temp = n1 + n2 + n3
            n1, n2, n3 = n2, n3, temp

        return n3

    
sol = Solution()
assert sol.count_ways(3) == 4 #{1,1,1} {2,1} {1,2} {3}
assert sol.count_ways(4) == 7

assert sol.count_ways_dp(3) == 4 #{1,1,1} {2,1} {1,2} {3}
assert sol.count_ways_dp(4) == 7