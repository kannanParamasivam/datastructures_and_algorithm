print('TreeCreator.py')
from .node import Node
from math import floor, ceil
from collections import namedtuple


class TreeHelper(object):

	@staticmethod
	def create_tree(values):

		root: Node
		nodes = []

		for i, val in enumerate(values):
			n = Node(val, None, None)
			nodes.append(n)

			root = n if i == 0 else root

			if i > 0:

				if i % 2 > 0:
					nodes[i//2].left = n
				else:
					nodes[ (i//2) - 1 ].right = n

		return root


	@staticmethod
	def print_tree(root:Node):
		if not root:
			return

		QueueNode = namedtuple('QueueNode',['node', 'level'])
		q = []
		q.append(QueueNode(root, 0))

		while len(q) > 0:
			queue_item: QueueNode = q.pop()

			if queue_item and queue_item.node:
				print('\t'*queue_item.level + str(queue_item.node.val if queue_item.node.val else 'null'))
				q.append(QueueNode(queue_item.node.left, queue_item.level+1))
				q.append(QueueNode(queue_item.node.right, queue_item.level+1))















