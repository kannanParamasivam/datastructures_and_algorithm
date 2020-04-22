'''
733. Flood Fill
Easy

847

159

Add to List

Share
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
Accepted
99,748
Submissions
186,566
'''

from collections import deque
from typing import List
from pprint import pprint


class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        if not image or len(image) == 0 or len(image[0]) == 0 or not self.is_valid(image, (sr, sc)) or image[sr][sc] == newColor:
            return image

        bfs_queue = deque()
        bfs_queue.append((sr, sc))
        old_color = image[sr][sc]

        while len(bfs_queue) > 0:
            cur_pos = bfs_queue.popleft()
            image[cur_pos[0]][cur_pos[1]] = newColor

            for n_pos in [(cur_pos[0]-1, cur_pos[1]), (cur_pos[0]+1, cur_pos[1]), (cur_pos[0], cur_pos[1]-1), (cur_pos[0], cur_pos[1]+1)]:

                if self.is_valid(image, n_pos) and image[n_pos[0]][n_pos[1]] == old_color:
                    bfs_queue.append(n_pos)

        return image

    def is_valid(self, image: List[List[int]], pos: tuple) -> bool:
        return True if 0 <= pos[0] < len(image) and 0 <= pos[1] < len(image[0]) else False


sol = Solution()
image = [[1, 1, 1],
         [1, 1, 0],
         [1, 0, 1]]
sr = 1
sc = 1
newColor = 2

pprint(sol.floodFill(image = image, sr = sr, sc = sc, newColor = newColor))
