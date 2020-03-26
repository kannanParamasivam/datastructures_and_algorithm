from helpers import TreeCreator
from helpers import Node
from collections import deque, namedtuple

QueueNode = namedtuple('QueueNode', ['node', 'level'])

# root: Node = TreeCreator.create_nodes([1,2,3,4,5,6,7,8,9])

root: Node = TreeCreator.create_nodes([1, 2, 3, 4, 5, 6, 7, 8, 9])

q = deque()
q.append(QueueNode(root, 0))

while len(q) > 0:
	queue_item: QueueNode = q.popleft()

	if queue_item and queue_item.node:
		print('\t'*queue_item.level + str(queue_item.node.val))
		q.append(QueueNode(queue_item.node.left, queue_item.level+1))
		q.append(QueueNode(queue_item.node.right, queue_item.level+1))

