'''
202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:

Input: n = 2
Output: false
'''


class Solution:

    
    def isHappy(self, n: int) -> bool:
        
        slow, fast = self.find_square_sum(n), self.find_square_sum(self.find_square_sum(n))
        
        while slow != fast:
            slow = self.find_square_sum(slow)
            fast = self.find_square_sum(self.find_square_sum(fast))
        
        return True if slow == 1 else False
    
    
    def find_square_sum(self, n: int) -> int:
        
        _sum = 0
        
        while n > 0:
            digit = n%10
            _sum += digit * digit
            n = n//10
        
        return _sum


sol = Solution()
print(sol.isHappy(19))
print(sol.isHappy(2))
print(sol.isHappy(23))
print(sol.isHappy(12))

            
            
            
        
        
        