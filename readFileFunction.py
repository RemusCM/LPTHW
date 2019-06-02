#Ex.20, using functions to read a file.

from sys import argv

scriptName, fileName = argv

#This would only work on a file that has been opened, and
#has its cursor at 0! *Don't forget that read doesn't reset cursor
def print_file(file):
    print(file.read())

"""Can't read twice. Meaning, you cannot do the following.
openedFile = open(fileName)
print_file(openedFile.read()) #Cursor stays at the end of file.
print_file(openedFile.read())
"""
#This also works only on an opened file.
def rewind(file):
    file.seek(0)

#print one line at the time
def print_line(file):
    print(file.readline())

#On to the main part of the program (We haven't looked into main method, but
#I think it exists in python too)

openedFile = open(fileName)
print_file(openedFile)
rewind(openedFile)
print_file(openedFile)
print_file(openedFile) #This won't print the file, as the cursor is at the end.
#it will instead print an empty line. (pretty much a \n)
rewind(openedFile)
print_line(openedFile)
