from helper import ListNode, LinkedListHelper


class Solution:


    def is_palindrome(self, head: ListNode) -> bool:

        if not head:
            return False

        # find middle of linked list
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half of linked list
        rev_head = self.reverse_linked_list(slow)

        # check both nodes are same
        while head and rev_head:
            
            if head.val != rev_head.val:
                return False

            head = head.next
            rev_head = rev_head.next

        return True


    def reverse_linked_list(self, head: ListNode) -> ListNode:

        prev = None
        current  = head

        while current:
            _next = current.next
            current.next = prev
            prev = current
            current = _next

        return prev



header: ListNode = LinkedListHelper.create_linked_list([1,2,3,4,2,1])
LinkedListHelper.print_linked_list(header)
sol = Solution()
#rev_header = sol.reverse_linked_list(header)
#LinkedListHelper.print_linked_list(rev_header)
print(sol.is_palindrome(header))