'''
Given 2 lists a and b. Each element is a pair of integers where the first integer represents the unique id and the second integer represents a value. Your task is to find an element from a and an element form b such that the sum of their values is less or equal to target and as close to target as possible. Return a list of ids of selected elements. If no pair is possible, return an empty list.

Example 1:

Input:
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7

Output: [[2, 1]]

Explanation:
There are only three combinations [1, 1], [2, 1], and [3, 1], which have a total sum of 4, 6 and 8, respectively.
Since 6 is the largest sum that does not exceed 7, [2, 1] is the optimal pair.
Example 2:

Input:
a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10

Output: [[2, 4], [3, 2]]

Explanation:
There are two pairs possible. Element with id = 2 from the list `a` has a value 5, and element with id = 4 from the list `b` also has a value 5.
Combined, they add up to 10. Similarily, element with id = 3 from `a` has a value 7, and element with id = 2 from `b` has a value 3.
These also add up to 10. Therefore, the optimal pairs are [2, 4] and [3, 2].
Example 3:

Input:
a = [[1, 8], [2, 7], [3, 14]]
b = [[1, 5], [2, 10], [3, 14]]
target = 20

Output: [[3, 1]]
Example 4:

Input:
a = [[1, 8], [2, 15], [3, 9]]
b = [[1, 8], [2, 11], [3, 12]]
target = 20

Output: [[1, 3], [3, 2]]
'''
from typing import List
from sys import maxsize

class Solution:

    def closest_pairs_to_target(self, a:List[List], b:List[List], target:int):

        a.sort(key=lambda x: x[1]) # sort list by second element in pair
        b.sort(key=lambda x: x[1]) # sort list by second element in pair

        ptr_a = 0
        ptr_b = len(b) -1

        diff = maxsize
        res_ptr_a = 0
        res_ptr_b = 0

        res = []

        while ptr_a < len(a):
            sum = a[ptr_a][1] + b[ptr_b][1]

            if sum <= target:
                if sum == target:
                    res.append([a[ptr_a][0],b[ptr_b][0]])
                
                if target - sum <= diff:
                    diff = target - sum
                    res_ptr_a = ptr_a
                    res_ptr_b = ptr_b
                    ptr_a += 1
            else:
                if ptr_b > 0:
                    ptr_b -= 1
                else:
                    break

        return res if len(res) > 0 else [[a[res_ptr_a][0],[res_ptr_b][0]]]


sol = Solution()
print(sol.closest_pairs_to_target(a=[[1, 3], [2, 5], [3, 7], [4, 10]], b=[[1, 2], [2, 3], [3, 4], [4, 5]], target=10))

                 
