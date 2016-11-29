from Calculator import Calculator
import unittest

class testCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator=Calculator()

    def test_should_add_two_numbers(self):
        self.assertEqual(self.calculator.add(1,2), 3)

if __name__ == '__main__':
    unittest.main()