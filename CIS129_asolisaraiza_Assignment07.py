"""A dice game, not fan"""
#Angel Solis
#CIS129 Assignment 7
#03/21/2024


#Dice game form Assignment 7 which I decided to make the winner
#the one with the greater value

import random


def main():
    print()

    #Initialize variables
    endProgram = "no"
    playerOne = "NO NAME"
    playerTwo = "NO NAME"

    playerOne, playerTwo = inputNames(playerOne,playerTwo)

    #while loop to run program again
    while endProgram == "no":
        winneName = "NO NAME"
        p1number = 0
        p2number = 0

        winnerName = rollDice(p1number, p2number, playerOne,playerTwo)

        displayIinfo(winnerName)
        endProgram = input("Do you want to end the game? (yes/no) ")

def inputNames(playerOne,playerTwo):
    playerOne = input("Insert player one name: ")
    playerTwo = input("Insert player two name: ")
    return playerOne,playerTwo

def rollDice(p1number, p2number, playerOne,playerTwo):
    p1number = random.randint(1,6)
    p2number = random.randint(1,6)
    if p1number == p2number:
        winnerName = "TIE"
    if p1number < p2number:
        winnerName = playerTwo
    if p1number > p2number:
        winnerName = playerOne
    return winnerName

def displayIinfo(winnerName):
    if winnerName == "TIE":
        print("it's a tie!")
    else:
        print(winnerName, "wins the game!")

main()
