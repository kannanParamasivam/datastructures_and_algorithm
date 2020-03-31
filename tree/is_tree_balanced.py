from helpers import TreeHelper
from helpers import Node
from collections import deque, namedtuple

BalanceAndHeight = namedtuple('BalanceAndHeight', ['balanced', 'height'])


class Solution:


	def isBalanced(self, root: Node):
		return self.is_height_balanced(root).balanced


	def is_height_balanced(self, root):

		if not root or not root.val:
			return BalanceAndHeight(balanced=True, height=0)

		left_balance_and_height = self.is_height_balanced(root.left)

		if not left_balance_and_height.balanced:
			return left_balance_and_height

		right_balance_and_height = self.is_height_balanced(root.right)

		if not right_balance_and_height:
			return right_balance_and_height

		if abs(left_balance_and_height.height - right_balance_and_height.height) <= 1:
			h = max([left_balance_and_height.height, right_balance_and_height.height])+1
			return BalanceAndHeight(balanced=True, height=h)
		else:
			h = max([left_balance_and_height.height, right_balance_and_height.height])+1
			return BalanceAndHeight(balanced=False, height=h)


root: Node = TreeHelper.create_tree([3, 9, 20, None, None, 15, 7])
TreeHelper.print_tree(root)
print(Solution().isBalanced(root))
