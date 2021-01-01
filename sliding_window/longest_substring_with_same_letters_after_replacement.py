from typing import List
from collections import defaultdict
from math import inf


class Solution:

    
    def characterReplacement(self, s: str, k: int) -> int:
        
        if not s:
            return -1
        
        window_start = 0
        window_char_freq = defaultdict(int)
        window_max_freq = -inf
        max_len = -inf
        
        for window_end in range(len(s)):
            
            right_char = s[window_end]
            window_char_freq[right_char] += 1
            window_max_freq = max(window_max_freq, window_char_freq[right_char])
            
            while (window_end - window_start + 1) - window_max_freq > k:
                left_char = s[window_start]
                window_char_freq[left_char] -= 1
                window_start += 1
                #window_max_freq = max(window_max_freq, window_char_freq[left_char])
                
            max_len = max(max_len, window_end -  window_start + 1)
         
        
        if max_len == -inf:
            return -1
        
        return max_len


sol = Solution()
print(sol.characterReplacement('aabccbb', 2))
print(sol.characterReplacement('abbcb', 1))
print(sol.characterReplacement('abccde', 1))


                
            
            
            
            
            
        
        