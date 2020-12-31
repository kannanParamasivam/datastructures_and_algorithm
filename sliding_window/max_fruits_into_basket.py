'''
904. Fruit Into Baskets
Medium

1045

1514

Add to List

Share
In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?
'''


from typing import List
from collections import defaultdict
from math import inf


class Solution:

    
    def totalFruit(self, tree: List[int]) -> int:
        
        if not tree:
            return -1
        
        window_start = 0
        
        fruit_freq = defaultdict(int)
        max_fruits = -inf
        
        
        
        for window_end in range(len(tree)):
            
            fruit_freq[tree[window_end]] += 1
            
            if len(fruit_freq) <= 2:
                max_fruits = max(max_fruits, window_end - window_start + 1)
            
            while len(fruit_freq) > 2:
                
                fruit_freq[tree[window_start]] -= 1
                
                if fruit_freq[tree[window_start]] <= 0:
                    del fruit_freq[tree[window_start]]
                
                window_start += 1
                
        if max_fruits == -inf:
            return 0
        
        return max_fruits


sol = Solution()
print(sol.totalFruit([1,2,1]))
print(sol.totalFruit([0,1,2,2]))



        
        