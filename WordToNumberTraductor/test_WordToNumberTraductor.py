from WordToNumberTraductor import WordToNumberTraductor
import unittest

class testWordToNumberTraductor(unittest.TestCase):

    def setUp(self):
        self.traductor=WordToNumberTraductor()

    def test_splites_phrase_into_words(self):
        wordArray=self.traductor.splitPhrase("one hundred")
        self.assertEqual(len(wordArray), 2)

    def test_should_return_elementalNumber_if_is_in_array(self):
        wordArray=self.traductor.splitPhrase("ten")
        self.assertEqual(self.traductor.getElementalNumber(wordArray[0]),10)

    def test_should_return_none_if_elementalNumber_is_not_in_array(self):
        wordArray=self.traductor.splitPhrase("palabra")
        self.assertEqual(self.traductor.getElementalNumber(wordArray[0]),None)


if __name__ == '__main__':
    unittest.main()