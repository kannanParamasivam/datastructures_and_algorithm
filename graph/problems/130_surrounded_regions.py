'''
130. Surrounded Regions
Medium

1297

576

Add to List

Share
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Accepted
196,036
Submissions
757,537
'''

from typing import List
from collections import deque
from pprint import pprint


class Solution:


    def solve(self, board: List[List[str]]) -> None:

        if not board or len(board) == 0 or len(board[0]) == 0:
            return

        n_rows, n_cols = (len(board), len(board[0]))

        bfs_queue = deque()
        visited = set()

        # append O's in top and bottom border to '-'

        for row in [0, len(board) - 1]:

            bfs_queue.extend([(row, col)
                              for col in range(n_cols) if board[row][col] == 'O'])

		# append O's in left and right border to '-'
        if n_rows > 1:

            for row in range(1, len(board) - 1):

                bfs_queue.extend(
                    [(row, col) for col in [0, n_cols - 1] if board[row][col] == 'O'])

		# Do bfs and update adjacent cells of '-' to '-'
        self.bfs(board, bfs_queue, visited)

		# Update remaining 'O' to 'X' and
        for row in range(1, n_rows-1):
            for col in range(n_cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'

		# Update '-' back to 'O'
        for pos in visited:
            board[pos[0]][pos[1]] = 'O'


    def bfs(self, board: List[List[str]], bfs_queue: deque, visited: set):

        while len(bfs_queue) > 0:

            cur_pos = bfs_queue.popleft()
            visited.add(cur_pos)

            if self.is_valid(board, cur_pos, visited):
                board[cur_pos[0]][cur_pos[1]] = '-'

            bfs_queue.extend([n_pos for n_pos in [(cur_pos[0] + 1, cur_pos[1]), (cur_pos[0] - 1, cur_pos[1]), (cur_pos[0], cur_pos[1] + 1),
                                                  (cur_pos[0], cur_pos[1] - 1)] if self.is_valid(board, n_pos, visited) and n_pos not in visited])

    def is_valid(self, board: List[List[str]], pos: tuple, visited: set) -> bool:
        return True if 0 <= pos[0] < len(board) and 0 <= pos[1] < len(board[0]) and board[pos[0]][pos[1]] == 'O' else False


sol: Solution = Solution()
board = [[X, X, X, X],
         [X, O, O, X],
         [X, X, O, X],
         [X, O, X, X]]

