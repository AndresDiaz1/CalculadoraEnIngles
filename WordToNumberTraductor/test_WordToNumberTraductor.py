from WordToNumberTraductor import WordToNumberTraductor
from WordToNumberTraductor import InvalidNumberException
import unittest

class testWordToNumberTraductor(unittest.TestCase):

    def setUp(self):
        self.traductor=WordToNumberTraductor()
        self.InvalidNumber=InvalidNumberException("Numero invalido")

    def test_splites_phrase_into_words(self):
        wordArray=self.traductor.splitPhrase("one hundred")
        self.assertEqual(len(wordArray), 2)

    def test_should_return_elementalNumber_if_is_in_array(self):
        wordArray=self.traductor.splitPhrase("ten")
        self.assertEqual(self.traductor.getElementalNumber(wordArray[0]),10)

    def test_should_return_none_if_elementalNumber_is_not_in_array(self):
        wordArray=self.traductor.splitPhrase("palabra")
        self.assertEqual(self.traductor.getElementalNumber(wordArray[0]),None)

    def test_should_return_magnitudeNumber_if_is_in_array(self):
        wordArray = self.traductor.splitPhrase("million")
        self.assertEqual(self.traductor.getMagnitudeNumber(wordArray[0]), 1000000)

    def test_should_return_none_if_elementalNumber_is_not_in_array(self):
        wordArray = self.traductor.splitPhrase("single")
        self.assertEqual(self.traductor.getMagnitudeNumber(wordArray[0]), None)

    def test_should_translate_phrase_into_number(self):
        number = self.traductor.translate("twenty one")
        self.assertEqual(number, 21)

    #def test_should_raise_Exception_if_number_does_not_exists(self):
     #   self.assertRaises(self.InvalidNumber, lambda: self.traductor.translate("twenty uno"))

if __name__ == '__main__':
    unittest.main()