from Translator.Translator import Translator

class UserInterface():
    def showTitle(self):
        print("***"*15)
        print("Calculadora Suma de numeros en Ingles Vivelab")
        print("***"*15)

    def getWordNumber(self, order):
        message="ingrese el "+order+" numero en ingles: "
        number = raw_input(message)
        return number

    def showResult(self,result):
        print("---"*15)
        print ("El resultado es: ", result)
        translator=Translator()
        print("Que en ingles seria", translator.numberToWordTranslate(result))
        print("---"*15)
