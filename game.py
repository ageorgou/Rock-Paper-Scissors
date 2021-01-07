# rock paper scissors game
import numpy as np
from enum import IntEnum
import random

# creating enum for hand gestures in rock, paper, scissors
class Hand(IntEnum):
    rock=1
    paper=2
    scissors=3


class Result(IntEnum):
    win = 1
    loss = 2
    draw = 3


def decide_result(player, opponent):
    assert player in Hand and opponent in Hand

    if player == opponent:
        return Result.draw
    
    if player == Hand.rock and opponent == Hand.paper :
        return Result.loss
    elif player == Hand.rock and opponent == Hand.scissors :
        return Result.win
    elif player == Hand.paper and opponent == Hand.rock :
        return Result.win
    elif player == Hand.paper and opponent == Hand.scissors :
        return Result.loss
    elif player == Hand.scissors and opponent == Hand.rock :
        return Result.loss
    elif player == Hand.scissors and opponent == Hand.paper :
        return Result.win

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
        result = decide_result(user_input, computer_input)
        assert result in Result
        if result == Result.draw:
            message = "Sorry, its a draw. No winner :("
        elif result == Result.loss:
            message = "I am sorry, the second player has won"
        else:
            message = "You have won the game!! :)"
        print(message)

        print("Type stop to end the game otherwise press enter to play again")
        another_input = input()
        if(another_input == "stop"):
            isGameOver = True

    



    


