class Node:
    
    def __init__(self, data:int, next):
        self.data = data
        self.next = next
        
    def add_next(self, next:Node):
        self.next = next
        
def find_middle_point(head:Node) -> str:
    
    node = head
    sPtr = node
    fPtr = node
    
    while fPtr!=Node and fPtr.next!=None:
        sPtr = sPtr.next
        fPtr = fPtr.next.next
        
    return sPtr.data
    
        
