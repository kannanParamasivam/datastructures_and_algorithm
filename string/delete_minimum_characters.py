from collections import deque

queue = deque()

def deleteMinChars(dic,query):
    
    if dic == None or len(dic)==0 or len(query) == 0:
        return -1
    
    queue.append((query,0))
     
    while len(queue) > 0:
        s, l = queue.popleft()
        
        if s in dic:
            return l
        
        for i in range(len(s)):
            queue.append((s[0:i]+s[i+1:], l+1))
             
    return -1




    