

class Solution:

    
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        
        ptr1, ptr2 = len(S) - 1, len(T) - 1
        
        while ptr1 >= 0 or ptr2 >= 0:
            
            backspaces1 = 0
            
            while ptr1 >=0:
                
                if S[ptr1] == '#':
                    backspaces1 += 1
                elif backspaces1 > 0:
                    backspaces1 -= 1
                else:
                    break
                    
                ptr1 -= 1
            
            backspaces2 = 0
            
            while ptr2 >= 0:
                
                if T[ptr2] == '#':
                    backspaces2 += 1
                elif backspaces2 > 0:
                    backspaces2 -= 1
                else:
                    break
                    
                ptr2 -= 1
                
            if ptr1 < 0 and ptr2 < 0:
                return True
            elif ptr1 < 0 or ptr2 < 0:
                return False
            elif S[ptr1] != T[ptr2]:
                return False
            
                
            ptr1 -= 1
            ptr2 -= 1
                
        return True


sol = Solution()
print(sol.backspaceCompare('xy#z', 'xzz#'))
print(sol.backspaceCompare('xy#z', 'xyz#'))
print(sol.backspaceCompare('xp#', 'xyz##'))