#Ex37-> Symbols # REVIEW: all the different keywords seen so far.
#In the table shown, there are many that weren't discussed yet.
#with keyword; used as syntactic surgar for try..finally blocks.
#need to import it first.
from __future__ import with_statement
#as keyword, can rename, as in sql.
import time as t

from sys import argv


#Different boolean expressions.
numb = int(input("Input a number."))
numbList = [8,17,21]
if (numb < 10 or numb > 100):
    print("Out of bounds")
elif (numb != 13 and numb < 20):
    print("Lucky.")
elif(numb not in numbList):
    print('not in list')
else:
    print(numb)

numb = int(input("Write 17"))
#Used more when debugging code.
assert numb == 17, "should be 17."

class favNumber:
    numb = 17
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printFav(self): #if an object calls the function, then it is considered
                        #as the object taking a parameter self.
        global numb #refer to global numb, not the one created locally.
        print(numb, self.name, self.age)


x = favNumber("Remus", 22)
x.printFav()


#del keyword; can delete an object, a class, a variable, an item from list.
print(numbList)
del numbList[0]
print(numbList)

#exec; executes a string as python code.
exec ('print("Hello world")')

#try&except;

try:
    exception = 5+"catches exception"
except:
    print("wrong.")
    #can create your own exceptions by making classes or exception name, Exception/Error arg, pass body.
    #commented out due to never completing the program.
    #raise ValueError("Can't add an integer with a string.")
finally:
    print("Good job.")

#is
print(1 is 1) #same as == pretty much. is looks at if same object, == looks at contents

#lambda functions; small anonymous functions, can take many arguments.
x = lambda a : a+10
print(x(5)) #5+10 = 15.

#custom exception
class WrongFormat(Exception):
    pass

try:
    exception = 5
    if exception < 10:

        raise WrongFormat("Wrong format.") #use raise where it could possibly fail
                                            #define what to do in case of exception
                                            #in except block.
except WrongFormat:
    print("Well hello there, wrong format caught.")
finally:
    print("This happens, exceptions or not.")

print("Continuing.")



openedFile = open('readExample.txt', 'r')
#with keyword, not really sure the use of with. Says to be used with unmanaged resources.
with openedFile as in_file:
    print(in_file.read())

#yield keyword; used like return, but returns generators, iteratables that can be
#iterated over only once.
def createGenerator():
    mylist = range(3) #make a list.
    for i in mylist:
        yield i*i #this is what returns a generator.

myGen = createGenerator()
print(myGen) #prints address
for i in myGen:
    print(i)


#dicts -> mappings between keys and values.
dict = {'a':1, 'b':2}
print(dict)
print(dict.get('a'))

#at, decorators, @classmethod, @staticmethod.
#Class methods can be used to different types of constructors,
#or setters/getters for an entire class. Ex: imagine increasing
#interest rate from 4% to 5% for some future clients (not all, the base
#constructor stays at 4%)

class Client:
    interest_rate = 1.04

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'Name: %s \n Age: %s \n Interest Rate: %s ' % (self.name, self.age, self.interest_rate)

    @classmethod
    def set_interest_rate(cls,ir):
        cls.interest_rate = ir



c1 = Client("Remus", 22)

print(str(c1))

Client.set_interest_rate(1.05)

c2 = Client("Bob", 17)


print(c2)

#bytes data type:
byte = b"\xe4\xb8\xad\xe6\x96\x87"

print(byte)

#if you just want the actual string, need to decode, recall ex23
print(byte.decode("utf-8"))
