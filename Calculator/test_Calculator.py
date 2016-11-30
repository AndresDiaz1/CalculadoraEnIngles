from Calculator import Calculator
import unittest


class testCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_should_check_if_number_is_valid(self):
        self.assertEqual(self.calculator.isInvalidNumber(1), False)

    def test_should_check_if_number_is_invalid(self):
        self.assertEqual(self.calculator.isInvalidNumber("Invalid Number"), True)

    def test_should_add_two_numbers_if_are_valid(self):
        self.assertEqual(self.calculator.add(1, 2), 3)

    def test_should_return_zero_if_1st_number_is_invalid(self):
        self.assertEqual(self.calculator.add("Invalid Number", 2), "Zero")

    def test_should_return_zero_if_2nd_number_is_invalid(self):
        self.assertEqual(self.calculator.add(2, "Invalid Number"), "Zero")


if __name__ == '__main__':
    unittest.main()
