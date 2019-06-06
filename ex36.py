#This exercise is used for practice.
#similar to 35, make my own game
#Game: Maze game, multiple doors, need of keys for some doors, one death trap

from sys import argv, exit
from playsound import playsound
import time
import os


scriptName = argv

print(f"Welcome to {scriptName}, a console maze game.")

def start():

    #initialize inventory:
    inventory = []
    print("You have arrived to the famous maze.")
    print("It is rumoured that people who reach the end of the maze are greatly rewarded.")
    print("Continue? (Y/N)")
    choice = input(">")

    if choice == "Y":
        print("You decide to go in.")
        while True:
            print("You can go left or right, which one will it be? (L/R)")
            choice = input(">")
            if choice == "R":
                print("You see an open door, leading to a room with open lights. Go in? (Y/N)")
                choice = input(">")
                if(choice == "Y"):
                        print("""
⣿⠿⣛⣯⣭⣭⣭⣭⣭⣭⣥⣶⣶⣶⣶⣶⣮⣭⣭⣭⣭⣭⡛⢻⣿⣿⣿⣿⣿⣿⣿
⡇⣾⣿⣿⣿⣿⣿⠿⢛⣯⣭⣭⣷⣶⣶⣶⣶⣶⣶⣶⣶⣬⣭⢸⣿⣿⣿⣿⣿⣿⣿
⢰⣶⣶⣶⣶⣶⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿
⡏⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⡿⢋⣩⠭⠭⡙⢋⣭⠶⠒⠒⢍⡘⠻⣿⣿⣿⣿⣿⣿
⡇⣿⣿⣿⣿⣿⢸⣿⣿⡿⣋⣴⣯⡴⠚⠉⡡⠤⢄⣉⣅⡤⠄⢀⢺⡌⣻⣿⣿⣿⣿
⡇⣿⣿⣿⣿⣿⢸⣿⡏⡆⣿⣿⣉⣐⢴⣿⠈⠈⢀⠟⡿⠷⠄⢠⢎⢰⣿⣿⣿⣿⣿
⡇⣿⣿⣿⣿⣿⢸⣿⢸⣿⣿⣿⡫⣽⣒⣤⠬⠬⠤⠭⠭⢭⣓⣒⡏⣾⣿⣿⣿⣿⣿
⡇⣿⣿⣿⣿⣿⢸⡿⢸⣿⣿⣿⣿⣷⣾⣾⣭⣭⣭⣭⣭⣵⣵⡴⡇⠉⠹⣿⣿⣿⣿
⡇⣿⣿⣿⣿⣿⢸⠠⠄⠉⠉⠛⠛⠛⠛⠛⠊⠉⠉⠉⠉⠁⠄⠄⠄⠠⢤⡸⣿⣿⣿
⢇⡻⠿⣿⣿⣿⠘⣠⣤⣤⣀⡚⠿⢦⣄⡀⠤⠤⠤⣤⣤⣤⣤⣤⣤⣄⣘⠳⣭⢻⣿
⣎⢿⣿⣶⣬⣭⣀⠛⢿⣿⣿⣿⣷⣶⣬⣙⡳⠟⢗⣈⠻⠛⠛⠛⠛⢿⣿⣿⣦⢸⣿
⣿⣆⢿⣿⣿⣿⣽⣛⣲⠤⠤⢤⣤⣤⣤⣀⡙⣿⣿⣿⠇⣤⣤⣤⡶⢰⣿⣿⠃⣼⣿
⣿⣿⣆⢿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⡖⣸⣿⡟⣠⣶⣶⡖⣠⣿⡿⣡⣾⣿⣿
⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣽⣛⣛⡻⣿⠇⣿⣿⠃⣿⣟⡭⠁⣿⣯⣄⢻⣿⣿⣿
⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣷⣭⣙⠗⣸⣿⡇⣾⣮⣙⡛⣸⣿⣿⣿

        """)
                        print("You find a rare pepe taking a massive one. Let's get out.")

                        continue
                else:
                    #Did not write Y to go in, continue to go back to start
                    continue
            elif choice == "L":
                print("The door is wide open, you go in.")
                foundSKey = False
                foundCarrot = False
                while True:
                    print("You now have three choices; continue straight ahead, turn left, or turn right.(S/L/R)")
                    choice = input(">")
                    if choice == 'S':
                        print("You come to a door that is locked")
                        print("Checking your inventory for needed key")
                        if 'sKey' in inventory:
                            print("You have the key, door is opened. You go in.")
                            print("You see someone blocking a huge gate")
                            print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣧⠀⠀⠀⢰⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡟⡆⠀⠀⣿⡇⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⣿⠀⢰⣿⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄⢸⠀⢸⣿⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡇⢸⡄⠸⣿⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⢸⡅⠀⣿⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣥⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡿⡿⣿⣿⡿⡅⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠉⠀⠉⡙⢔⠛⣟⢋⠦⢵⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣄⠀⠀⠁⣿⣯⡥⠃⠀⢳⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡇⠀⠀⠀⠐⠠⠊⢀⠀⢸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⡿⠀⠀⠀⠀⠀⠈⠁⠀⠀⠘⣿⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⡀⠀⠀⠀
⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣧⠀⠀
⠀⠀⠀⡜⣭⠤⢍⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢛⢭⣗⠀
⠀⠀⠀⠁⠈⠀⠀⣀⠝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠠⠀⠀⠰⡅
⠀⠀⠀⢀⠀⠀⡀⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠔⠠⡕⠀
⠀⠀⠀⠀⣿⣷⣶⠒⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠊⠉⢆⠀⠀⠀⠀
⠀⢀⠤⠀⠀⢤⣤⣽⣿⣿⣦⣀⢀⡠⢤⡤⠄⠀⠒⠀⠁⠀⠀⠀⢘⠔⠀⠀⠀⠀
⠀⠀⠀⡐⠈⠁⠈⠛⣛⠿⠟⠑⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⠑⠒⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

                            """)
                            print("Bunny: Uhhh, what's up doc?")
                            if 'carrot' not in inventory:
                                print("""You have a few options:
                                1. Ask him to let you in.
                                2. Go back.
                                (1/2) """)
                                choice = input(">")
                                if choice == "1":
                                    print("Boi you messed up; can't be talking to a bunny like that.")
                                    print("The bunny slaps you right out")
                                    print("""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠻⠿⣿⣿⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠟⠉⠄⠄⠄⠄⠄⠄⠄⠉⢟⠉⠄⠄⠄⠄⠄⠈⢻⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠃⠄⠄⠤⠐⠉⠉⠉⠉⠉⠒⠬⡣⠤⠤⠄⠄⠄⠤⠤⠿⣿⣿⣿⣿
⣿⣿⣿⣿⠁⠄⠄⠄⠄⠄⠄⠠⢀⡒⠤⠭⠅⠚⣓⡆⡆⣔⡙⠓⠚⠛⠄⣹⠿⣿
⣿⠟⠁⡌⠄⠄⠄⢀⠤⠬⠐⣈⠠⡤⠤⠤⣤⠤⢄⡉⢁⣀⣠⣤⣤⣀⣐⡖⢦⣽
⠏⠄⠄⠄⠄⠄⠄⠄⠐⠄⡿⠛⠯⠍⠭⣉⣉⠉⠍⢀⢀⡀⠉⠉⠉⠒⠒⠂⠄⣻
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠩⠵⠒⠒⠲⢒⡢⡉⠁⢐⡀⠬⠍⠁⢉⣉⣴⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⢉⣒⡉⠁⠁⠄⠄⠉⠂⠙⣉⣁⣀⣙⡿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⢠⠄⡖⢉⠥⢤⠐⢲⠒⢲⠒⢲⠒⠲⡒⠒⡖⢲⠂⠄⢀⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠈⢆⡑⢄⠳⢾⠒⢺⠒⢺⠒⠚⡖⠄⡏⠉⣞⠞⠁⣠⣾⣿
⠄⠄⠄⠄⠄⠄⢆⠄⠄⠄⠈⠢⠉⠢⠍⣘⣒⣚⣒⣚⣒⣒⣉⠡⠤⣔⣾⣿⣿⣿
⠷⣤⠄⣀⠄⠄⠄⠈⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣤⣾⣿⣿⣿⣿⣿
⠄⠄⠉⠐⠢⠭⠄⢀⣒⣒⡒⠄⠄⠄⠄⠄⠄⣀⡠⠶⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠁⠈⠄⠄⠄⠄⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⣿""")
                                    exit(0)
                                else:
                                    print("You go back")
                                    continue
                            else:
                                print("""You have a few options:
                                1. Ask him to let you in.
                                2. Go back.
                                3. Subdue the filthy rabbit with the carrot you have in your inventory.
                                (1/2/3) """)
                                choice = input(">")
                                if choice == "1":
                                    print("Boi you messed up; can't be talking to a bunny like that.")
                                    print("The bunny slaps you right out")
                                    print("""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠻⠿⣿⣿⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠟⠉⠄⠄⠄⠄⠄⠄⠄⠉⢟⠉⠄⠄⠄⠄⠄⠈⢻⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠃⠄⠄⠤⠐⠉⠉⠉⠉⠉⠒⠬⡣⠤⠤⠄⠄⠄⠤⠤⠿⣿⣿⣿⣿
