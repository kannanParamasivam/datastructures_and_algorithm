from helpers import TreeHelper, Node


class Solution:
    
    
    def printkDistanceNodeDown(self, root:Node, k): 
      
        # Base Case 
        if root is None or root.val is None or k< 0 : 
            return 
      
        # If we reach a k distant node, print it 
        if k == 0 : 
            print(root.val)
            return 
        
        # Recur for left and right subtee 
        self.printkDistanceNodeDown(root.left, k-1) 
        self.printkDistanceNodeDown(root.right, k-1) 
    

    def printkDistanceNode(self, root:Node, target:Node, k): 
        if root is None: 
            return -1
    
        if root == target: 
            self.printkDistanceNodeDown(root, k) 
            return 0 
        
        dl = self.printkDistanceNode(root.left, target, k) 
        
        if dl != -1: 
            
            if dl +1 == k: 
                print(root.val)
        
            else: 
                self.printkDistanceNodeDown(root.right, k-dl-2) 
    
            return 1 + dl 
    
        dr = self.printkDistanceNode(root.right, target, k) 
        if dr != -1: 
            if (dr+1 == k): 
                print(root.val)
            else: 
                self.printkDistanceNodeDown(root.left, k-dr-2) 
            return 1 + dr 
    
        return -1
    

sol = Solution()
root:Node = TreeHelper.create_tree([3,5,1,6,2,9,8,None,None,7,4,None,None,None,None])
TreeHelper.print_tree(root)
sol.printkDistanceNode(root, root.left, 2)
   
