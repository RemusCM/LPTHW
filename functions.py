#Ex18, teaches how to create functions, and the different ways to capture arguments.

#Using a variable number of arguments.
#In this case, we'll only use two args in the method
#I believe there is a way to use this to dynamically assign variables
#at runtime, but I'll that qu
def print_two_times(*args):
    arg1, arg2 = args
    print(f"Well, the first argument is {arg1} and the second is {arg2}")
#Can have different types of arguments.
print_two_times("Remus", 22)

#If we'd want to have a variable number of arguments
#we need to use the for loop; we haven't learned about it yet, but who cares.
def print_x_times(*args):
    for arg in args:
        print(arg, end = ' ')
    print("")

print_x_times("Hi,","my name is", "Remus" )

#If we know the number of arguments, then we don't need *args
def print_twice(arg1, arg2):
    print(arg1)
    print(arg2)

print_twice("This", "Works")

#Ex19 Other function attributes
#Can give arguments directly, as previously
print_two_times("Hi", "again")

#can give variables as arugments
word1 = "hi"
word2 = "bye"
print_two_times(word1, word2)

#can do mathinside the arguments, though I don't really see the use of this.
print_two_times(10+7, 7+10)

#or a mix f varibales and math.
numb = 10
numb2 = 7
print_two_times(numb+numb2, numb2+numb)

print("Give me a number")
numb3 = int(input())

print_two_times(numb3,numb3)

#Can even ask inputs in the arguments! This is very interesting.
print_two_times(int(input()), int(input()))
