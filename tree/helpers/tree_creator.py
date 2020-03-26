print('TreeCreator.py')
from .node import Node
from math import floor, ceil


class TreeCreator(object):

	@staticmethod
	def create_nodes(values):

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













