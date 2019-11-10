import unittest
from typing import List
from merge_k_lls import merge_linked_lists, Node

class TestMergeKLinkedLists(unittest.TestCase):
    
    
    def setUp(self):
        pass
    
    
    def tearDown(self):
        pass
    
    
    def test_merge_linked_lists_when_lists_are_valid_shoud_return_merged_list(self):
        lists = list()
        lists.append(Node(3,Node(5,Node(7,Node(8)))))
        lists.append(Node(1,Node(2,Node(9,Node(11)))))
        lists.append(Node(4,Node(6,Node(10,Node(12)))))
        expected = Node(1,Node(2, Node(3,Node(4,Node(5,Node(6,Node(7,Node(8,Node(9,Node(10,Node(11,Node(12))))))))))))
        
        exp_node = expected;
        res_node = merge_linked_lists(lists);
        
        while exp_node != None and res_node != None:
            self.assertEqual(exp_node.val,res_node.val)
            exp_node = exp_node.next
            res_node = res_node.next
        
    
if __name__ == '__main__':
    unittest.main()