import unittest
from reorder_data_in_log_files import Solution


class TestReorderLogFile(unittest.TestCase):
    
    
    def setUp(self):
        pass
    
    
    def tearDown(self):
        pass
    
    
    def test_reorderLogFiles_when_input_is_valid_log_file_should_return_reordered_logs(self):
        sol = Solution()
        self.assertEqual(sol.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]),
                                            ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"])
        
        
    def test_reorderLogFiles_when_input_has_same_content_with_different_title_should_order_by_title(self):
        sol = Solution()
        self.assertEqual(sol.reorderLogFiles(["let3 art can","let1 art can"]),
                                            ["let1 art can","let3 art can"])
        
        
if __name__ == '__main__':
    unittest.main()