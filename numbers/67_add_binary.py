'''
67. Add Binary
Easy

1515

258

Add to List

Share
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        n = max(len(a), len(b))

        a = a.zfill(n)
        b = b.zfill(n)

        carry = 0
        ans = ''

        for i in range(n-1, -1, -1): # iterate from n to 0

            carry += int(a[i]) + int(b[i])

            ans += str(carry%2)

            carry = carry//2

        if carry == 1:
            ans += str(carry)

        ans = ans[len(ans)::-1]

        return ans


sol = Solution()
print(sol.addBinary('11','1'))
