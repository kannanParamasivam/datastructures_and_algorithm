from typing import List
from math import ceil, floor


class Solution:
    

    def find(self, data: List[int], key: int) -> bool:

        if not data:
            return False

        l, r = 0, len(data) - 1
       
        while l <= r:
            
            m = self.get_middle(l, r)
            
            if data[m] == key:
                return True
            
            if key < data[m]:
                r = m - 1
            
            if key > data[m]:
                l = m  + 1
        
        return False
        

    def get_middle(self, l: int, r: int) -> int:

        if l == r:
            return l

        return (l + r) // 2


sol = Solution()
assert sol.find([1, 2, 3, 4,6,7,9,10,11,12,13,14,15,16,17], 8) == False
assert sol.find([1, 2, 3, 4,6,7,9,10,11,12,13,14,15,16,17], 13) == True
assert sol.find([1], 1) == True
assert sol.find([1], 3) == False


