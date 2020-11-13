

class Solution:
    
    
    def find_longest_palindromic_subsequence(self, s: str) -> int:
        
        if not s:
            return 0
        
        if len(s) == 1:
            return 1
        
        memo = [[-1] * len(s) for _ in range(len(s))]

        res = self.lps_recurse(0, len(s)-1, s, memo)
        
        return res
    
    
    def lps_recurse(self, start, end, s, memo) -> int:
        
        if start > end:
            return 0
        
        if start == end:
            return 1
        
        if memo[start][end] == -1:
        
            if s[start] == s[end]:
                memo[start][end] = 2 + self.lps_recurse(start + 1, end - 1, s, memo)
            else:
                l1 = self.lps_recurse(start + 1, end, s, memo)
                l2 = self.lps_recurse(start, end - 1, s, memo)
                memo[start][end] = max(l1, l2)
                
        return memo[start][end]
        


sol: Solution = Solution()
# print(sol.find_longest_palindromic_subsequence('abdbca')) # 5
# print(sol.find_longest_palindromic_subsequence('cddpd')) # 3
print(sol.find_longest_palindromic_subsequence('pqr')) # 1
    