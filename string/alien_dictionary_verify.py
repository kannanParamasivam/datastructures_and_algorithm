'''
953. Verifying an Alien Dictionary
Easy

669

268

Add to List

Share
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
'''

from typing import List


class Solution:


	def isAlienSorted(self, words: List[str], order: str) -> bool:

		if not words or not order:
			return

		if len(words) == 1:
			return True

		dictionary = {c:i for i, c in enumerate(order)}

		for n in range(len(words)-1):
			if not self.is_in_order(words[n], words[n+1], dictionary):
				return False

		return True


	def is_in_order(self, word_one: str, word_two: str, dictionary: dict) -> bool:

		if not word_one and not word_two:
			return True

		found_diff = False

		for i in range(min(len(word_one), len(word_two))):

			if dictionary[word_one[i]] != dictionary[word_two[i]]:
				found_diff = True

				if dictionary[word_one[i]] > dictionary[word_two[i]]:
					return False

				break

		if not found_diff and len(word_two) < len(word_one):
			return False

		return True



sol:Solution = Solution()
assert sol.isAlienSorted(["hello","leetcode"], 'hlabcdefgijkmnopqrstuvwxyz') == True
assert sol.isAlienSorted(["lello","heetcode"], 'hlabcdefgijkmnopqrstuvwxyz') == False
assert sol.isAlienSorted(["monsy","money"], 'hlabcdefgijkmnopqrstuvwxyz') == False
assert sol.isAlienSorted(["mon","monday"], 'hlabcdefgijkmnopqrstuvwxyz') == True
assert sol.isAlienSorted(["monday","mon"], 'hlabcdefgijkmnopqrstuvwxyz') == False



