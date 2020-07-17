from typing import List
from pprint import pprint as pp


class Solution:
    
    
    def optimal_utilization(self, a: List[List[int]], b: List[List[int]], target: int) -> List[List[int]]:
        
        if not a or not b:
            return 
        
        a.sort(key=lambda x: x[1])
        b.sort(key=lambda x: x[1])
        
        pp(f'a after sorting {a}')
        pp(f'a after sorting {b}')
        
        max = 0
        res = []
        
        i, j = 0, len(b)-1
        
        while i < len(a) and j >= 0:
            
            s = a[i][1] + b[j][1]
            
            if s > target:
                j -= 1
            elif s > max:
                res.clear()
                res.append([a[i][0], b[j][0]])
                max = s
                i += 1
            elif s == max:
                res.append([a[i][0], b[j][0]])
                i += 1
        
        print(res)
        
        return res                   
        
            
            
            
            
            
        
    
    
sol = Solution()
# sol.optimal_utilization(a=[[1, 2], [2, 4], [3, 6]],
#                         b=[[1, 2]],
#                         target=7)

sol.optimal_utilization(a=[[1, 3], [2, 5], [3, 7], [4, 10]],
                        b=[[1, 2], [2, 3], [3, 4], [4, 5]],
                        target=10)