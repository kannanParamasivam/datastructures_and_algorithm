'''
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
'''

from typing import List

class Solution:
    
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board:
            return

        board_copy = [row[:] for row in board]

        neighbors = [(0,-1),(0,1),(-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1)]

        for row in range(len(board_copy)):

            if not board_copy[row]:
                continue

            for col in range(len(board_copy[row])):

                neighbor_total = 0

                for x, y in neighbors:
                    
                    n_r , n_c = x+row, y+col

                    if n_r < len(board_copy) and n_r >= 0 and n_c < len(board_copy[row]) and n_c >= 0:

                        neighbor_total += board_copy[n_r][n_c]

                if board_copy[row][col] == 0 and neighbor_total == 3:
                    board[row][col] = 1
                elif board_copy[row][col] == 1 and neighbor_total in {2,3}:
                    continue
                else:
                    board[row][col] = 0

sol = Solution()
life_board = [
    [0,1,0],
    [0,0,1],
    [1,1,1],
    [0,0,0]
]

sol.gameOfLife(life_board)

print(life_board)


                    
                    


        