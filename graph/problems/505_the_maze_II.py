'''
505. The Maze II
Medium

539

24

Add to List

Share
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

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

Output: 12

Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1

Explanation: There is no way for the ball to stop at the destination.



Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
Accepted
43,779
Submissions
93,471
'''
from typing import List
from collections import deque, namedtuple

CurPosDetail = namedtuple('CurPosDetail', ('depth', 'pos'))


class Solution:

	def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

		self.visited = set()

		if not maze or len(maze) == 0 or len(maze[0]) == 0 or self.is_wall(maze, tuple(start)):
			return -1

		bfs_queue = deque()
		bfs_queue.append(CurPosDetail(depth=0, pos=tuple(start)))

		while len(bfs_queue) > 0:

			cur_pos: CurPosDetail = bfs_queue.popleft()

			if cur_pos.pos not in self.visited:
				self.visited.add(cur_pos.pos)

				if cur_pos.pos == tuple(destination):
					if self.is_surrounded_by_walls(maze, cur_pos.pos):
						return cur_pos.depth
					else:
						return -1

				bfs_queue.extend([CurPosDetail(depth=cur_pos.depth + 1, pos=pos)
									for pos in self.get_neighbor_pos(cur_pos.pos) if not self.is_wall(maze, pos)])

		return -1


	def is_wall(self, maze: List[List[int]], pos: tuple) -> bool:
		return False if pos not in self.visited and 0 <= pos[0] < len(maze) and 0 <= pos[1] < len(maze[0]) and maze[pos[0]][pos[1]] == 0 else True


	def is_surrounded_by_walls(self, maze: List[List[int]], pos: tuple) -> bool:
		n_poses = self.get_neighbor_pos(pos)
		return all(map(lambda n_pos:self.is_wall(maze, n_pos), n_poses))


	def get_neighbor_pos(self, pos) -> List:
		n_offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]
		return list(map(lambda n_offset: tuple(sum(x) for x in zip(pos, n_offset)), n_offsets))


sol: Solution = Solution()
maze = [[0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]

start = [0,4]
# destination = [4,4]
destination = [3,2]

print(sol.shortestDistance(maze=maze, start=start, destination=destination))