⣿⣿⣿⣿⠁⠄⠄⠄⠄⠄⠄⠠⢀⡒⠤⠭⠅⠚⣓⡆⡆⣔⡙⠓⠚⠛⠄⣹⠿⣿
⣿⠟⠁⡌⠄⠄⠄⢀⠤⠬⠐⣈⠠⡤⠤⠤⣤⠤⢄⡉⢁⣀⣠⣤⣤⣀⣐⡖⢦⣽
⠏⠄⠄⠄⠄⠄⠄⠄⠐⠄⡿⠛⠯⠍⠭⣉⣉⠉⠍⢀⢀⡀⠉⠉⠉⠒⠒⠂⠄⣻
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠩⠵⠒⠒⠲⢒⡢⡉⠁⢐⡀⠬⠍⠁⢉⣉⣴⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⢉⣒⡉⠁⠁⠄⠄⠉⠂⠙⣉⣁⣀⣙⡿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⢠⠄⡖⢉⠥⢤⠐⢲⠒⢲⠒⢲⠒⠲⡒⠒⡖⢲⠂⠄⢀⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠈⢆⡑⢄⠳⢾⠒⢺⠒⢺⠒⠚⡖⠄⡏⠉⣞⠞⠁⣠⣾⣿
⠄⠄⠄⠄⠄⠄⢆⠄⠄⠄⠈⠢⠉⠢⠍⣘⣒⣚⣒⣚⣒⣒⣉⠡⠤⣔⣾⣿⣿⣿
⠷⣤⠄⣀⠄⠄⠄⠈⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣤⣾⣿⣿⣿⣿⣿
⠄⠄⠉⠐⠢⠭⠄⢀⣒⣒⡒⠄⠄⠄⠄⠄⠄⣀⡠⠶⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠁⠈⠄⠄⠄⠄⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⣿""")
                                    exit(0)
                                elif choice == "2":
                                    print("You go back.")
                                    continue
                                elif choice == "3":
                                    print("You give the carrot to the rabbit.")
                                    print("The rabbit is happy, and lets you pass through.")
                                    print("Seems like you reached the end already! You ready for your prize? (Y/N)")
                                    choice = input(">")
                                    if choice == "Y":
                                        os.system('cls')
                                        playsound("u got that.mp3", False)
                                        print("Loading prize...")
                                        time.sleep(17)
                                        for x in range(25):
                                            print("""
