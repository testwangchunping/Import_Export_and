import unittest
from Automation_test_module.read_csv_file2.csv_read import Test

class TestCase(unittest.TestCase):
    test = Test()
    def test_case(self):
        self.test.user_login('zdh2', 'boss', 'aaaaaa')
        self.test.test_export()
if __name__ == "__main__":
    unittest.main()
