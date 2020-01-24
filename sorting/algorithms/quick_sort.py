'''
    Quick Sort is divide and conqure algorithm
    * In-Place sorting
    * Best time O(N log N)
    * Worst time O(N^2) if array is already sorted
'''
from typing import List


class QuickSort:


    def sort(self, nums):
        self.quickSort(nums, 0, len(nums)-1)
    

    def quickSort(self, nums, l , h):

        if l < h:
            # Partitiion and find privot
            pivot = self.partition(nums, l, h)
            self.quickSort(nums, l, pivot - 1)
            self.quickSort(nums, pivot + 1, h)


    
    def partition(self, nums, l, h):
        '''Move lower values to left of pivot and move higher values to right side of pivot'''
        # Take first element as Pivot
        pivot_value = nums[l]
        i = l + 1
        j = h

        while i <= j:
            # Find first larger number than pivot from left
            while i <= j and nums[i] <= pivot_value:
                i += 1
            
            #Find first smaller number from right
            while j >= i and nums[j] >= pivot_value:
                j -= 1

            # Move smaller number to left and larger number to right
            if i < j:
                self.swap(nums, i, j)

        # Move pivot to cutting place   
        self.swap(nums, l, j)

        # Return new pivot location
        return j

    
    def swap(self, nums, i, j):
        print(f'{nums[i]} {nums[j]}')
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp




            

nums = [3,2,1,5,6,4]
print(nums)
qs = QuickSort()
qs.sort(nums)
print(nums)


