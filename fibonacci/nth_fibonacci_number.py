


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

    
sol = Solution()
assert sol.calculate_fibonacci(0) == 0
assert sol.calculate_fibonacci(1) == 1
assert sol.calculate_fibonacci(2) == 1
assert sol.calculate_fibonacci(5) == 5
assert sol.calculate_fibonacci(6) == 8


        