''' Given the routers and connection between them, find out the critical routers which disconnect part of the network when it is removed or turned off'''

class Router:
    def __init__(self,val):
        self.val = val
        self.links = []
    def addLink(self,router):
        self.links.append(router)

def dfs(rootNode,removedOne):
    visited = {}
    stack = []
    stack.append(rootNode)
    while len(stack) > 0:
        top = stack.pop()
        if  top.val in visited.keys():
            continue
        if  top.val != removedOne.val:
            visited[top.val] = 1
            stack += top.links
    return len(visited)
        
def criticalRouters(numRouters,numLinks,links):
    if numRouters == 0:
        return []
    if len(links) < numRouters-1:
        return []
    routerList = [Router(i) for i in range(numRouters)]
    for link in links:
        routerList[link[0]-1].addLink(routerList[link[1]-1])
        routerList[link[1]-1].addLink(routerList[link[0]-1])
        
    
    criticals = []
    for i in range(numRouters):
        if i==0:
            rootNode = routerList[1]
        else:
            rootNode = routerList[0]
        removedOne = routerList[i]

        visitedNum = dfs(rootNode,removedOne)
        if visitedNum == numRouters-1:
            continue
        else:
            criticals.append(i+1)
    return criticals

# r = criticalRouters(numRouters,numLinks,Links)




print(criticalRouters(6,5,[[1,2],[2,3],[3,4],[4,5],[6,3]]))
