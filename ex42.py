#ex42, is-a, has-a relationships.

# Dog is-a Animal.
class Dog(Animal):

    def __init__(self, name):
        #Every dog has a name.
        self.name = name

# Cat is-a Animal
class Cat(Animal):

    def __init__(self,name):
        #Every Cat has-a name.
        self.name = name

#Person is-a Object.
class Person(object):

    def __init__(self, name):
        #Every Person has-a name.
        self.name = name

        #Person has-a pet of some kind
        self.pet = None

#Employee is-a Person
class Employee(Person):

    def __init__(self,name,salary):

        #Starting python 3, can write super.()__init__(name)
        #Every employee has-a name/is-a person.
        super.(Employee,self).__init__(name)
        #Every Employee has-a salary
        self.salary = salary


#Every Fish is an Object.
class Fish(object):
    pass

#Every Salmon is a Fish
class Salmon(Fish):
    pass

#Every Halibut is a Fish
class Halibut(Fish):
    pass

#rover is-a Dog.
rover = Dog('Rover')

#Sky is a Cat.
sky = Cat("Sky")

#Mary is a Person.
mary = Mar("Mary")

#mary has a pet named sky.
mary.pet = sky

#frank is a Employee/Person, has a salary of 12000, has a name of Frank.
frank = Employee("Frank", 12000)

#frank has a pet, rover.
frank.pet = rover

#flipper is a Fish.
flipper = Fish()

#crouse is a salmon is a fish.
crouse = Salmon()

#harry is a Halibut is a Fish
harry = Halibut()
