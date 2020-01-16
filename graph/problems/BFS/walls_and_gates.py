'''
286. Walls and Gates

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
  '''

from typing import List
from collections import deque
from pprint import pprint


class Solution:

    
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = deque()

        "Find Gates and add it to queue with distance 0"
        for rpos, r in enumerate(rooms):
            for cpos, c in enumerate(r):
                if rooms[rpos][cpos] == 0:
                    queue.append((rpos, cpos, 0))

        nformulas = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        level = 0
        INF = pow(2, 31) - 1

        "Update neighbor empty rooms with distance from gate"
        while len(queue) > 0:
            gr, gc, level = queue.popleft()

            for nformula in nformulas:
                nr, nc = tuple(sum(x) for x in zip((gr, gc), nformula))

                if nr >= 0 and nr < len(rooms) and nc >= 0 and nc < len(rooms[nr]) and rooms[nr][nc] == INF:

                    rooms[nr][nc] = level+1
                    queue.append((nr, nc, level+1))


rooms = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647]
]

sol = Solution()
sol.wallsAndGates(rooms)
pprint(rooms)
