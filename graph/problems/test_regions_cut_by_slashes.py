import unittest
from regions_cut_by_slashes import Solution


class TestRegionsCutBySlashes(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_regionsCutBySlahes_when_validGridIsProvided_should_return_numberOfRegions(self):
        self.assertEqual(Solution.regionsCutBySlashes([" /", "/ "]), 2)


if __name__ == "__main__":
    unittest.main()

