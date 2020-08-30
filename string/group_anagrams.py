from collections import defaultdict
from typing import List


class Solution:
    
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if not strs:
            return
        
        d = defaultdict(list)
        
        for s in strs:
            k = self.get_code(s)
            d[k].append(s)
         
        res = [val for _, val in d.items()]
        
        return res
    
    
    def get_code(self, s):
        
        l = [0]*26
        
        for c in s:
            l[ord(c) - ord('a')] += 1
            
        return ''.join([str(n) for n in l])
            

sol = Solution()
print(sol.groupAnagrams(["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod","aha","nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"]))