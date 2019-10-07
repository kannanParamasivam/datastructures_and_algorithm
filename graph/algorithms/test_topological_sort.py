import unittest
from topological_sort import Graph


class TestTopologicalSort(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_topological_sort_should_return_nodes_in_topological_order(self):
        g = Graph()
        g.add_edge('f', 'c')
        g.add_edge('f', 'a')
        g.add_edge('e', 'a')
        g.add_edge('e', 'b')
        g.add_edge('c', 'd')
        g.add_edge('d', 'b')
        res = g.topological_sort('f')
        self.assertTrue(res.index('f') < res.index('c'))
        self.assertTrue(res.index('f') < res.index('a'))
        self.assertTrue(res.index('e') < res.index('a'))
        self.assertTrue(res.index('e') < res.index('b'))
        self.assertTrue(res.index('c') < res.index('d'))
        self.assertTrue(res.index('d') < res.index('b'))


if __name__ == '__main__':
    unittest.main()
