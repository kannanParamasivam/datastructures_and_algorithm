import unittest
from BFS_adj_matrix import Graph


class TestGraph(unittest.TestCase):


    def setUp(self):
        print('set up')
        self.g = Graph('a b c d'.split())
        self.g.add_edge('a', 'c')
        self.g.add_edge('c', 'a')
        self.g.add_edge('a', 'b')
        self.g.add_edge('b', 'c')
        self.g.add_edge('c', 'd')
        self.g.add_edge('d', 'd')


    def tearDown(self):
        del self.g


    def test_BFS(self):
        self.assertEqual(self.g.breadth_first_search('c'), 'c a d b')


if __name__ == '__main__':
    unittest.main()
