import unittest

from solutions.challenge_9.sum_of_digits import sum_of_digits


class TestSumOfDigits(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(sum_of_digits(5), 5)

    def test_multi_digit(self):
        self.assertEqual(sum_of_digits(123), 6)
        self.assertEqual(sum_of_digits(4567), 22)

    def test_edge_case(self):
        self.assertEqual(sum_of_digits(0), 0)


if __name__ == "__main__":
    unittest.main()
