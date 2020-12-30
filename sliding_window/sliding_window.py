'''
Find averages of Contiguous subarrays of size K
'''


from typing import List


class Solution:


    def find_average_of_subarrays(self, K: int, arr: List[int]) -> List[int]:

        if not arr:
            return

        if not K:
            return 

        window_start, window_sum, result = 0, 0, []

        for window_end in range(len(arr)):

            window_sum += arr[window_end]

            if window_end >= K-1:
                result.append(window_sum/K)
                window_sum -= arr[window_start]
                window_start += 1

        return result


sol = Solution()
print(sol.find_average_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]))

