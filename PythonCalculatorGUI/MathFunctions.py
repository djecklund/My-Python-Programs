import decimal as dec

class MathFuncs:

    def addition(self, num1, num2):
        sum = dec.Decimal(num1) + dec.Decimal(num2)
        return str(sum)

    def subtraction(self, num1, num2):
        difference = dec.Decimal(num1) - dec.Decimal(num2)
        return str(difference)

    def multiplication(self, num1, num2):
        product = dec.Decimal(num1) * dec.Decimal(num2)
        return str(product)

    def division(self, num1, num2):
        quotient = dec.Decimal(num1) / dec.Decimal(num2)
        return str(quotient)
