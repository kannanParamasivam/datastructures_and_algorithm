'''
Given a string S, we can split S into 2 strings: S1 and S2. Return the number of ways S can be split such that the number of unique characters between S1 and S2 are the same.

Example 1:

Input: "aaaa"
Output: 3
Explanation: we can get a - aaa, aa - aa, aaa- a
Example 2:

Input: "bac"
Output: 0
Example 3:

Input: "ababa"
Output: 2
Explanation: ab - aba, aba - ba
Looking back on this one I felt like I could've done better and got carried away about how easy I thought it was. I basically, looped from the second element to the second last element, had 2 sets, 1 for each half of the string. and then check if the size of the 2 sets are equal, if so increment a counter. The time complexity is O(n^2) since we have to iterate through the whole string to check of unique characters each time we split. and Space is O(n).
Is there a better way to do this?
'''

class Solution:
    
    def split_string(self, s: str):
        
        left_counter = [0]*26
        right_counter = [0]*26
        res = 0

        for c in s:
            right_counter[ord(c) - ord('a')] += 1
        
        for i in range(len(s)):
            left_counter[ord(s[i]) - ord('a')] += 1
            right_counter[ord(s[i]) - ord('a')] -= 1
            
            if self.get_count(left_counter) == self.get_count(right_counter):
                res += 1
                
        return res
        
            
    def get_count(self, arr:str):
        return sum(1 for x in arr if x>0)        
        
    
    
sol = Solution()
print(sol.split_string('ababa')) 
# print(sol.split_string('aaaa')) 
# print(sol.split_string('bac')) 