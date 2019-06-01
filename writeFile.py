from sys import argv

scriptName, fileName = argv
#Don't forget to add the writing privilege to the file, using the
#second argument. the w privilege automatically truncates the file. Need to use
#the 'a' privilege to only append on top of existing lines.
#To understand how to use modes, go to
#https://bit.ly/1xtuwG9
openedFile = open(fileName, 'a+')


openedFile.write(
f"""I am writing to this file using the {scriptName} script.
And you can write as a paragraph.\n""")

print("Here are the current contents of the file:")
#Because of a+, the index is set to the end of the file. need to Seek back to 0.
openedFile.seek(0)
print(openedFile.read())
