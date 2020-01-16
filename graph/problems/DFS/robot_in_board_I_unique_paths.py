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
        self.n = n
        self.m = m
        self.bottom = (1,0)
        self.right = (0,1)
        self.no_paths = 0
        
        self.dfs((0,0))
        return self.no_paths
        
    
    def dfs(self, node):
        
        row, col = node
        
        if row >= self.n or col >= self.m:
            return
        
        if node == (self.n-1,self.m-1):
            self.no_paths += 1
            return
        
        self.dfs(tuple(sum(x) for x in zip(node,self.bottom)))
        self.dfs(tuple(sum(x) for x in zip(node, self.right)))
    

sol = Solution()
print(sol.uniquePaths(7,3))
print(sol.uniquePaths(3,2))