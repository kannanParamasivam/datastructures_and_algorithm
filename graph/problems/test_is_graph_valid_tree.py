import unittest
from is_graph_valid_tree import is_valid_tree

class TestIsGraphValidTree(unittest.TestCase):
    
    def setUp(self):
        pass
    
    
    def tearDown(self):
        pass
    
    
    def test_is_graph_valid_tree_when_graph_has_no_cycle_and_connected_should_return_true(self):
        graph = [[0]*4 for i in range(4)]
        graph[0][1] = 1
        graph[0][2] = 1
        graph[2][3] = 1
        self.assertTrue(is_valid_tree(graph))
        
    
    def test_is_graph_valid_tree_when_graph_has_cycle_and_connected_should_return_false(self):
        graph = [[0]*5 for i in range(4)]
        graph[0][1] = 1
        graph[0][2] = 1
        graph[2][3] = 1
        graph[3][0] = 1
        graph[3][4] = 1
        self.assertFalse(is_valid_tree(graph))
        
    def test_is_graph_valid_tree_when_graph_is_disconnected_and_should_return_false(self):
        graph = [[0]*4 for i in range(4)]
        graph[0][1] = 1
        # graph[0][3] = 1
        graph[2][3] = 1
        self.assertFalse(is_valid_tree(graph))


if __name__ == '__main__':
    unittest.main()
    