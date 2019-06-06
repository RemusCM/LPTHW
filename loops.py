#Ex 32-33-34, loops and lists.

from sys import argv

scriptName = argv

print(f"Welcome to {scriptName}")

#Making lists
hairColor = ['Black', 'Blonde', 'Red']
eyeColor = ['Blue', 'Green', 'Brown']

#Most used for loop, similar to for each loop in Java.
for x in hairColor:
    print(x)
    print(eyeColor) #Prints the array.

#For-Loop as known in Java
for x in range(6): #Can also have a begining, range(2,6)
    print(x) #Starts at 0, ends at range(y) -> y-1

#Adding elements to a list.
list = []
for x in range(6):
    list.append(x)
print(list)

#The + sign comes from __add__ method from my understanding.
for x in range(6,7):
    list = list + list

print(list)

i=0
#While loops
while(list[i]<4):
    print(list[i])
    i+=1
