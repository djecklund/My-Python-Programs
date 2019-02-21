from tkinter import *
from MathFunctions import *

window = Tk()
window.title("Python Calculator")

def getAnswer(myInput):
    mathfuncs = MathFuncs()
    equation = myInput.split(" ")
    if " + " in myInput:
        resultsLBL.config(text=mathfuncs.addition(equation[0], equation[2]))
    elif " - " in myInput:
        resultsLBL.config(text=mathfuncs.subtraction(equation[0], equation[2]))
    elif " * " in myInput:
        resultsLBL.config(text=mathfuncs.multiplication(equation[0], equation[2]))
    elif " / " in myInput:
        resultsLBL.config(text=mathfuncs.division(equation[0], equation[2]))

def inputCalc(myInput):
    lblText = resultsLBL.cget("text")
    if myInput == ".":
        if lblText != "":
            if myInput not in lblText:
                lblText = resultsLBL.cget("text") + myInput
    elif myInput == "+" or myInput == "-" or myInput == "/" or myInput == "*":
        if " + " not in lblText and " - " not in lblText and " * " not in lblText and " / " not in lblText:
            if lblText != "":
                lblText = resultsLBL.cget("text") + " " + myInput + " "
            else:
                lblText = resultsLBL.cget("text")
        else:
            lblText = resultsLBL.cget("text")
    else:
        lblText = resultsLBL.cget("text") + myInput

    resultsLBL.config(text=lblText)

def clear():
    resultsLBL.config(text="")

#  Create Buttons and Label
clearButton = Button(window, text="C", bg="grey", fg="white", width=4, height=2, command=clear)
resultsLBL = Label(window, text="", bg="green", borderwidth=2, relief="sunken", width=15, height=2)
sevenButton = Button(window, text="7", bg="grey", fg="white", width=4, height=2, command=lambda: inputCalc("7"))
eightButton = Button(window, text="8", bg="grey", fg="white", width=4, height=2, command=lambda: inputCalc("8"))
nineButton = Button(window, text="9", bg="grey", fg="white", width=4, height=2, command=lambda: inputCalc("9"))
divisionButton = Button(window, text="/", bg="blue", fg="white", width=4, height=2, command=lambda: inputCalc("/"))

fourButton = Button(window, text="4", bg="grey", fg="white", width=4, height=2, command=lambda: inputCalc("4"))
fiveButton = Button(window, text="5", bg="grey", fg="white", width=4, height=2, command=lambda: inputCalc("5"))
sixButton = Button(window, text="6", bg="grey", fg="white", width=4, height=2, command=lambda: inputCalc("6"))
multiplicationButton = Button(window, text="*", bg="blue", fg="white", width=4, height=2, command=lambda: inputCalc("*"))

oneButton = Button(window, text="1", bg="grey", fg="white", width=4, height=2, command=lambda: inputCalc("1"))
twoButton = Button(window, text="2", bg="grey", fg="white", width=4, height=2, command=lambda: inputCalc("2"))
threeButton = Button(window, text="3", bg="grey", fg="white", width=4, height=2, command=lambda: inputCalc("3"))
subtractionButton = Button(window, text="-", bg="blue", fg="white", width=4, height=2, command=lambda: inputCalc("-"))

zeroButton = Button(window, text="0", bg="grey", fg="white", width=4, height=2,  command=lambda: inputCalc("0"))
decimalButton = Button(window, text=".", bg="grey", fg="white", width=4, height=2, command=lambda: inputCalc("."))
equalsButton = Button(window, text="=", bg="red", fg="white", width=4, height=2, command=lambda: getAnswer(resultsLBL.cget("text")))
additionButton = Button(window, text="+", bg="blue", fg="white", width=4, height=2, command=lambda: inputCalc("+"))

# End Buttons and Label creation

# Placing Buttons and Label in grid
clearButton.grid(row=0, column=0)
resultsLBL.grid(row=0, columnspan=4, sticky=E)
sevenButton.grid(row=1, column=0)
eightButton.grid(row=1, column=1)
nineButton.grid(row=1, column=2)
divisionButton.grid(row=1, column=3)

fourButton.grid(row=2, column=0)
fiveButton.grid(row=2, column=1)
sixButton.grid(row=2, column=2)
multiplicationButton.grid(row=2, column=3)

oneButton.grid(row=3, column=0)
twoButton.grid(row=3, column=1)
threeButton.grid(row=3, column=2)
subtractionButton.grid(row=3, column=3)

zeroButton.grid(row=4, column=0)
decimalButton.grid(row=4, column=1)
equalsButton.grid(row=4, column=2)
additionButton.grid(row=4, column=3)

# End of grid

window.mainloop()
