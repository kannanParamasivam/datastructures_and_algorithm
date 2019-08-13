from typing import List, Tuple, Dict, TextIO


class TwoSum:
    
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """find two numbers yield sum in O(n)"""

        if nums == None or len(nums) <= 0:
            return []
        
        s = set()

        for i in iter(nums):
            
            diff = target - i
            
            if diff in s:
                return [i, diff]
            
            s.add(i)
        
        raise Exception('item not found')
