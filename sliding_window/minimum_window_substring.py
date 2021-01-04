    from collections import defaultdict
    from typing import List
    from math import inf


    class Solution:

        
        def minWindow(self, s: str, t: str) -> str:
            
            window_start = 0
            char_freq = defaultdict(int)
            min_len = inf
            substring_start = 0
            matched = 0
            
            for c in t:
                char_freq[c] += 1
                
            for window_end in range(len(s)):
                
                right_char = s[window_end]
                
                if right_char in char_freq:
                    char_freq[right_char] -= 1
                    if char_freq[right_char] >= 0:
                        matched +=1
                    
                while matched == len(t):
                    
                    if min_len > (window_end - window_start + 1):
                        min_len = (window_end - window_start) + 1
                        substring_start = window_start
                    
                    left_char = s[window_start]
                    
                    if left_char in char_freq:
                        
                        if char_freq[left_char] == 0:
                            matched -= 1
                            
                        char_freq[left_char] += 1
                        
                    window_start += 1
            
            if min_len == inf:
                return ""
            
            return s[substring_start:substring_start+min_len]


    sol = Solution()
    print(sol.minWindow('ADOBECODEBANC', 'ABC'))
                    
            