import unittest
from closest_two_sum_two_array import find_closest_two_sum


class TestClosestTwoSum(unittest.TestCase):

    def test_find_closest_two_sum_input_set_one(self):
        self.assertEqual(find_closest_two_sum(nums1=[1, 4, 5, 7],
                                              nums2=[10, 20, 30, 40],
                                              target=32),
                         (1, 30))  # Keyword arguments


    def test_find_closest_two_sum_input_set_two(self):
        self.assertEqual(find_closest_two_sum(nums1=[1, 4, 5, 7],
                                              nums2=[10, 20, 30, 40],
                                              target=50),
                         (7, 40))  # Keyword arguments
