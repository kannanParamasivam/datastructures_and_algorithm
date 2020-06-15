'''
518. Coin Change 2
Medium

1874

61

Add to List

Share
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

 

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10] 
Output: 1
'''
from typing import List


class Solution:

    
    def change(self, amount: int, coins: List[int]) -> int:
        
        if amount == 0:                                    # Can get amount 0 1 way which is adding no coins
            return 1

        if amount > 0 and (not coins or len(coins) == 0):
            return 0
        
        ways:List[int] = [0] * (amount + 1)
        ways[0] = 1                                         # Can make amoutn 0 in 1 ways which is adding no coins
        
        for coin in coins:
            
            if coin <= amount:
                
                for i in range(coin, amount+1):
                    ways[i] = ways[i-coin] + ways[i]
                    
        return ways[amount]


sol: Solution = Solution()
assert sol.change(amount=5, coins=[1,2,5]) == 4
assert sol.change(amount=0, coins=[1,2,5]) == 1
assert sol.change(amount=6, coins=[]) == 0

                    
        
        
            
        