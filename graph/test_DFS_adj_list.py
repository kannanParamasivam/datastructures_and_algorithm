import unittest
from DFS_adj_list import Graph


class TestGraph(unittest.TestCase):


    def setUp(self):
        self.g = Graph('a b c d e f g'.split())
        self.g.add_edge('a','c')
        self.g.add_edge('a','g')
        self.g.add_edge('a','b')
        self.g.add_edge('g','c')
        self.g.add_edge('c','d')
        self.g.add_edge('b','e')
        self.g.add_edge('b','d')
        self.g.add_edge('d','e')
        self.g.add_edge('d','f')
        self.g.add_edge('f','g')
    

    def tearDown(self):
        del self.g

    
    def test_dfs(self):
        self.assertEqual(self.g.depth_first_search('a'), 'a c d e f g b')


if __name__ == '__main__':
    unittest.main()