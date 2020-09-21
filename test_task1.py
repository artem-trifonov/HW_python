import unittest
import task1 as tk


class Task1UnitTest(unittest.TestCase):
    def test_value_without_unit(self):
        self.assertEqual(tk.task1("341"), 341)

    def test_value_with_unit1(self):
        self.assertEqual(tk.task1("21m"), 1260)

    def test_value_with_unit2(self):
        self.assertEqual(tk.task1("21s"), 21)

    def test_value_with_unit3(self):
        self.assertEqual(tk.task1("1d"), tk.day)

    def test_unit_without_value1(self):
        self.assertEqual(tk.task1("s"), tk.sec)

    def test_unit_without_value2(self):
        self.assertEqual(tk.task1("m"), tk.minute)

    def test_unit_without_value3(self):
        self.assertEqual(tk.task1("h"), tk.hour)

    def test_unit_without_value4(self):
        self.assertEqual(tk.task1("d"), tk.day)

    def test_float_value_with_unit(self):
        self.assertEqual(tk.task1("1.5h"), 5400)

    def test_value_with_fullname_unit(self):
        self.assertEqual(tk.task1("20minute"), tk.exception_message)

    def test_value_with_two_units(self):
        self.assertEqual(tk.task1("1d1h"), tk.exception_message)

    def test_value_without_unsupported_unit(self):
        self.assertEqual(tk.task1("1y"), tk.exception_message)

    def test_with_empty_value(self):
        self.assertEqual(tk.task1(""), tk.exception_message)


if __name__ == '__main__':
    unittest.main()