⠄⠄⠄⠄⠄⠄⢴⡶⣶⣶⣶⡒⣶⣶⣖⠢⡄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⢠⣿⣋⣿⣿⣉⣿⣿⣯⣧⡰⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⣿⣿⣹⣿⣿⣏⣿⣿⡗⣿⣿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠟⡛⣉⣭⣭⣭⠌⠛⡻⢿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⣤⡌⣿⣷⣯⣭⣿⡆⣈⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⣿⣿⣿⣿⣷⢛⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⢻⣷⣽⣿⣿⣿⢿⠃⣼⣧⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣛⣻⣿⠟⣀⡜⣻⢿⣿⣿⣶⣤⡀⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⢠⣤⣀⣨⣥⣾⢟⣧⣿⠸⣿⣿⣿⣿⣿⣤⡀⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⢟⣫⣯⡻⣋⣵⣟⡼⣛⠴⣫⣭⣽⣿⣷⣭⡻⣦⡀⠄
⠄⠄⠄⠄⠄⠄⠄⢰⣿⣿⣿⢏⣽⣿⢋⣾⡟⢺⣿⣿⣿⣿⣿⣿⣷⢹⣷⠄
⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⢣⣿⣿⣿⢸⣿⡇⣾⣿⠏⠉⣿⣿⣿⡇⣿⣿⡆
⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⢸⣿⣿⣿⠸⣿⡇⣿⣿⡆⣼⣿⣿⣿⡇⣿⣿⡇
⠇⢀⠄⠄⠄⠄⠄⠘⣿⣿⡘⣿⣿⣷⢀⣿⣷⣿⣿⡿⠿⢿⣿⣿⡇⣩⣿⡇
⣿⣿⠃⠄⠄⠄⠄⠄⠄⢻⣷⠙⠛⠋⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⡇⣿⣿⡇
                                            """)
                                            time.sleep(0.5)
                                            os.system('cls')
                                            for j in range(5):
                                                time.sleep(0.5)
                                                os.system('cls')

                                                print("""
    ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣀⣤⣴⣶⣾⣆⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⣤⣤⣤⠄⢤⣴⣶⣿⣿⣿⢟⣿⣿⣿⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⣀⣠⣤⡾⢏⢠⣶⣶⣾⡑⡀⢸⠋⠁⠄⢠⣾⣿⣿⣿⠄⠄⠄⠄⠄
    ⠄⢀⣠⣶⣿⣿⣿⠟⠁⠁⠰⣋⢫⢲⡇⠛⠄⠄⢀⣠⣤⣉⠻⠿⠿⠄⠄⠄⠄⠄
    ⢰⣿⣿⣟⣋⣉⣁⠄⠄⠄⠄⠻⣆⣂⡕⠼⠂⠉⣿⣿⡇⢏⠉⠉⠁⠄⠄⠄⠄⠄
    ⠄⠙⢿⣿⣿⣿⣿⠃⢸⢋⡁⢊⠒⣲⡶⠊⢁⣴⣿⣿⣿⣦⣦⠄⠄⠄⠄⠄⠄⠄
    ⠄⠄⠄⠙⠻⣿⡟⠄⡆⢸⣧⣾⣶⣤⣤⣾⡿⣿⣿⠿⡻⣻⣿⠁⠄⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⠄⠄⠘⠠⣾⣿⣿⡿⠿⠿⣥⣾⣿⠿⣛⠅⢰⣗⠄⠄⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠸⣶⣶⣿⣟⣛⣛⣛⠲⠿⣵⣿⣟⢅⠂⠄⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢹⡟⠋⣠⣤⣤⣤⣍⡑⠂⠬⢉⣾⠄⠄⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢠⠁⣿⣿⣿⣿⠿⠿⠿⠿⠷⢶⡄⠄⠄⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠄⢉⣁⣀⣤⣤⣤⣤⣤⣤⣤⠄⠄⠄⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⠈⠙⠿⣿⣿⣿⣿⡍⠟⢁⣠⣤⣶⣶⣤⣄⡀⠄⠄⠄
    ⠄⠄⠄⠄⠄⠄⠄⢀⣾⣿⣿⣷⣦⣀⠉⠿⣿⡇⠄⣾⣿⣿⣿⣿⣿⣿⣿⣶⡀⠄
    ⠄⠄⠄⠄⠄⠄⢠⣾⣿⣿⣿⣿⣿⣿⣷⡄⠹⠇⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄
    ⠄⠄⠄⠄⠄⠄⣾⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⠈⠙⠿⢿⣿⣿⣿⣿⣿⣿⣿⡇      """)

                                                time.sleep(0.5)
                                                os.system('cls')



                                                print("""
