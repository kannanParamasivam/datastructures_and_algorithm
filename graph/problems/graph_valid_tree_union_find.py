'''
261. Graph Valid Tree
Medium

942

32

Add to List

Share
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.

Accepted
121,910
Submissions
293,130
'''
from typing import List



class Solution:


	def validTree(self, n: int, edges: List[List[int]]) -> bool:

		if not edges and n  == 1:
			return True

		parents = [-1 for i in range(n)]

		for node1, node2 in edges:
			set1 = self.get_parent(parents, node1)
			set2 = self.get_parent(parents, node2)

			if set1 == set2:
				return False
			else:
				self.union(parents, set1, set2)

		return True if len([p for p in parents if p < 0]) == 1 else False




	def get_parent(self, parents, node):
		i = node

		while parents[i] != -1:
			i = parents[i]

		return i


	def union(self, parents, set1, set2):
		if set1 != set2:
			parents[set2] = set1






sol: Solution = Solution()
print(sol.validTree(5, [[0,1], [0,2], [0,3], [1,4]]))
print(sol.validTree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]]))
