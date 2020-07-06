'''
394. Decode String
Medium

3085

161

Add to List

Share
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
'''

class Solution(object):
    
    
    def decodeString(self, s):
        
        if not s:
            return None
        
        stack = []
        cur_str = ""
        cur_num:int = 0
        
        for c in s:
            
            if c == '[':
                stack.append(cur_str)
                stack.append(cur_num)
                cur_str = ''
                cur_num = 0
            
            elif c == ']':
                
                cur_str = cur_str * stack.pop()
                cur_str = stack.pop() + cur_str
                
            elif c.isdigit():
                cur_num = cur_num * 10 + int(c)                
            else:
                cur_str += c
        
        return cur_str
    
sol = Solution()
assert(sol.decodeString('2[abc]3[cd]ef') == 'abcabccdcdcdef')
assert(sol.decodeString('3[a2[c]]') == 'accaccacc')
assert(sol.decodeString('abc3[cd]xyz') == 'abccdcdcdxyz')
    

