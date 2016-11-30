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

ByOne = [
"zero",
"one",
"two",
"three",
"four",
"five",
"six",
"seven",
"eight",
"nine",
"ten",
"eleven",
"twelve",
"thirteen",
"fourteen",
"fifteen",
"sixteen",
"seventeen",
"eighteen",
"nineteen"
]
ByTen = [
"zero",
"ten",
"twenty",
"thirty",
"forty",
"fifty",
"sixty",
"seventy",
"eighty",
"ninety"
]
zGroup = [
"",
"thousand",
"million",
"billion",
"trillion",
"quadrillion",
"quintillion",
"sextillion",
"septillion",
"octillion",
"nonillion",
"decillion",
]

class Translator():

    def splitPhrase(self,splitPhrase):
        wordsNumberArray=re.split(r"[\s-]+", splitPhrase)
        return wordsNumberArray

    def getElementalNumber(self, word):
        return elementalNumbers.get(word,None)

    def getMagnitudeNumber(self, word):
        return magnitudeNumbers.get(word,None)

    def wordToNumberTranslate(self, Phrase):
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


    def numberToWordTranslate(self,number):
        return 0 if number=="Zero" else self.thousandUp(number)

    def thousandUp(self,number):
        return " ".join(reversed([self.subThousand(z) + (" " + zGroup[i] if i else "") if z else "" for i, z in enumerate(self.splitByThousands(number))]))

    def splitByThousands(self,number):
        resultSplittedByThousands = []
        while number:
            number, remainder = divmod(number, 1000)
            resultSplittedByThousands.append(remainder)
        return resultSplittedByThousands

    def subThousand(self,number):
        if number <= 19:
            return ByOne[number]
        elif number <= 99:
            quotient, remainder = divmod(number, 10)
            return ByTen[quotient] + (" " + self.subThousand(quotient) if remainder else "")
        else:
            quotient, remainder = divmod(number, 100)
            return ByOne[quotient] + " hundred" + (" and " + self.subThousand(remainder) if remainder else "")