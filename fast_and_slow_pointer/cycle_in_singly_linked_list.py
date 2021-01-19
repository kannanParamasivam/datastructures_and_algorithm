from typing import List


class ListNode:

    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class LinkedList:

    def __init__(self, vals: List[int] = []):
        cur_node = None
        self.head = None
        self.d = dict()

        for i in range(len(vals)):
            
            node = None

            if vals[i] in self.d:
                node = self.d[vals[i]]
            else:
                node = ListNode(vals[i])
                self.d[vals[i]] = node
            
            if cur_node:
                cur_node.next = node
            
            cur_node = node

            if not self.head:
                self.head = cur_node


class Solution:

    
    def hasCycle(self, head: ListNode) -> bool:
        
        if not head:
            return False
        
        fast, slow = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
            
        return False


ll: LinkedList = LinkedList([1,2,3,1])
node: ListNode = ll.head
sol = Solution()
print(sol.hasCycle(node))

ll: LinkedList = LinkedList([1,2,3])
node: ListNode = ll.head
sol = Solution()
print(sol.hasCycle(node))

ll: LinkedList = LinkedList([1,2,3,4,5,6,3])
node: ListNode = ll.head
sol = Solution()
print(sol.hasCycle(node))




        