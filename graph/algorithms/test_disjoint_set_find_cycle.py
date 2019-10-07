import unittest
from disjoint_set_find_cycle import *


class TestDisjointSetFindCycle(unittest.TestCase):


    def setUp(self):
        pass

    
    def tearDown(self):
        pass

    
    def test_union_find_cycle_when_there_is_cycle_should_return_true(self):
        g = Graph('a b c'.split())
        g.add_edge('a', 'b')
        g.add_edge('b', 'c')
        g.add_edge('c', 'a')
        self.assertTrue(g.union_find_cycle())     


    def test_union_find_cycle_when_there_is_no_cycle_should_return_false(self):
        g = Graph('a b c'.split())
        g.add_edge('a', 'b')
        g.add_edge('b', 'c')
        self.assertFalse(g.union_find_cycle())    


if __name__ == '__main__':
    unittest.main()

