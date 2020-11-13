from pprint import pprint


class Solution:
    
    
    def longest_palindromic_subsequence(self, s: str) -> int:
        
        if not s:
            return 0
        
        if len(s) == 1:
            return 1
        
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        
        # mark every character as palindrome
        
        for i in range(len(s)):
            dp[i][i] = 1
            
        for start in range(len(s)-1, -1, -1):
            
            for end in range(start+1, len(s)):
                
                if s[start] == s[end]:
                    dp[start][end] = 2 + dp[start + 1][end - 1]
                else:
                    dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])
        
        pprint(dp)
        
        return dp[0][len(s)-1]
        

sol: Solution = Solution()
print(sol.longest_palindromic_subsequence('abdbca'))             
            


    