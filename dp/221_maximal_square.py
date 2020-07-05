'''
221. Maximal Square
Medium

3035

76

Add to List

Share
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''


from typing import List


class Solution:


    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        if not matrix or not matrix[0]:
            return 0
        
        dp_memo: List[List[int]] = [[0] * len(matrix[row]) for row in range(len(matrix))]
        max_square = -1
        
        for row in range(len(matrix)):
            
            for col in range(len(matrix[row])):
                
                dp_memo[row][col] = min(self.get_value(dp_memo, row, col - 1),
                                        self.get_value(dp_memo, row - 1, col - 1),
                                        self.get_value(dp_memo, row - 1, col)) + 1 if matrix[row][col] == '1' else 0
                
                max_square = max(max_square, dp_memo[row][col])
                
        return max_square ** 2
    
    
    def get_value(self, matrix, row, col) -> int:
        
        if 0 <= row < len(matrix) and 0 <= col < len(matrix[row]):
            return int(matrix[row][col])
        else:
            return 0
        
            




matrix = [
            ['1', '0', '1', '0', '0'],
            ['1', '0', '1', '1', '1'],
            ['1', '1', '1', '1', '1'],
            ['1', '0', '0', '1', '0']
         ]

sol = Solution()
assert(sol.maximalSquare(matrix) == 4)
