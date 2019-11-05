'''Given the string and dictionary delete minimum number of characters from string to make a word from the dictionary'''

import unittest
from delete_minimum_characters import deleteMinChars


class TestDeleteMinChars(unittest.TestCase):

    def test_deleteminchars_when_StringAndDictionaryProvided_should_ReturnResult(self):
        self.assertEqual(deleteMinChars(dic=['a', 'aa', 'aaa'], query='abc'), 2)


if __name__ == '__main__':
    unittest.main()