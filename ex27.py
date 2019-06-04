#This exercise introduces logic/ truth values.

from sys import argv

scriptName = argv

print(f"Welcome to {scriptName}")

#Truth Terms

if (5+11 == 17):
    #this won't happen.
    print("Broken mathematics.")

if (True and True):
    print("True.")

if (True or False):
    print("True.")

if (not False or False):
    print("True.")

#evalutation of math terms is similar (<=, >= >,<)
