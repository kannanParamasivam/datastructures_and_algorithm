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
'''

from typing import List
from collections import defaultdict


class Solution:


	def validTree(self, n: int, edges: List[List[int]]) -> bool:

		if not edges and n == 1:
			return True

		g = defaultdict(set)

		for node1, node2 in edges:									# Create graph from edges
			g[node1].add(node2)
			g[node2].add(node1)

		visited = set()
																	# DFS to make it sure not cycle (back edges)
																	# DFS to make it sure all nodes are connect (connected graph)
		if not self.has_cycle(g, edges[0][0], None, visited) and len(visited) == len(g) == n:
			return True
		else:
			return False


	def has_cycle(self, g: defaultdict, node: int, parent: int, visited: set) -> bool:

		if node in visited:
			return True

		visited.add(node)

		return any(map(lambda child_node: self.has_cycle(g, child_node, node, visited) if child_node != parent else False, g[node]))




sol: Solution = Solution()
assert sol.validTree(5, [[0,1], [0,2], [0,3], [1,4]]) == True
assert sol.validTree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]]) == False
