import unittest
from dijkstra_shortest_path import Graph

class TestDijkstraShortestPath(unittest.TestCase):

    def setUp(self):
        self.g = Graph('a b c d'.split())
        self.g.add_edge('a','b',10)
        self.g.add_edge('a','c',20)
        self.g.add_edge('b','c',5)
        self.g.add_edge('b','d',16)
        self.g.add_edge('c','d',20)


    def tearDown(self):
        del self.g

    
    def test_dijkstra(self):
        res = self.g.dijkstra('a')
        self.assertEqual(res,{'a': [None, 0], 'b': ['a', 10], 'c': ['b', 15], 'd': ['b', 26]})


if __name__ == '__main__':
    unittest.main()   
