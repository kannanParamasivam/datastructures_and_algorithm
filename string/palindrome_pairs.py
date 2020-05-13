'''
336. Palindrome Pairs
Hard

1253

147

Add to List

Share
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
'''

from typing import List
from pprint import pprint


class Solution:


	def palindromePairs(self, words: List[str]) -> List[List[int]]:

		if not words or len(words) == 0:
			return

		reversed_words = {w[::-1]:i for i, w in enumerate(words)} 				# Create reverse dictionary
		results: List[List[int]] = []

		for wi in range(len(words)):											# For each word in words

			word = words[wi]
			i  = len(word) - 1

			if len(word) == 1:
				continue

			if word in reversed_words:													# check reverse of whole word present
				results.append([wi, reversed_words[word]])

			while i >= 0:

				prefix = word[0:i]

				suffix = word[i:len(word)]
				# print(f'prefix {prefix}; suffix {suffix}')

				if self.is_palindrome(prefix) and suffix in reversed_words:				# if prefix is palindrome check for suffix
					results.append([reversed_words[suffix], wi])

				if self.is_palindrome(suffix) and prefix in reversed_words:				# if suffix is palindrome check for prefix
					results.append([wi, reversed_words[prefix]])

				i -= 1

		return results


	def is_palindrome(self, word) -> bool:

		if not word or len(word.strip()) == 0:
			return False

		if len(word) == 1:
			return True

		i, j = 0, len(word) - 1

		while i <= j:

			if word[i] != word[j]:
				return False

			i += 1
			j -= 1

		return True


sol: Solution = Solution()
assert sol.is_palindrome('madam') == True
assert sol.is_palindrome('abcd') == False
assert sol.is_palindrome('a') == True
print(sol.palindromePairs(["abcd","dcba","lls","s","sssll"]))
print(sol.palindromePairs(["bat","tab","cat"]))






# ["abcd","dcba","lls","s","sssll"]
