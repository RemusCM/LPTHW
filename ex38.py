#Ex 38, Doing things to list.

from sys import argv

scriptName = argv

print(f"Welcome to {scriptName}, where we work more on lists.")

print("""
First, let's learn about the differences between append, extend, and concatenation( + ).
append adds the elements you want to the end of the list. if you append a list, Then
it is appended as its own item.
extend adds items individually ( if you extend a list, then it iterates through
every item within the list, and appends it to the list)
concatenation creates a new list with the addition of the selected items to add.
L = [1,2,3]
L + [2,4]
print(L) -> [1,2,3]
""")

list = [1,2,3]

#join only works on string
print ("-".join(str(x) for x in list))

for i in range(2):
    list.pop()
    print(list)
