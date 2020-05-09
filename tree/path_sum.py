'''
113. Path Sum II
Medium

1513

54

Add to List

Share
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''

from typing import List
from helpers import TreeHelper, Node


class Solution:


	def pathSum(self, root: Node, sum: int) -> List[List[int]]:

		if not root:
			return

		paths : List[List[int]] = []

		self.recurse_tree(root, 0, [], sum, paths)

		return paths


	def recurse_tree(self, node, path_sum: int, path: List[int], target_sum: int, paths):

		if not node or not node.val:
			return

		path_sum += node.val
		path.append(node.val)

		# Found leaf with targeted sum
		if path_sum == target_sum  and self.is_leaf(node):
			paths.append(list(path))
		# Reurse for left and right nodes
		else:
			self.recurse_tree(node.left, path_sum, path, target_sum, paths)
			self.recurse_tree(node.right, path_sum, path, target_sum, paths)

		path.pop()


	def is_leaf(self, node) -> bool:
		return not node.left and not node.right



root: Node = TreeHelper.create_tree([5,2,3,10,8,7,2,3,5,1,None,None,1,3,4])
# TreeHelper.print_tree(root)

sol = Solution()
print(sol.pathSum(root, 16))







