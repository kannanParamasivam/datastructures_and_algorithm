
'''
68. Text Justification
Hard

670

1566

Add to List

Share
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
'''

from typing import List
from pprint import pprint as pp
from queue import deque
from collections import Counter


class Solution:

    
    def minWindow(self, s: str, t: str) -> str:
        
        if not s or not t or len(s) < len(t):
            return ""
        
        if s == t:
            return s
        
        if len(t) == 1:
            for c in s:
                if c == t:
                    return t
            return ""
        
        count = Counter(t)
        window_count = {c:0 for c in t}
        q = deque()
        start , current = 0, 0
        result:str = ""
        
        # place start at first occurance of expected letters
        while start < len(s):
            if s[start] in window_count:
                current  = start + 1
                window_count[s[start]] += 1
                break
            start += 1
        
        while start < len(s) and current < len(s) and start < current:
            
            # match found at current position
            if s[current] in window_count:
                q.append(current)
                window_count[s[current]] += 1
                
                found_t = all(count[c] <= n for c,n in window_count.items())
                
                while found_t:
                    
                    start, current, result, s, q = self.udpate_res_move_start(count, window_count, start, current, result, s, q)
                    
                    found_t = all(count[c] <= n for c,n in window_count.items())
            
            current += 1
        
        return result
            
        
    def udpate_res_move_start(self, count, window_count, start, current, result, s, q):
        
        result = s[start : current + 1] if result == "" or (current - start) + 1 < len(result) else result
        # move start
        window_count[s[start]] -= 1
        start = q.popleft()

        # found_t = all(count[c] == n for c,n in window_count.items())
        
        return (start, current, result, s, q)
    

sol:Solution = Solution()
print(sol.minWindow("ADOBECODEBANC","ABC"))
# print(sol.minWindow("abc","bc"))
# print(sol.minWindow("bbaa","aba"))

                

            
            
        
        