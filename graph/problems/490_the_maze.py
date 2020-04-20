'''
490. The Maze
Medium

663

70

Add to List

Share
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.



Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true

Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: false

Explanation: There is no way for the ball to stop at the destination.



Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
Accepted
57,432
Submissions
113,598
'''
from typing import List
from pprint import pprint


class Solution:

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        if not maze or len(maze) <= 0:
            return False

        return self.dfs(maze, start, destination)

    def dfs(self, maze, cur_pos, destination) -> bool:

        if self.is_wall(maze, cur_pos):
            return False

        if cur_pos == destination:
            if self.is_surrounded_by_walls(maze, cur_pos):
                return True
            else:
                return False

        # mark current position as wall
        maze[cur_pos[0]][cur_pos[1]] = 1

        found_destination = any(map(lambda pos: self.dfs(
            maze, pos, destination), self.get_neighbors(cur_pos)))

        if not found_destination:
            maze[cur_pos[0]][cur_pos[1]] = 0

        return found_destination

    def is_wall(self, maze, pos) -> bool:

        if 0 <= pos[0] < len(maze) and 0 <= pos[1] < len(maze[0]) and maze[pos[0]][pos[1]] != 1:
            return False
        else:
            return True

    def is_surrounded_by_walls(self, maze, pos) -> bool:

        # n_offsets = [(0,-1),(0,1),(1,0),(-1,0)]

        # n_positions = map(lambda n_offset: tuple(sum(x) for x in zip(n_offset,pos)), n_offsets)
        n_positions = self.get_neighbors(pos)

        for n_position in n_positions:
            if not self.is_wall(maze, n_position):
                return False

        return True

        # all(list(map(lambda n_pos:is_wall(n_pos),list(map(lambda n_offset: tuple(sum(x) for x in zip(n_offset, pos)),n_offsets)))))

    def get_neighbors(self, pos):
        n_offsets = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        return map(lambda n_offset: tuple(sum(x) for x in zip(n_offset, pos)), n_offsets)


sol = Solution()

# maze = [[0, 0, 1, 0, 0],
#         [0, 0, 0, 0, 0],
#         [0, 0, 0, 1, 0],
#         [1, 1, 0, 1, 1],
#         [0, 0, 0, 0, 0]]

# start = (0, 4)
# destination = (3, 2)
# # Expected answer is false

maze = [[0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]
start = (0, 4)
destination = (4, 4)

print(sol.hasPath(maze, start, destination))
