#Ex 40, Modules, Classes, Objects
import ex40a

print("Can import custom made modules (py files with functions/variables)\nand access them with moduleName.whatYouWantToAccess")
print(list(ex40a.personDict.keys()))
for x in ex40a.personDict.keys():
    print(x)
print(ex40a.personDict.get("Remus"))
print(ex40a.personDict['John'])

john = ex40a.Employee('John', 'Doe')

print(str(john))
