from helpers import TreeHelper, Node
import sys
from time import time, process_time


class Solution:


	def __init__(self):
		self.difference = sys.maxsize
		self.value = 0


	def closestValue(self, root: Node, target: float) -> int:

		if not root:
			return

		self.in_order_traversal(root, target)
		return self.value


	def in_order_traversal(self, node: Node, target: float):

		if not node:
			return

		self.in_order_traversal(node.left, target)

		diff = abs(node.val - target)

		if diff < self.difference:
			self.difference = diff
			self.value = node.val

		self.in_order_traversal(node.right, target)


start_time = process_time()

root: Node = TreeHelper.create_tree([4,2,5,1,3])
TreeHelper.print_tree(root)

sol = Solution()
print(sol.closestValue(root, 3.714286))

print(process_time() - start_time)
