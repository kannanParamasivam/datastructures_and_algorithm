

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