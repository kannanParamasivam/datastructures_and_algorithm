'''
94. Binary Tree Inorder Traversal
Medium

2787

120

Add to List

Share
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \\
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively
'''
from typing import List
from helpers import TreeHelper, Node
from collections import namedtuple


class Solution:


	def inorderTraversal(self, root: Node) -> List[int]:

		StackItem = namedtuple('StackItem',('node', 'processed'))

		if not root:
			return

		res: List[int] = []
		stack: List[tuple] = [(StackItem(node=root,processed=False))]

		while stack:
			cur_item: StackItem = stack.pop()

			if cur_item.processed:
				res.append(cur_item.node.val)
				continue

			if cur_item.node.right and cur_item.node.right.val:
				stack.append(StackItem(node=cur_item.node.right, processed=False))

			stack.append(StackItem(node=cur_item.node, processed = True))

			if cur_item.node.left and cur_item.node.left.val:
				stack.append(StackItem(node=cur_item.node.left, processed=False))

		return res






sol = Solution()
print(sol.inorderTraversal(TreeHelper.create_tree([1, None, 2, None, None, 3, None])))



