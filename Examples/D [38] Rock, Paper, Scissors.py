# A simple game of rock paper scissors where the player plays against a pseudo-random selection

import random

print("\nRock, Paper, Scissors\n")

def rps():
    choice = 1
    while 1 == 1:
        print("1. Rock\n2. Paper\n3. Scissors\n4. Quit\n")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("You have to enter a number!\n")
        
        aiChoice = random.randint(1, 3)

        if choice == aiChoice:
            print("It is a draw!\n")
        elif choice == 1 and aiChoice == 3:
            print("You Win!\n")
        elif choice == 1 and aiChoice == 2:
            print("You lose!\n")
        elif choice == 2 and aiChoice == 1:
            print("You win!\n")
        elif choice == 2 and aiChoice == 3:
            print("You lose!\n")
        elif choice == 3 and aiChoice == 1:
            print("You lose\n")
        elif choice == 3 and aiChoice == 2:
            print("You win!\n")
        elif choice == 4:
            quit()
        else:
            print("You have to choose an option.\n")

rps()
