'''
62. Unique Paths
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.
(n rows and m columns)

Example 1:

Input: m = 3, n = 2
(2 rows and 3 columns)
Output: 3

Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:

Input: m = 7, n = 3
()
Output: 28
'''

class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        
        if m <= 0 or n<=0:
            return
        
        'n Rows and m columns'
        self.board = [[0]*m for i in range(n)]

        for rpos, row in enumerate(self.board):
            for cpos, col in enumerate(row):

                if rpos == 0 or cpos == 0:
                    self.board[rpos][cpos] = 1
                else:
                    ur, uc = tuple(sum(x) for x in zip((rpos, cpos),(-1,0)))
                    lr, lc = tuple(sum(x) for x in zip((rpos, cpos),(0,-1)))

                    self.board[rpos][cpos] = self.board[ur][uc] + self.board[lr][lc]

                if rpos == n-1 and cpos == m-1:
                    return self.board[rpos][cpos]

        return 0
        
    

sol = Solution()
print(sol.uniquePaths(3,2))
print(sol.uniquePaths(7,3))
