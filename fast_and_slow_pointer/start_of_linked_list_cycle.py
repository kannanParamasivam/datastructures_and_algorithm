'''
142. Linked List Cycle II
Start of LinkedList cycle
'''


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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Done using Floyd's cycle detection algorithm

class Solution:
    
    
    def detectCycle(self, head: ListNode) -> ListNode:
        
        # detect meeting point of slow and fast pointer
        slow, fast = head, head
        
        if not fast or not fast.next:
            return None
        
        has_cycle = False
        
        while fast and fast.next:
            
            if fast == None or fast.next == None:
                return None
            
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                has_cycle = True
                break
        
        if not has_cycle:
            return None
        
        # move slow pointer to head
        slow = head
        
        # move fast and slow one step at a time and get the meeting point
        while fast != slow:
            slow = slow.next
            fast = fast.next
        
        # retrun the meeting point detected
        return slow


def print_node(node: ListNode):
    if not node:
        print('No Cycle')
        return
    else:
        print(node.val)


ll: LinkedList = LinkedList([1,2,3,4,5,6,3])
head: ListNode = ll.head
sol = Solution()
print_node(sol.detectCycle(head))

ll: LinkedList = LinkedList([1,2,3,4,5,6])
head: ListNode = ll.head
sol = Solution()
print_node(sol.detectCycle(head))



        

