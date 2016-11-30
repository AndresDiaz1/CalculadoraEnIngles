from Calculator.Calculator import Calculator
from Translator.Translator import Translator
from UserInterface.UserInterface import UserInterface

if __name__ == "__main__":
    userInterface=UserInterface()
    traductor = Translator()
    calculator=Calculator()

    userInterface.showTitle()

    number1 = userInterface.getWordNumber("primer")
    number2 = userInterface.getWordNumber("segundo")

    number1 = traductor.wordToNumberTranslate(number1)
    number2 = traductor.wordToNumberTranslate(number2)

    result = calculator.add(number1, number2)
    userInterface.showResult(result)





