import unittest
from middle_of_singly_linked_list import Node, find_middle_point


class TestMiddleOfSinglyLinkedList(unittest.TestCase):
    
    def setUp(self):
        pass
    
    
    def tearDown(self):
        pass
    
    
    def test_find_middle_pint_when_odd_number_of_nodes(self):
        node1:Node = Node(1, None)
        node2:Node = Node(2, None)
        node3:Node = Node(3, None)
        node4:Node = Node(4, None)
        node5:Node = Node(5, None)
        
        node1.add_next(node2)
        node2.next = node3
        node3.next = node4
        node4.next = node5
        
        self.assertEqual(find_middle_point(node1), 3) 
        

if __name__ == '__main__':
    unittest.main()
        
        