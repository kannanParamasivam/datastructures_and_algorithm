import unittest
from two_sum import TwoSum


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.two_sum = TwoSum()

    def tearDown(self):
        del self.two_sum

    def test_twosum_should_return_empty_when_input_is_None(self):
        self.assertEqual(self.two_sum.two_sum(None, 3), [])

    def test_twosum_should_return_empty_when_input_isempty(self):
        self.assertEqual(self.two_sum.two_sum([], 3), [])

    def test_twosum_should_raise_exception_when_target_can_not_be_achieved(self):
        with self.assertRaises(Exception):
            self.two_sum.two_sum([1, 5, 10], 3)

    def test_twosum_should_return_two_elements_which_sums_to_target(self):
        res = sum(self.two_sum.two_sum([1, 5, 10, 2], 3))
        self.assertEqual(res, 3)
