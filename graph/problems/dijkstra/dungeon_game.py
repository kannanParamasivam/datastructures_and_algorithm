'''
174. Dungeon Game

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)
 

Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
'''

from queue import PriorityQueue
from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        if not dungeon or len(dungeon) == 0 or len(dungeon[0]) == 0:
            return 0
        
        q = PriorityQueue()
        visited = set()
        
        q.put((-dungeon[0][0], (0,0)))
        nbrs = [(0,1),(1,0)]
        
        while not q.empty():
            h, pos = q.get()
            h = -h
            r, c = pos
            
            if (r,c) in visited:
                continue
            else:
                visited.add((r,c))
            
            if r == len(dungeon)-1 and c == len(dungeon[len(dungeon) - 1]) - 1:
                res = 0
                if h < 0:
                    res = abs(h) + 1
                else:
                    res = 1
                
                if res <= abs(dungeon[0][0]) and dungeon[0][0] < 0:
                    res += abs(dungeon[0][0])
                
                return res
            
            for nbr in nbrs:
                nr, nc = tuple(sum(x) for x in zip(pos, nbr))
                
                if (nr, nc) not in visited and nr >= 0 and nr < len(dungeon) and nc >= 0 and nc < len(dungeon[nr]):
                    q.put((-(h + dungeon[nr][nc]), (nr, nc)))
                    
                    if nr == len(dungeon)-1 and nc == len(dungeon[len(dungeon) - 1]) - 1:
                        ht = (h + dungeon[nr][nc])
                        res = 0
                        if ht < 0:
                            res = abs(ht) + 1
                        else:
                            res = 1

                        if res <= abs(dungeon[0][0]) and dungeon[0][0] < 0:
                            res += abs(dungeon[0][0])
                
                        return res
                
                else:
                    continue

sol = Solution()
print(sol.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
print(sol.calculateMinimumHP([[100]]))
print(sol.calculateMinimumHP([[-3,5]]))
print(sol.calculateMinimumHP([[-1,1]]))
print(sol.calculateMinimumHP([[1,-2,3],[2,-2,-2]]))
            
            
        