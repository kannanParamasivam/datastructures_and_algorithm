from helper import ListNode, LinkedListHelper


class Solution:
    def reverse_linked_list(self, head: ListNode) -> ListNode:
        
        prev = None

        while head:
            _next = head.next
            head.next = prev
            prev = head
            head = _next 

        return prev



head:ListNode = LinkedListHelper.create_linked_list([1,2,3,4,5,6])
print('--- Original Linked List ---')
LinkedListHelper.print_linked_list(head)
sol: Solution = Solution()
print('--- Reversed Linked List ---')
LinkedListHelper.print_linked_list(sol.reverse_linked_list(head))
        