'''
130. Surrounded Regions
Medium

1196

546

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
'''

from typing import List
from collections import deque
from pprint import pprint


class Solution:

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.visited = set()
        self.queue = deque()

        if not board or len(board) <= 0:
            return

        for row in [0, len(board)-1]:
            for col in range(len(board[row])):
                if board[row][col] == 'O':
                    self.queue.append((row, col))

        for row in range(1, len(board)-1):

            if board[row][0] == 'O':
                self.queue.append((row, 0))

            if board[row][len(board[row])-1] == 'O':
                self.queue.append((row, len(board[row])-1))

        self.BFS(board)

        # pprint(board)

        for row in range(1, len(board)-1):
            for col in range(1, len(board[row])-1):
                if board[row][col] == 'O':
                    board[row][col] = 'X'

        for row, col in self.visited:
            board[row][col] = 'O'

        # pprint(board)

    def BFS(self, board):

        neighbor_offset = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        while len(self.queue) > 0:
            r, c = self.queue.popleft()
            self.visited.add((r, c))

            if board[r][c] == 'O':
                board[r][c] = 'E'

            for offset_location in neighbor_offset:

                n_r, n_c = (sum(x) for x in zip((r, c), (offset_location)))

                if n_r < len(board)
                and n_r >= 0
                and n_c < len(board[n_r])
                and n_c >= 0 and (n_r, n_c) not in self.visited
                and board[n_r][n_c] == 'O':
                    self.queue.append((n_r, n_c))


sol = Solution()
sol.solve(
    [['X', 'X', 'X', 'X'],
     ['X', 'O', 'O', 'X'],
     ['X', 'X', 'O', 'X'],
     ['X', 'O', 'X', 'X']]
)
