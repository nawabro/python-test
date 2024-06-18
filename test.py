import unittest
from app import add

class TestApp(unittest.TestCase):
    def test_add(self):
        result = add(5, 10)  # Replace with the actual parameters you want to test
        expected_result = 15  # Replace with the expected result
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()