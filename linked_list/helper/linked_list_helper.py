from typing import List
from .list_node import ListNode


class LinkedListHelper:

	@staticmethod
	def create_linked_list(list_items: List) -> ListNode:

		header: ListNode = ListNode(-1)
		currentNode: ListNode = header

		for list_item in list_items:
			list_node: ListNode = ListNode(list_item)
			currentNode.next = list_node
			currentNode = list_node

		return header.next