⠄⠄⠄⠄⠄⣆⣾⣶⣴⣤⣀⢀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⣿⣿⣿⢟⣿⣿⣿⣶⣴⢤⠄⣤⣤⣤⠠⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⣿⣿⣿⣾⢠⠄⠁⠋⢸⡀⡑⣾⣶⣶⢠⢏⡾⣤⣠⣀⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠿⠿⠻⣉⣤⣠⢀⠄⠄⠛⡇⢲⢫⣋⠰⠁⠁⠟⣿⣿⣿⣶⣠⢀⠄
⠄⠄⠄⠄⠄⠁⠉⠉⢏⡇⣿⣿⠉⠂⠼⡕⣂⣆⠻⠄⠄⠄⠄⣁⣉⣋⣟⣿⣿⢰
⠄⠄⠄⠄⠄⠄⠄⣦⣦⣿⣿⣿⣴⢁⠊⡶⣲⠒⢊⡁⢋⢸⠃⣿⣿⣿⣿⢿⠙⠄
⠄⠄⠄⠄⠄⠄⠁⣿⣻⡻⠿⣿⣿⡿⣾⣤⣤⣶⣾⣧⢸⡆⠄⡟⣿⠻⠙⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⣗⢰⠅⣛⠿⣿⣾⣥⠿⠿⡿⣿⣿⣾⠠⠘⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠂⢅⣟⣿⣵⠿⠲⣛⣛⣛⣟⣿⣶⣶⠸⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⣾⢉⠬⠂⡑⣍⣤⣤⣤⣠⠋⡟⢹⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⡄⢶⠷⠿⠿⠿⠿⣿⣿⣿⣿⠁⢠⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⣤⣤⣤⣤⣤⣤⣤⣀⣁⢉⠄⠘⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⡀⣄⣤⣶⣶⣤⣠⢁⠟⡍⣿⣿⣿⣿⠿⠙⠈⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⡀⣶⣿⣿⣿⣿⣿⣿⣿⣾⠄⡇⣿⠿⠉⣀⣦⣷⣿⣿⣾⢀⠄⠄⠄⠄⠄⠄⠄
⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢰⠇⠹⡄⣷⣿⣿⣿⣿⣿⣿⣾⢠⠄⠄⠄⠄⠄⠄
⡇⣿⣿⣿⣿⣿⣿⣿⢿⠿⠙⠈⠄⠄⠋⡿⣿⣿⣿⣿⣿⣿⣿⣾⠄⠄⠄⠄⠄⠄""")
                                            time.sleep(0.5)
                                            os.system('cls')

                                            print("""
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡄⠢⣖⣶⣶⡒⣶⣶⣶⡶⢴⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡰⣧⣯⣿⣿⣉⣿⣿⣋⣿⢠⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠁⣿⣿⡗⣿⣿⣏⣿⣿⣹⣿⣿⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⢿⡻⠛⠌⣭⣭⣭⣉⡛⠟⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣈⡆⣿⣭⣯⣷⣿⡌⣤⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢛⣷⣿⣿⣿⣿⣿⣿⣿⢻⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀⣧⣼⠃⢿⣿⣿⣿⣽⣷⢻⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⡀⣤⣶⣿⣿⢿⣻⡜⣀⠟⣿⣻⣛⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⡀⣤⣿⣿⣿⣿⣿⠸⣿⣧⢟⣾⣥⣨⣀⣤⢠⠄⠄⠄⠄⠄⠄⠄⠄
⠄⡀⣦⡻⣭⣷⣿⣽⣭⣫⠴⣛⡼⣟⣵⣋⡻⣯⣫⢟⠄⠄⠄⠄⠄⠄⠄⠄
⠄⣷⢹⣷⣿⣿⣿⣿⣿⣿⢺⡟⣾⢋⣿⣽⢏⣿⣿⣿⢰⠄⠄⠄⠄⠄⠄⠄
⡆⣿⣿⡇⣿⣿⣿⠉⠏⣿⣾⡇⣿⢸⣿⣿⣿⢣⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄
⡇⣿⣿⡇⣿⣿⣿⣼⡆⣿⣿⡇⣿⠸⣿⣿⣿⢸⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄
⡇⣿⣩⡇⣿⣿⢿⠿⡿⣿⣿⣷⣿⢀⣷⣿⣿⡘⣿⣿⠘⠄⠄⠄⠄⠄⢀⠇
⡇⣿⣿⡇⣿⣿⣿⣶⣷⣿⣿⣿⣿⣿⠋⠛⠙⣷⢻⠄⠄⠄⠄⠄⠄⠃⣿⣿ """)
                                            time.sleep(0.5)
                                            os.system('cls')


                                        exit()

                                    else:
                                        print("Write a correct number.")
                                        continue


                        else:
                            print("You don't have the key, maybe you forgot something. You go back.")
                            continue

                    if choice == 'L':
                        if not foundSKey:
                            foundSKey = True
                            print("You found a key. You put it in your inventory.")
                            inventory.append('sKey')
                            print("Going back")
                            continue
                        else:
                            print("Nothing left to do here, going back.")
                            continue

                    if choice == 'R':
                        if not foundCarrot:
                            foundCarrot = True
                            print("You found a carrot, I don't know it's use, but let's pick it up.")
                            inventory.append('carrot')
                            print("Going back")
                            continue
                        else:
                            print("Nothing left to do here, going back.")
                            continue



            else:
                print("Wrong input")
                continue

        else:
            print("Wise.")
            exit(0)

start()
