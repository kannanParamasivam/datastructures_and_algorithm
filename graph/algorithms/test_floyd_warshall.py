import unittest
from floyd_warshall import Graph


class TestFloydWarshall(unittest.TestCase):


    def setUp(self):
        self.g = Graph('a b c d'.split())
        self.g.add_edge('a', 'b', 3)
        self.g.add_edge('b', 'a', 8)
        self.g.add_edge('a', 'd', 7)
        self.g.add_edge('d', 'a', 2)
        self.g.add_edge('c', 'a', 5)
        self.g.add_edge('c', 'd', 1)
        self.g.add_edge('b', 'c', 2)

    
    def tearDown(self):
        pass

    
    def test_floyd_warshall(self):
        self.assertEqual(self.g.floydwarshall(),
            [[0, 3, 5, 6], 
             [5, 0, 2, 3], 
             [3, 6, 0, 1], 
             [2, 5, 7, 0]])
        


if __name__ == '__main__':
    unittest.main()