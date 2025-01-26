import unittest
from your_module_name import max_integer  # Make sure to import max_integer from the correct module


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_empty_list(self):
        """Test for an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test for a list with a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_multiple_elements(self):
        """Test for a list with multiple elements"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        """Test for a list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        """Test for a list with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 0, 1, 2, 3]), 3)

    def test_floats(self):
        """Test for a list with float numbers"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_all_identical_numbers(self):
        """Test for a list where all elements are identical"""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_strings(self):
        """Test for a list of strings (comparison should be lexicographic)"""
        self.assertEqual(max_integer(['apple', 'banana', 'cherry']), 'cherry')


if __name__ == '__main__':
    unittest.main()
