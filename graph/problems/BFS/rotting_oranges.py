'''
994. Rotting Oranges
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
'''

from collections import deque
from typing import List

class Solution:


    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()

        
        # find rotten oranches and append as level 0
        for row, r in enumerate(grid):
            for col, c in enumerate(r):
                
                if grid[row][col] == 2:
                    queue.append((row, col, 0))

        level = 0

        nbors = ((0,-1),(0,1),(-1,0),(1,0))

        # rotting adjacent oranches while tracking its rotting level (minute)
        while len(queue) > 0:
             r, c, level = queue.popleft()
             
             for nr, nc in nbors:
                nrow, ncol = tuple(sum(x) for x in zip((nr,nc), (r, c)))
                
                if nrow >= 0 and nrow< len(grid) and ncol >= 0 and ncol < len(grid[nrow]) and grid[nrow][ncol] == 1:
                    grid[nrow][ncol] = 2
                    queue.append((nrow, ncol, level+1))
        
        # check if there are any fresh oranches
        for row in grid:
            for orange in row:
                if orange == 1:
                    return -1

        return level


sol = Solution()
orange_grid1 = [[2,1,1],[1,1,0],[0,1,1]]
print(sol.orangesRotting(orange_grid1))

# orange_grid2 = [[2,1,1],[0,1,1],[1,0,1]]
# print(sol.orangesRotting(orange_grid2))

# orange_grid3 = [[0,2]]
# print(sol.orangesRotting(orange_grid3))



        

        