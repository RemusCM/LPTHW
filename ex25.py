#This exercise serve for more practice, only that this time around,
#we import the program's methods in powershell, and use them there
#(No calls in the program)

from sys import argv

scriptName = argv

def printThis(stringToPrint):
    print(stringToPrint)

def mult(numb1, numb2):
    print(int(numb1)*int(numb2))

"""To call functions in powershell, import ex25 (no need to add
.py extension)
Then, whenever you want to call a function, all we need to do is
ex25.functionName(args)
Otherwise, can write from ex25 import * to not have to write ex25 everytime
Other functions taught are split, sorted, and pop
"""
