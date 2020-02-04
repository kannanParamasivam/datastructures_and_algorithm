'''
Merge Sort -  Divide and conqure with recursion with back tracking
'''

from typing import List
from math import ceil


class MergeSort:


    def sort(self, nums):
        return self.merge_sort(nums)


    def merge_sort(self, nums):

        if len(nums) <= 1:
            return nums

        mid_point = len(nums) // 2

        left_list = nums[:mid_point]
        right_list = nums[mid_point:]

        left_list = self.merge_sort(left_list)
        right_list = self.merge_sort(right_list)

        return self.merge(left_list, right_list)


    def merge(self, left_list, right_list):
        lp = 0
        rp = 0
        res = []

        while lp < len(left_list) and rp < len(right_list):

            if(left_list[lp] <= right_list[rp]):
                res.append(left_list[lp])
                print(f'{left_list[lp]} {right_list[rp]}')
                lp += 1
            elif(right_list[rp] < left_list[lp]):
                res.append(right_list[rp])
                print(f'{right_list[rp]} {left_list[lp]}')
                rp += 1

        if lp < len(left_list):
            while lp < len(left_list):
                res.append(left_list[lp])
                
                lp += 1

        if rp < len(right_list):
            while rp < len(right_list):
                res.append(right_list[rp])
                rp += 1

        return res


nums = [3, 2, 1, 5, 6, 4]
print(nums)
ms = MergeSort()
print(ms.sort(nums))
