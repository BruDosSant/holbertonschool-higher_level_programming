import unittest
from max_integer import max_integer  # Asegúrate de que max_integer está correctamente importada

class TestMaxInteger(unittest.TestCase):

    def test_max_integer_with_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_integer_with_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_max_integer_with_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)

    def test_max_integer_with_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_integer_with_single_element(self):
        self.assertEqual(max_integer([10]), 10)

    def test_max_integer_with_duplicates(self):
        self.assertEqual(max_integer([1, 1, 1, 1, 1]), 1)

    def test_max_integer_with_large_numbers(self):
        self.assertEqual(max_integer([1000000, 2000000, 500000]), 2000000)

    def test_max_at_the_end(self):
        """Test for 'max at the end'."""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

if __name__ == '__main__':
    unittest.main()
