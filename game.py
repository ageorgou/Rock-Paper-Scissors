# rock paper scissors game
import numpy as np
from enum import IntEnum
import random

# creating enum for hand gestures in rock, paper, scissors
class Hand(IntEnum):
    rock=1
    paper=2
    scissors=3

isGameOver = False

print("Welcome to our game")
count = 1
while not isGameOver:
    print("Choose either rock,paper or scissors")
    keyboard_input = input()
    count = count + 1
    
    """
    First player choice and reassigning user_input variable
    into a integer for later comparison
    """
    hasUserChosenCorrectly = False
    for option in Hand:
        if keyboard_input == option.name:
            hasUserChosenCorrectly = True
            user_input = option
            print("You have chosen {}".format(option.name))
    if not hasUserChosenCorrectly: 
        if count > 3:
            isGameOver = True
        else:
            print("Choose again")
    if hasUserChosenCorrectly:
        # Second player choice
        computer_input = random.choice(list(Hand))
        print("The second player has chosen {}".format(computer_input.name))

        # Finding winner

        if user_input == Hand.rock and computer_input == Hand.rock :
            print("Sorry, its a draw. No winner :(")
        elif user_input == Hand.rock and computer_input == Hand.paper :
            print("I am sorry, the second player has won")
        elif user_input == Hand.rock and computer_input == Hand.scissors :
            print("You have won the game!! :)")
        elif user_input == Hand.paper and computer_input == Hand.rock :
             print("You have won the game!! :)")
        elif user_input == Hand.paper and computer_input == Hand.paper :
             print("Sorry, its a draw. No winner :(")
        elif user_input == Hand.paper and computer_input == Hand.scissors :
            print("I am sorry, the second player has won")
        elif user_input == Hand.scissors and computer_input == Hand.rock :
             print("I am sorry, the second player has won")
        elif user_input == Hand.scissors and computer_input == Hand.paper :
             print("You have won the game!! :)")
        elif user_input == Hand.scissors and computer_input == Hand.scissors :
            print("Sorry, its a draw. No winner :(")
        print("Type stop to end the game otherwise press enter to play again")
        another_input = input()
        if(another_input == "stop"):
            isGameOver = True

    



    


