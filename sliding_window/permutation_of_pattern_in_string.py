'''
567. Permutation in String
Medium

2039

75

Add to List

Share
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Constraints:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
'''

from collections import defaultdict


class Solution:
    
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        s1_freq = [0]*26
        
        for c in s1:
            s1_freq[ord(c)-ord('a')] += 1
            
        s2_window_freq = [0]*26
        window_start = 0
        window_size = len(s1)
        
        for window_end in range(len(s2)):
            
            right_char = s2[window_end]
            s2_window_freq[ord(right_char)-ord('a')] += 1
            
            while (window_end - window_start + 1) > window_size:
                left_char = s2[window_start]
                s2_window_freq[ord(left_char)-ord('a')] -= 1
                window_start += 1
                
            if (window_end - window_start + 1) == window_size and s1_freq == s2_window_freq:
                return True
            
        return False


sol = Solution()
print(sol.checkInclusion('ab','eidbaooo'))
        
        
            
        
        