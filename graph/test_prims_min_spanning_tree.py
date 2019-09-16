import unittest
from prims_min_spanning_tree import Graph


class TestMinSpanningTree(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_prims_should_give_min_spanning_tree(self):
        g = Graph('a b c d e f g h i'.split())
        g.add_edge('a', 'b', 4)
        g.add_edge('b', 'c', 8)
        g.add_edge('c', 'd', 7)
        g.add_edge('d', 'e', 9)
        g.add_edge('e', 'f', 10)
        g.add_edge('f', 'g', 2)
        g.add_edge('g', 'h', 1)
        g.add_edge('h', 'a', 8)
        g.add_edge('b', 'h', 11)
        g.add_edge('h', 'i', 7)
        g.add_edge('c', 'i', 2)
        g.add_edge('g', 'i', 6)
        g.add_edge('c', 'f', 4)
        g.add_edge('d', 'f', 14)
        self.assertEqual(g.prims(), 37)


if __name__ == '__main__':
    unittest.main()
