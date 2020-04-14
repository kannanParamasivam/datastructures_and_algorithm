from typing import List
from queue import PriorityQueue
from helper import LinkedListHelper, ListNode
from pprint import pprint


class Solution:


	def mergeKLists(self, lists: List[ListNode]) -> ListNode:

		if not lists:
			return

		min_heap = PriorityQueue()

		# load node values of all lists into minheap
		for  list_item in lists:
			cur_node = list_item

			while cur_node:
				min_heap.put(cur_node.val)
				cur_node = cur_node.next

		res_header: ListNode = ListNode(-1)
		cur_res = res_header

		while not min_heap.empty():
			val = min_heap.get()

			node: ListNode = ListNode(val)
			cur_res.next = node
			cur_res = node

		return res_header.next



lists: List[ListNode] = [LinkedListHelper.create_linked_list([1, 4, 5]),
                         LinkedListHelper.create_linked_list([1, 3, 4]),
                         LinkedListHelper.create_linked_list([2, 6])]

sol = Solution()
resultNode: ListNode = sol.mergeKLists(lists)
print(resultNode)
