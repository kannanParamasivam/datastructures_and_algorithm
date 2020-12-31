'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


from math import inf
from typing import List


class Solution:

    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        
        window_start = 0
        char_pos = {}
        max_len = -inf
        
        for window_end in range(len(s)):
            
            
                
            if s[window_end] in char_pos:
                #cur_len = window_end - window_start
                #max_len = max(max_len, cur_len)
                
                while s[window_end] in char_pos and window_start <= char_pos[s[window_end]]:
                    del char_pos[s[window_start]]
                    window_start += 1
                    
                #char_pos[s[window_end]] = window_end
                
            char_pos[s[window_end]] = window_end
            cur_len = window_end - window_start + 1
            max_len = max(max_len, cur_len)
        
        if max_len == -inf:
            return 0
        
        return max_len
                
        