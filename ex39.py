#Ex39, Dictionaries.

from sys import argv

scriptName = argv

print(f"Welcome to {scriptName}, an exercise on Dictionaries.")
print("""
Dictionaries are a data structure that allows to store pretty much anything as a database.
The way to define a dictionary(dict) dictName = {'name': 'Remus', 'age': '22'}.
You can access anything inside the dictionary with dictName['name'].
""")

dictOfPersonAges = {'Remus': '22', 'Abdo': '23', 'Sofiane': '24'}

print(dictOfPersonAges)
print("Printing Remus' age with dictOfPersonAges['Remus']")
print(dictOfPersonAges['Remus'])
print("Can also use for loops on every key,value pair with loops, \nusing for key, value in list(dictName.items)")
for name, age in list(dictOfPersonAges.items()):
    print(name, "is", age , "years old")
print("Deleting Sofiane from the dictionary with del dictOfPersonAges['Sofiane']")
del dictOfPersonAges['Sofiane']
print(dictOfPersonAges)
print("Can also use pop like this : dictOfPersonAges.pop('Abdo')")
dictOfPersonAges.pop('Abdo')
print(dictOfPersonAges)

#other functions include len, values, keys, pop, popitem, get, copy, clear, setitem.
#ordered dictionaries : collections.OrderedDict()
