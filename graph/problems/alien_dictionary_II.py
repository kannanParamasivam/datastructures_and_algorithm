'''
269. Alien Dictionary
Hard

1569

309

Add to List

Share
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
]

Output: ""

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
'''


from typing import List
from collections import defaultdict
from pprint import pprint


class Solution:


	def alienOrder(self, words: List[str]) -> str:

		if not words:
			return

		g: defaultdict(set) = self.create_letter_graph(words=words)

		visited = set()
		stack: List[str] = []

		for c in list(g.keys()):               # topological sort
			if c not in visited:
				self.dfs(c, g, visited, stack)

		stack.reverse()
		return "".join(stack)


	def dfs(self, node: str, g: defaultdict(set), visited: set, stack: List[str]):

		if node in visited:
			return

		visited.add(node)

		for child_node in g[node]:
			self.dfs(child_node, g, visited, stack)

		stack.append(node)


	def create_letter_graph(self, words: List[str]) -> defaultdict(set):

		g = defaultdict(set)

		for wi in range(len(words) - 1):
			word_one, word_two = words[wi], words[wi+1]

			for c1, c2 in zip(word_one, word_two):

				if c1 != c2:
					g[c1].add(c2)
					break

		return g


sol = Solution()
assert sol.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]) == "wertf"



