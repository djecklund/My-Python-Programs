from MathEquations import MathEquations
import sys

userInput = input("Do you want to do some math? Type yes or no: ")

while(userInput != 'no' and userInput != 'No'):
    if userInput == "yes" or userInput == "Yes":

        try:

            num1 = int(input("Please enter your first number: "))
            operation = input("Please enter an operation Examples are +, -, /, *: ")

            if operation != "+" or operation != "-" or operation != "/" or operation != "*":
                while(operation != "+" and operation != "-" and operation != "/" and operation != "*"):
                    operation = input("You have entered an incorrect operation, please pick from the following: +, -, /, * ")

            num2 = int(input("Please enter a second number: "))
            math = MathEquations()
            print(num1, " ", operation, " ", num2, " = ", math.math(num1,operation, num2))
        except:
            print("Oops, the exception: ", sys.exc_info()[0], " occured.")

        userInput = input("Do you want to do some math? Type yes or no: ")
    else:
        userInput = input("You have entered an incorrect response, please enter either yes or no. ")