import unittest
from find_articulation_points import ArticulationFinder


class TestArticulationFinder(unittest.TestCase):
    
    def setUp(self):
        pass
    
    
    def tearDown(self):
        pass
    
    
    def test_find_articulation_point_when_one_articulation_point_should_return_it(self):
        articulationFinder = ArticulationFinder()
        self.assertEqual(articulationFinder.find_articulation_point([[1,2],[1,3],[3,4],[4,2],[2,5]]),[2])
        

if __name__ == '__main__':
    unittest.main()
    