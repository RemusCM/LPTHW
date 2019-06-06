#Branches and functions; wrote this exercise completely, it's more to understand
#how the program works, rather than how different functions work.
from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
#Not sure what the point of this was..
#Like I can't pick numbers without them having a 0 or a 1 in them?
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has honey.")
    print("The bear is in front of the door.")
    print("How are you going to move the bear?")
    print("""
    1. Take honey
    2. Taunt bear
    3. Open door
    """)
    bear_moved = False

    while True:
        choice = input(">")

        if choice == "1":
            dead("The bear looks at you and slaps your face.")
        elif choice == "2":
            print("Bear moved from the door")
            print("You can now go through the door.")
            bear_moved = True
        elif choice == "3":
            if bear_moved == False:
                print("How are you going to open the door with a bear in front of it?")
                print("Pick Again.")
            else:
                gold_room()
        else:
            print("Pick a valid number.")

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room. You have two paths, you decide to go to the left.")
    bear_room()

start()
