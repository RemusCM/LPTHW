#Ex29, The if statement.

import sys
#seems like it saves it in an array this time around.
scriptName = sys.argv

print(f"Welcome to {sys.argv[0]}")

def hasNumber(string):
    return any(char.isdigit() for char in string)

name = input("What is your name?")

if(hasNumber(name)):
    print("Since when can names have numbers? Exiting.")
    exit()
else:
    print(f"Have a good day, {name}.")

#spent a long time figuring out global variables, need to define initially.
guess = 0

def guessNumb():
    #Really need to define as global guess, and can't do it on the same line
    """Another way to get global is using x = globals()['nameOfVar']
    That would allow to have a local variable with the same name"""
     global guess
     guess = int(input("Guess a number"))

guessNumb()
#Used while loop, even though didn't see it yet.
while(guess != 17):
    if(guess < 17):
        print("Guess a larger number")
        guessNumb()
    else:
        print("Guess a smaller number")
        guessNumb()
