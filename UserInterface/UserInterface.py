class UserInterface():
    def showTitle(self):
        print("***"*15)
        print("Calculadora Suma de numeros en Ingles")
        print("***"*15)

    def getWordNumber(self, order):
        message="ingrese el "+order+" numero en ingles: "
        number = raw_input(message)
        return number

    def showResult(self,result):
        print("---"*15)
        print ("El resultado es: ", result)