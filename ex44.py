#Ex44, inheritance vs composition.
#Three different ways to use inheritance.

from sys import argv

scriptName = argv

print(f"Welcome to {scriptName}, inheritance vs Composition.")

print("""
You have three types of inheritance:
1. Inherit and use parents' methods.
2. Inherit, but override parent's methods.
3. Inherit, override and use parents' methods.
Here are examples of each one.
""")

class Parent(object):

    def __init__(self, name):
        self.name = name
#Don't forget, if you use self inside of a method, it needs to be
#stated inside the method arguments.
    def callName(self):
        print(f"PARENT {self.name}")

class Child(Parent):
    def __init__(self, name):
        self.name = name
#Override + use of old
    def callName(self):
        print(f"CHILD {self.name}")
        #how to call super in python. This way is more specific to
        #multiple inheritance. Here, you don't need the arguments.
        super(Child, self).callName()

p = Parent("Super")
c = Child("Duper")

p.callName()
c.callName()


#Composition
print("""
For composition, it would seem that it does the same thing as inheritance,
and it is preferred. To make it work, from my understanding, it is to use
instance variables of a class, and assign another class to it.
e.x. Class A has a instance variable type_of_wheels, and we assign the cool_wheel
class to it. self.type_of_wheels=cool_wheel(). In this case, we don't need
a argument in the __init__ function.
""")

class CoolWheel(object):

    def __init__(self,name):
        self.name = name

    def callName(self):
        print(f"CoolWheel {self.name}")

class Car(object):

    def __init__(self,name):
        self.name = name
        self.wheelSet = CoolWheel("Super cool")

    def implicitCallName(self):
        self.wheelSet.callName()

    def overrideCallName(self):
        print(f"Car {self.name}")

    def bothCallName(self):
        self.wheelSet.callName()
        print("along with other functionality")
        self.overrideCallName()

car = Car("Audi")
car.implicitCallName()
car.overrideCallName()
car.bothCallName()
