class Calculator():
    def add(self, number1, number2):
        return "Zero" if (self.isInvalidNumber(number1) or self.isInvalidNumber(number2)) else number1 + number2

    def isInvalidNumber(self, number):
        return number == "Invalid Number"
