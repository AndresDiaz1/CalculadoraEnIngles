import re

elementalNumbers = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90
}
magnitudeNumbers = {
    'thousand': 1000,
    'million': 1000000,
    'billion': 1000000000,
    'trillion': 1000000000000,
    'quadrillion': 1000000000000000,
    'quintillion': 1000000000000000000,
    'sextillion': 1000000000000000000000,
    'septillion': 1000000000000000000000000,
    'octillion': 1000000000000000000000000000,
    'nonillion': 1000000000000000000000000000000,
    'decillion': 1000000000000000000000000000000000,
}

class WordToNumberTraductor():

    def splitPhrase(self,splitPhrase):
        wordsNumberArray=re.split(r"[\s-]+", splitPhrase)
        return wordsNumberArray

    def getElementalNumber(self, word):
        return elementalNumbers.get(word,None)

    def getMagnitudeNumber(self, word):
        return magnitudeNumbers.get(word,None)

    def translate(self,Phrase):
        wordsNumberArray=self.splitPhrase(Phrase)
        elementalNumbersCounter=0
        magnitudeNumberCounter=0

        for word in wordsNumberArray:
            number=self.getElementalNumber(word)

            if number is not None:
                elementalNumbersCounter += number
            elif word == "hundred" and elementalNumbersCounter!=0:
                elementalNumbersCounter *=100
            else:
                number=self.getMagnitudeNumber(word)

                if number is not None:
                    magnitudeNumberCounter += elementalNumbersCounter * number
                    elementalNumbersCounter=0
                else:
                   return "Invalid Number"

        return magnitudeNumberCounter + elementalNumbersCounter
