'''
266. Palindrome Permutation
Easy

329

51

Add to List

Share
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
'''

from collections import defaultdict



class Solution:
	def canPermutePalindrome(self, s: str) -> bool:

		if not s:
			return

		letters_freq = defaultdict(int)

		# Find letter frequencies
		for c in s:
			letters_freq[c.lower()] += 1

		# Check if more than one letters with odd freq present
		found_odd_freq = False

		for f in letters_freq.values():

			if f%2 > 0:

				if found_odd_freq  ==  False:
					found_odd_freq  = True
				else:
					return False

		return True


sol: Solution = Solution()

assert sol.canPermutePalindrome('code') == False
assert sol.canPermutePalindrome('madma') ==  True
assert sol.canPermutePalindrome('Reppare') ==  True


