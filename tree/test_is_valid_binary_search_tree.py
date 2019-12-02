import unittest
from typing import List
from is_valid_binary_search_tree import Solution, TreeNode

class TestSolution(unittest.TestCase):
    
    
    def setUp(self):
        pass
    
    
    def tearDown(self):
        pass
    
    
    def test_isValidBST_when_tree_has_single_node_should_return_true(self):
        sol = Solution()
        root = sol.get_tree([1],0)
        self.assertTrue(sol.isValidBST(root))
        
    
    def test_isValidBST_when_tree_is_BST_should_return_true(self):
        sol = Solution()
        root = sol.get_tree([6,2,9,1,3,8,10],0)
        self.assertTrue(sol.isValidBST(root))
        

if __name__ == '__main__':
    unittest.main()