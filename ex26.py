#Ex26's goal is to fix broken code
#To find errors faster, we can run the program multiple times.
from sys import argv

print("How old are you?", end=' ')
age = input()
#Thirtheenth error, never ask how tall.
print("How tall are you?", end=' ')
height = input()
#first error, missing a closing )
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

#Fourthteenth error, don't forget to include a text file, never imported
script, filename = argv

#17th Error, wrong name
txt = open(filename)
#Fifteenth Error, not formatted with f
print(f"Here's your file {filename}:")
#Sixteenth Error, txt, not tx
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

#18th txt_again_read is not a method.
print(txt_again.read())

#Second error, didn't escape the '
print('Let\'s practice everything.')
#Third error, can't skip line with the same command
#Can either use triple """, or put on same line.
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
#Fourth Error, missing quotes. Harder to fix with """
print("--------------")
print(poem)
print("--------------")

#Fifth error, extra symbol, or missing number. since it says it should be 5,
#missing 6, also missing a closing parenthesis )
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

#Sixth error, missing : to start definition of method
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    #Seventh error, missing an operator
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
#19th error, missing third return value
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
#20th Error, missing _ for startpoint
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
#21st error, cats, not cates
cats = 30
dogs = 15

#Eighth error, missing parenthesis over the print
if people < cats:
    print ("Too many cats! The world is doomed!")

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

#Ninth error, missing : for if statement
if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

#Tenth error, missing : for if statement
if people <= dogs:
    #Eleventh error, missing " for the print
    print("People are less than or equal to dogs.")

#Twelveth Error, to check equality, ==
if people == dogs:
    print("People are dogs.")
