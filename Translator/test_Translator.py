from Translator import Translator
import unittest


class testWordToNumberTranslator(unittest.TestCase):
    def setUp(self):
        self.traductor = Translator()

    def test_splites_phrase_into_words(self):
        wordArray = self.traductor.splitPhrase("one hundred")
        self.assertEqual(len(wordArray), 2)

    def test_should_return_elementalNumber_if_is_in_array(self):
        wordArray = self.traductor.splitPhrase("ten")
        self.assertEqual(self.traductor.getElementalNumber(wordArray[0]), 10)

    def test_should_return_none_if_elementalNumber_is_not_in_array(self):
        wordArray = self.traductor.splitPhrase("palabra")
        self.assertEqual(self.traductor.getElementalNumber(wordArray[0]), None)

    def test_should_return_magnitudeNumber_if_is_in_array(self):
        wordArray = self.traductor.splitPhrase("million")
        self.assertEqual(self.traductor.getMagnitudeNumber(wordArray[0]), 1000000)

    def test_should_return_none_if_magnitudeNumber_is_not_in_array(self):
        wordArray = self.traductor.splitPhrase("single")
        self.assertEqual(self.traductor.getMagnitudeNumber(wordArray[0]), None)

    def test_should_translate_phrase_into_number(self):
        number = self.traductor.wordToNumberTranslate("twenty one")
        self.assertEqual(number, 21)

    def test_should_return_invalid_number_if_number_does_not_exists(self):
        self.assertEqual(self.traductor.wordToNumberTranslate("twenty uno"), "Invalid Number")


class testNumberToWordTranslator(unittest.TestCase):
    def setUp(self):
        self.traductor = Translator()

    def test_should_return_Zero_if_number_is_0(self):
        self.assertEqual(self.traductor.numberToWordTranslate("Zero"), 0)

    def test_should_split_by_thousands(self):
        self.assertEqual(self.traductor.splitByThousands(2705), [705,2])

    def test_should_return_sub_thousands_function_a_string_below_19_if_passed_number_is_below_19(self):
        self.assertEqual(self.traductor.subThousand(3), "three")

    def test_should_return_sub_thousands_function_a_string_below_99_if_passed_number_is_below_99(self):
        self.assertEqual(self.traductor.subThousand(33), "thirty three")

    def test_should_return_sub_thousands_function_a_string_above_99_if_passed_number_is_above_99(self):
        self.assertEqual(self.traductor.subThousand(333), "three hundred and thirty three")


if __name__ == '__main__':
    unittest.main()
