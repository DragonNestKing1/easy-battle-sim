from sys import exit
from os import system

import battle

while True:
    system("cls")
    print("WELCOME TO BATTLE SIM")

    print("1. Start New Game\n2.Load Game\n3. Options\n4. Quit")
    choice = input("\n\n>> ")

    system("cls")
    if choice == "1":
        battle.start()
    elif choice == "2":
        print("Load Game")
        input()
    elif choice == "3":
        print("Show Options")
        input()
    elif choice == "4":
        system("cls")
        exit(0)
    else:
        input("Please select one of the four options... Enter to continue")