from Calculator.Calculator import Calculator
from WordToNumberTraductor.WordToNumberTraductor import WordToNumberTraductor

class UserInterface():
    def showTitle(self):
        print("***"*15)
        print("Calculadora Suma de numeros en Ingles")
        print("***"*15)

    def getWordNumber(self, order):
        message="ingrese el "+order+" numero en ingles: "
        number = raw_input(message)
        return number

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
    print("El resultado es ", result)





