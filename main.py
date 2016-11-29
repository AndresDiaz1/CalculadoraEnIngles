from Calculator.Calculator import Calculator
from WordToNumberTraductor.WordToNumberTraductor import WordToNumberTraductor
from UserInterface.UserInterface import UserInterface

if __name__ == "__main__":
    userInterface=UserInterface()
    traductor = WordToNumberTraductor()
    calculator=Calculator()

    userInterface.showTitle()

    number1 = userInterface.getWordNumber("primer")
    number2 = userInterface.getWordNumber("segundo")

    number1 = traductor.translate(number1)
    number2 = traductor.translate(number2)

    result = calculator.add(number1, number2)
    userInterface.showResult(result)





