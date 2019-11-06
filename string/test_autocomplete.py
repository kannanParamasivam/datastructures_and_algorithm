import unittest
from autocomplete import AutoComplete

class TestAutoComplete(unittest.TestCase):
    
    
    def test_autoComplete_when_inputIsValid_should_returnWords(self):
        words = ["nature","nation","country","county"]
        self.assertEqual(len(AutoComplete(words).find_words("nat")),len(["nation","nature"]))
        
    
if __name__ == "__main__":
    unittest.main()