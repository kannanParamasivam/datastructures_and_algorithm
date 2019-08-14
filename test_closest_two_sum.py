import unittest
from closest_two_sum import find_closest_pair


class TestClosestTwoSum(unittest.TestCase):

    def test_find_closest_two_sum(self):
        array = [10, 22, 28, 29, 30, 40]
        n = len(array)
        target = 54
        self.assertEqual(find_closest_pair(array, n, target), (22, 30))

if __name__ == '__main__':
    unittest.main()