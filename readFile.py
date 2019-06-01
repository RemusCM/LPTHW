from sys import argv

scriptName, fileName = argv

#Using argv
txtFile= open(fileName)

print(f"Reading from {fileName}")
print(txtFile.read())

#Using input
print("What is the name of the file you wish to read from?")
inputedFileName = input('>')

print(f"Opening file{inputedFileName}")
openedFile = open(inputedFileName)
print(f"Reading now from {openedFile}")
print(openedFile.read())
