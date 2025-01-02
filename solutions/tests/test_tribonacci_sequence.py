import unittest

from solutions.the_tribonacci_sequence.main import tribonacci


class TestTribonacci(unittest.TestCase):
    """Test suite for the tribonacci function."""

    def test_base_cases(self):
        """Test the base cases."""
        self.assertEqual(tribonacci(0), 0)  # Base case T(0)
        self.assertEqual(tribonacci(1), 1)  # Base case T(1)
        self.assertEqual(tribonacci(2), 1)  # Base case T(2)

    def test_standard_cases(self):
        """Test standard cases."""
        self.assertEqual(tribonacci(3), 2)  # 0, 1, 1, 2
        self.assertEqual(tribonacci(4), 4)  # 0, 1, 1, 2, 4
        self.assertEqual(tribonacci(5), 7)  # 0, 1, 1, 2, 4, 7
        self.assertEqual(tribonacci(6), 13)  # 0, 1, 1, 2, 4, 7, 13

    def test_large_values(self):
        """Test for larger values of n."""
        self.assertEqual(tribonacci(10), 149)  # Verify correct calculation for T(10)
        self.assertEqual(tribonacci(15), 3136)  # Verify correct calculation for T(15)

    def test_edge_cases(self):
        """Test edge cases."""
        self.assertEqual(tribonacci(30), 29249425)  # Large n value
