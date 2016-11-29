from Calculator.Calculator import Calculator
from WordToNumberTraductor.WordToNumberTraductor import WordToNumberTraductor
from UserInterface.UserInterface import UserInterface

if __name__ == "__main__":
    userInterface=UserInterface()
    userInterface.showTitle()

    number1 = userInterface.getWordNumber("primer")
    number2 = userInterface.getWordNumber("segundo")

    traductor = WordToNumberTraductor()
    number1 = traductor.translate(number1)
    number2 = traductor.translate(number2)

    calculator=Calculator()
    result = calculator.add(number1, number2)
    userInterface.showResult(result)





