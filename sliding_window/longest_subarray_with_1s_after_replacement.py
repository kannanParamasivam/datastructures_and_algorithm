from typing import List
from math import inf


class Solution:
    
    
    def longestOnes(self, A: List[int], K: int) -> int:
        
        window_start = 0
        window_1s = 0
        max_len = -inf
        
        for window_end in range(len(A)):
            
            left_char = A[window_end]
            
            if left_char == 1:
                window_1s += 1
                
            while (((window_end - window_start) + 1) - window_1s) > K:
                left_char = A[window_start]
                
                if left_char == 1:
                    window_1s -= 1
                    
                window_start += 1
                    
            max_len = max(max_len, window_end - window_start + 1)
            
        if max_len == -inf:
            return -1
        
        return max_len


sol = Solution()
print(sol.longestOnes([0,1,1,0,0,0,1,1,0,1,1], 2))
        