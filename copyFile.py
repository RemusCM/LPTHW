from sys import argv

from os.path import exists
#To properly get the size of a file.
import os
scriptName, fromFile, toFile = argv
#getsize uses a path, not the opened file.
size = os.path.getsize(fromFile)
print(f"The size of {fromFile} is {size} bytes long.")

openedFromFile = open(fromFile)

fromFileData = openedFromFile.read()

print(exists(toFile))

openedToFile = open(toFile, 'a+')

openedToFile.write(fromFileData)

print(f"the current contents of {toFile} are :")
openedToFile.seek(0)
print(openedToFile.read())

openedFromFile.close()
openedToFile.close()
