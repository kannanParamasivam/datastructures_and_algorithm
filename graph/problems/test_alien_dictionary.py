import unittest
from alien_dictionary import Solution



class TestAlienDictionary(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_alienorder_when_validAlienWordsAreProvided_should_retrunTheLetterOrder(self):
        Solution.alienOrder(["wrt","wrf","er","ett","rftt"])