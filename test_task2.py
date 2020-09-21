import unittest
import task2 as tk2


class Task2UnitTest(unittest.TestCase):
    def test_negative_value(self):
        self.assertEqual(tk2.task2(-50), "Incorrect value, supported only non-negative numbers")

    def test_zero_value(self):
        self.assertEqual(tk2.task2(0), 0)

    def test_with_same_numbers(self):
        self.assertEqual(tk2.task2(1111), 1111)

    def test_value_with_zero(self):
        self.assertEqual(tk2.task2(80), 8)


if __name__ == '__main__':
    unittest.main()
