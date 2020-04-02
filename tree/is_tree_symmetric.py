'''
101. Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Note:
Bonus points if you could solve it both recursively and iteratively.
'''

from helpers import TreeHelper, Node

class Solution:


	def check_if_symmetric(self, subtree_1:Node, subtree_2:Node) -> bool:

		if not subtree_1 and not subtree_2:
			return True
		elif subtree_1 and subtree_2:

			if subtree_1.val != subtree_2.val:
				return False
			elif self.check_if_symmetric(subtree_1.left, subtree_2.right) and self.check_if_symmetric(subtree_1.right, subtree_2.left):
				return True
			else:
				return False

		else:
			return False


	def isSymmetric(self, root: Node) -> bool:

		if not root:
			return True

		return self.check_if_symmetric(root.left, root.right)

root:Node = TreeHelper.create_tree([1,2,2,3,None,4,3])
TreeHelper.print_tree(root)
print(Solution().isSymmetric(root))




