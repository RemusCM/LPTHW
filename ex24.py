#The goal of this exercise was just to practice whatever we did so far.

from sys import argv

scriptName, fileName = argv

def infoToFile(fileName):
    #Append to existing file
    openedFile= open(fileName, 'a+')
    print("The current contents of the file are:", openedFile.read())
    name = input("Enter your name:")
    age = input("Enter your age:")
    #Can't concatenate string with ints, keep everything as string
    #Can't concatenate with commas in arguments, as it seems like different args
    openedFile.write(name+ " " + age + "\n")

    #Can't seek and read on the same line.
    openedFile.seek(0)
    print("The contents of the file are now:", openedFile.read(), "\n")


print(f"Welcome to the script {scriptName}")

#Don't forget to give arguments
infoToFile(fileName)
