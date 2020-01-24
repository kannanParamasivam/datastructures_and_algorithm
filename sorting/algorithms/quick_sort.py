'''
    Quick Sort is divide and conqure algorithm
'''
from typing import List


class QuickSort:


    def sort(self, nums):
        self.quickSort(nums, 0, len(nums)-1)
    

    def quickSort(self, nums, l , h):

        if l < h:
            pivot = self.partition(nums, l, h)
            self.quickSort(nums, l, pivot - 1)
            self.quickSort(nums, pivot + 1, h)


    def partition(self, nums, l, h)->int:
        pivot_value = nums[l]
        i = l + 1
        j = h

        while i <= j:

            while i <= j and nums[i] <= pivot_value:
                i += 1
            
            while j >= i and nums[j] >= pivot_value:
                j -= 1

            if i < j:
                self.swap(nums, i, j)
            
        self.swap(nums, l, j)

        return j

    
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp




            

nums = [3,2,1,5,6,4]
print(nums)
qs = QuickSort()
qs.sort(nums)
print(nums)


