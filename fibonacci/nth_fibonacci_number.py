


class Solution:


    def calculate_fibonacci(self, n) -> int:

        # 0th fibonacci number is 0
        if n == 0:
            return 0
        # 1st fibonacci number is 1
        if n == 1:
            return 1

        if n == 2:
            return 1

        return self.calculate_fibonacci(n-1) + self.calculate_fibonacci(n-2)

    
    def calculate_fibonacci_dp(self, n) -> int:

        if n < 2:
            return n

        n1, n2 = 0, 1

        for i in range(2, n+1):
            temp = n1 + n2
            n1, n2 = n2, temp

        return n2

    
sol = Solution()
assert sol.calculate_fibonacci(0) == 0
assert sol.calculate_fibonacci(1) == 1
assert sol.calculate_fibonacci(2) == 1
assert sol.calculate_fibonacci(5) == 5
assert sol.calculate_fibonacci(6) == 8

assert sol.calculate_fibonacci_dp(0) == 0
assert sol.calculate_fibonacci_dp(1) == 1
assert sol.calculate_fibonacci_dp(2) == 1
assert sol.calculate_fibonacci_dp(5) == 5
assert sol.calculate_fibonacci_dp(6) == 8


        