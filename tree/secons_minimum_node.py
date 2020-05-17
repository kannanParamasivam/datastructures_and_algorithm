'''
671. Second Minimum Node In a Binary Tree
Easy

546

785

Add to List

Share
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

Input:
    2
   / \\
  2   5
     / \\
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.


Example 2:

Input:
    2
   / \\
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List
from helpers import TreeHelper, Node
from sys import maxsize


class Solution:


	def findSecondMinimumValue(self, root: Node) -> int:

		if not root:
			return

		self.first_min, self.second_min = maxsize, maxsize

		self.traverse_pre_order(root)

		return self.second_min if self.second_min < maxsize else -1


	def traverse_pre_order(self, node: Node):

		if not node or not node.val:
			return

		if node.val < self.first_min:
			self.first_min = node.val
		elif self.first_min < node.val < self.second_min:
			self.second_min = node.val

		self.traverse_pre_order(node.left)
		self.traverse_pre_order(node.right)


sol = Solution()

tree = TreeHelper.create_tree([2, 2, 5, None, None, 5, 7])
TreeHelper.print_tree(tree)
assert sol.findSecondMinimumValue(tree) == 5

tree = TreeHelper.create_tree([2, 2, 2])
TreeHelper.print_tree(tree)
assert sol.findSecondMinimumValue(tree) == -1





