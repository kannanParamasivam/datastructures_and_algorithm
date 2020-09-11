'''
You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from the top-left corner of the map and can move one block up, down, left or right at a time. The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe. Output the minimum number of steps to get to the treasure.

Example:

Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.
'''
from typing import List


def find_min_steps(input: List[List[int]]) -> int:
    
    if not input or not len(input[0]):
        return 
    
    q = [(0,0,0)]
    offsets = [(0,-1),(0,1),(-1,0),(1,0)]
    
    while q:
        
        row, col, dist = q.pop(0)
        input[row][col] = '2'
        
        for n_r_o, n_c_o in offsets:
            
            n_r = row + n_r_o
            n_c = col + n_c_o
            
            if 0 <= n_r < len(input) and 0 <= n_c < len(input[0]) and input[n_r][n_c] not in {'D','2'}:
                
                if input[n_r][n_c] == 'X':
                    return dist + 1
                
                q.append((n_r, n_c, dist + 1))
                
    return -1
                

print(find_min_steps(
    [
 ['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']
 ])) 

print(find_min_steps(
    [
 ['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['D', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']
 ])) 
                
                
            
        
        