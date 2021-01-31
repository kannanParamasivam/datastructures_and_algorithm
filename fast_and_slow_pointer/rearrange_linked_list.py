from helper import ListNode, LinkedListHelper


class Solution:


    def rearrange_linked_list(self, head: ListNode) -> ListNode:

        # find middle of the linked list
        slow, fast = head, head
        head_backup = head
        prev = slow

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        #print(slow.val)
        
        # reverse second half of the linked list
        rev_head = self.reverse_linked_list(slow)
        #print(rev_head.val)
        prev.next = None

        # rearrange the linked list
        while head and rev_head:
            head_next = head.next
            rev_head_next = rev_head.next
            head.next = rev_head
            rev_head.next = head_next
            head = head_next
            rev_head = rev_head_next

        # return head of linked list
        return head_backup


    def reverse_linked_list(self, head: ListNode) -> ListNode:

        current = head
        prev = None

        while current:
            _next = current.next
            current.next = prev
            prev = current
            current = _next

        return prev


sol = Solution()
h: ListNode = LinkedListHelper.create_linked_list([1,2,3,4,5,6])
sol.rearrange_linked_list(h)
LinkedListHelper.print_linked_list(h)
