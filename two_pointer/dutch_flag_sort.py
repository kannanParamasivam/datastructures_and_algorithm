from typing import List


class Solution:


    def dutch_flag_sort(self, arr: List):

        if not arr:
            return arr

        left, right = 0, len(arr) - 1
        i:int = 0

        while i <= right:

            if arr[i] == 2:
                arr[i], arr[right] = arr[right], arr[i]
                right -= 1
            elif arr[i] == 0:
                arr[i], arr[left] = arr[left], arr[i]
                left += 1
            else:
                i += 1

        print(arr)


sol: Solution = Solution()
sol.dutch_flag_sort([1, 0, 2, 1, 0])
sol.dutch_flag_sort([2, 2, 0, 1, 2, 0])

    
            
            



