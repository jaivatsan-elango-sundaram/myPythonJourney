#inspired from Angela Yu on Udemy, added my own twists
#all code by me

#importing random for random choices, and getpass to hide userinput for multiplayer
import random
from getpass import getpass
#function for the singplayer gamemode 
def single_player():
    wannaPlay = ""
    computerChoice = 0
    userChoice = ""
    userWon = False
    userTied = False
    userLost = False
    playAgain = True
    timesWon = 0
    timesLost = 0
    timesTied = 0
    plays = ["Rock", "Paper", "Scissors"]
    while(playAgain == True):
        computerChoice = random.randint(0,2)
        userChoice = input("What would you like to play: Rock, Paper, Scissors? ")
        if userChoice == "Scissors":
            if computerChoice == 1:
                userWon = True
            elif computerChoice == 2:
                userTied = True 
            elif computerChoice == 0:
                userLost = True
        if userChoice == "Paper":
            if computerChoice == 0:
                userWon = True
            elif computerChoice == 1:
                userTied = True 
            elif computerChoice == 2:
                userLost = True
        elif userChoice == "Rock":
            if computerChoice == 0:
                userTied = True
            elif computerChoice == 1:
                userLost = True
            elif computerChoice == 2:
                userWon = True
        if userWon == True:
            timesWon += 1
            print(f"You won! You chose {userChoice} and the computer chose {plays[computerChoice]}. {userChoice} beats {plays[computerChoice]}.")
        elif userTied == True:
            timesTied += 1
            print(f"You tied! You chose {userChoice} and the computer chose {plays[computerChoice]}. {userChoice} ties with {plays[computerChoice]}.")
        elif userLost == True:
            timesLost += 1
            print(f"You lost! You chose {userChoice} and the computer chose {plays[computerChoice]}. {userChoice} loses to {plays[computerChoice]}.")
        wannaPlay = input("Woul you like to play again? (y/n) ")
        if wannaPlay == "n":
            print("Thanks for playing!")
            playAgain = False
        userWon = False
        userTied = False
        userLost = False

#code for the multiplayer gamemode 
def multiplayer():
    p1W = False
    p2W = False
    Tied = False
    wannaPlay = ""
    playAgain = True
    playerOneName = input("What is the name of the first player? ")
    playerTwoName = input("WHat is the name of the second player? ")
    while playAgain == True:
        p1Choice = getpass(f"{playerOneName}, please choose your choice (Rock, Paper, Scissors): ")
        p2Choice = getpass(f"{playerTwoName}, please choose your choice (Rock, Paper, Scissors): ")
        if p1Choice == "Scissors":
            if p2Choice == "Paper":
                p1W = True
            elif p2Choice == "Scissors":
                Tied = True
            elif p2Choice == "Rock":
                p2W = True
        if p1Choice == "Paper":
            if p2Choice == "Rock":
                p1W = True
            elif p2Choice == "Paper":
                Tied = True
            elif p2Choice == "Scissors":
                p2W = True
        if p1Choice == "Rock":
            if p2Choice == "Scissors":
                p1W = True
            elif p2Choice == "Rock":
                Tied = True
            elif p2Choice == "Paper":
                p2W = True
        if p1W == True:
            print(f"{playerOneName} won! {playerOneName} chose {p1Choice} and {playerTwoName} chose {p2Choice}. {p1Choice} beats {p2Choice}.")
        elif p2W == True:
            print(f"{playerTwoName} won! {playerOneName} chose {p1Choice} and {playerTwoName} chose {p2Choice}. {p2Choice} beats {p1Choice}.")
        elif Tied == True:
            print(f"{playerOneName} and {playerTwoName} tied! {playerOneName} chose {p1Choice} and {playerTwoName} chose {p2Choice}. {p1Choice} ties with {p2Choice}.")
        wannaPlay = input("Would you like to play again? (y/n) ")
        if wannaPlay == "n":
            print("Thanks for playing!")
            playAgain = False
        p1W = False
        p2W = False
        Tied = False
#asks user what gamemode they want to play
whichGame = input("Which game would you prefer, multiplayer or singleplayer (against the computer)? (m/s): ")
if whichGame == "m":
    multiplayer()
elif whichGame == "s":
    single_player()