#We learn how to import here
from sys import argv

#with argv, we can run programs with given arguments.
#Usually, the first argument is the script name.
script, firstName, lastName  = argv
#Don't forget to pass the same number of arguments when running it in the
#command line.
print("Script name: ", script)
print("First:", firstName)
#Can use the command line arguments whenever.
prompt = '>'
print(f"How old are you, {firstName}?")
age = int(input(prompt))
print(age)
print("Second:", lastName)
