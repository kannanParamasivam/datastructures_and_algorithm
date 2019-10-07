import unittest
from add_two_numbers import ListNode, Solution


class TestAddTwoNumbers(unittest.TestCase):

    def test_add_two_numbers_should_return_result(self):
        ln11 = ListNode(2)
        ln12 = ListNode(4)
        ln13 = ListNode(3)
        ln11.next = ln12
        ln12.next = ln13

        ln21 = ListNode(5)
        ln22 = ListNode(6)
        ln23 = ListNode(4)
        ln21.next = ln22
        ln22.next = ln23

        s = Solution()
        s.addTwoNumbers(ln11,ln21)





if __name__ == '__main__':
    unittest.main()