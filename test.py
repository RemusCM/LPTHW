#This is a regular comment.
#For multiline comments, you can use """ whatever-comment """
"""print("Hi")
print("Hi again")
print("How you doin'?")"""
print("Learning Python")

#Can set variables easily, no need to define what type of variable it is as
#in Java.
s = "This is a string."
print(s)

#modulo,  Better than Java, works as expected with negative numbers as well.
print((-5)%2)
#Can print true/false, evaluate things inside print.
print(5>2)
print(5>6)

cars = 100
space_in_car = 4.0

#will convert int to double automatically, no need  for casting.
print(cars/space_in_car)

name = "Remus"
age = 22

#There are different ways of formatting strings.
#The first way, we have knowledge about variables to be used inside
#the string.
print(f"My Name is {name} and I am {age} years old")
print(f"In less than a month, I will be {age+1} years old.")

#Can also save the formatted string without the use of print, and use it later
#as a variable
fString = f"My Name is {name} and I am {age} years old"

print(fString)

#Very interesting; if you would like to have a string with {}
#But with nothing inside the {}, meaning you are waiting for something
#To be put inside of the brackets, then you would want to use
#the format() function, which takes in as parameter the variable.
#Example:

toFormat = "Am I funny? {}"

answer = False

print(toFormat.format(answer))

#This is pretty hard grasp, so I will do another example.

toFormat2 = "Is it raining outside? {}"

answer2 = True
print(toFormat2.format(answer2))

#Can format with other strings, not necessarily booleans. I guess it would work
#with any kind of variable.
toFormat3 = "Can format with other types of variables? {}"
answer3 = "Yes, here is a test with a string."

print(toFormat3.format(answer3))

toFormat4 = "How old am I? {}"
answer4 = 22

print(toFormat4.format(answer4))

#Can round with the round function
print(round(1.7555, 2))

#Can copy string multiple strings one next to the other with multiplication
print("." * 10)

#Same line prints
w1 = "cheese"
w2 = "burger"
print(w1, end=' ')
print(w2)

"""
In python 2, instead of doing end =  ' '
we could've done
print(w1),
print(w2)
"""
