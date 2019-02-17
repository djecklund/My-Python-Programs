class MathEquations:

    def math(self, num1, operation ,num2):
        answer = 0
        if operation == "+":
            answer = self.addition(num1,num2)
        elif operation == "-":
            answer = self.subtraction(num1,num2)
        elif operation == "/":
            answer = self.division(num1,num2)
        elif operation == "*":
            answer = self.multiplication(num1,num2)
        else:
            print("You have entered an incorrect operation, please choose between one of the following: +,-,/,*")

        return answer

    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def division(self, num1, num2):
        return num1 / num2

    def multiplication(self, num1, num2):
        return num1 * num2