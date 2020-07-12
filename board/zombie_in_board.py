'''
Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour. Find out how many hours does it take to infect all humans?

Example:

Input:
[[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]

Output: 2

Explanation:
At the end of the 1st hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [0, 1, 0, 1, 1],
 [1, 1, 1, 0, 1]]

At the end of the 2nd hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1]]
'''
from typing import List
from queue import deque
from collections import namedtuple

Zombie = namedtuple('Zombie', ['position', 'gen'])


class Solution:


    def min_hours(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return 0

        q = deque()

        for row in range(len(grid)):

            for col in range(len(grid[row])):

                if grid[row][col] == 1:
                    q.append(Zombie((row, col), 0))

        n_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_gen = 0

        while len(q) > 0:

            pos, gen = q.popleft()

            for offset in n_offsets:

                row = offset[0] + pos[0]
                col = offset[1] + pos[1]

                if 0 <= row < len(grid) and 0 <= col < len(grid[row]) and grid[row][col] == 0:
                    grid[row][col] = 1
                    q.append((Zombie(row, col), gen + 1))
                    max_gen = max(max_gen, gen+1)

        return max_gen


sol = Solution()
result = sol.min_hours(grid=[[0, 1, 1, 0, 1],
                    [0, 1, 0, 1, 0],
                    [0, 0, 0, 0, 1],
                    [0, 1, 0, 0, 0]])

print(result)
