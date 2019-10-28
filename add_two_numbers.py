'''
Given two numbers in singly linked list form, where each digit will be a node and which is in reverse order, 
Find sum of these two numbers and return result as linked list where the digital positions are reversed.

123 would be 3->2->1
546 would be 6->4->5
result should be 689 which is 9->8->6
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        num1 = self.get_num(l1)
        num2 =  self.get_num(l2)
        
        res = num1+num2
        
        resPv = 1
        
        while abs(res // resPv) > 0:
            resPv = resPv * 10
            
        resPv = abs(resPv//10)
        
        stack = []
        
        while abs(resPv) > 0:
            stack.append(abs(res//resPv))
            if resPv > 0:
                res = res - (abs(res//resPv)*resPv)
            resPv = resPv // 10
            
            
        dummyHead = ListNode(None)
        currListNode = dummyHead
        
        
        while len(stack) > 0:
            currListNode.next = ListNode(stack.pop())
            currListNode = currListNode.next
        
        return dummyHead.next
        
    
    
    def get_num(self, n:ListNode):
        
        pv = 1
        cur = n
        num = 0
        
        while cur != None:
            num += (cur.val * pv)
            pv = pv*10
            cur = cur.next
            
        return num
    