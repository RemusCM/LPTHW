#We learn how to import here
from sys import argv

#with argv, we can run programs with given arguments.
#Usually, the first argument is the script name.
script, first, second = argv
#Don't forget to pass the same number of arguments when running it in the
#command line.
print("Script name: ", script)
print("First:", first)
#Can use the command line arguments whenever.
age = int(input("age?"))
print(age)
print("Second:", second)
