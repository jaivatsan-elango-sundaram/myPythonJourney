#idea by angela yu on udemy. first package imported on all ascii art by angela yu. all other code by jai sundaram.
#imported packages needed
from words import word_list
import random
from getpass import getpass
#function for multiplayer
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
      ''')
def multiplayer():
    playAgain = True
    askAgain = ""
    currentLife = 0
    noSpaces = ""
    p1Name = input("What is player one's name?: ")
    p2Name = input("What is player two's name?: ")
    while playAgain == True:
        p1Word = ""
        p1List = []
        p2Word = ""
        p2List = []
        previousState = ""
        gameOver = False
        p1Word = getpass("Enter a random word: ")
        p1Word = p1Word.lower()
        noSpaces = p1Word
        for i in range (0, len(p1Word)):
            p1List.append("x")
            p2List.append("_ ")
            previousState += "_ "
        for i in range(0, len(p1Word)):
            p1List[i] = p1Word[i] + " "
        print("".join(p2List))
        print('''
  +---+
  |   |
      |
      |
      |
      |
=========
              ''')
        while gameOver == False:
            userLetter = input("Enter a letter you think may be in the word:")
            userLeter = userLetter.lower()
            for i in range(0, len(p1List)):
                if userLetter + " " == p1List[i]:
                    p2List[i] = userLetter + " "
            p2Word = "".join(p2List)
            p1Word = "".join(p1List) 
            if p2Word == previousState:
                currentLife += 1
            print(p2Word)
            if currentLife == 1:
                print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========
          ''')
            elif currentLife == 2:
                print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
              ''')
            elif currentLife == 3:
                print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
              ''')
            elif currentLife == 4:
                print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
              ''')
            elif currentLife == 5:
                print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
              ''')
            elif currentLife == 6:
                print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
              ''')
            if p2Word == p1Word:
                gameOver = True
                print(f"{p1Name} won! The word was {noSpaces}.")
                currentLife = 0
            elif currentLife >= 6:
                gameOver = True
                print(f"{p2Name} lost! The word was {noSpaces}. ")
                currentLife = 0
            previousState = p2Word
        askAgain = input("Wanna play again (y/n)?: ")
        if askAgain == "n":
            playAgain = False
            print("Thanks for playing!")
#function for singleplayer
def singleplayer():
    playAgain = True
    askAgain = ""
    currentLife = 0
    noSpaces = ""
    while playAgain == True:
        computerWord = ""
        computerList = []
        userWord = ""
        userList = []
        previousState = ""
        gameOver = False
        randomPosition = random.randint(0, len(word_list))
        computerWord = word_list[randomPosition]
        noSpaces = computerWord
        for i in range (0, len(computerWord)):
            computerList.append("x")
            userList.append("_ ")
            previousState += "_ "
        for i in range(0, len(computerWord)):
            computerList[i] = computerWord[i] + " "
        print("".join(userList))
        print('''
  +---+
  |   |
      |
      |
      |
      |
=========
              ''')
        while gameOver == False:
            userLetter = input("Enter a letter you think may be in the word: ")
            userLeter = userLetter.lower()
            for i in range(0, len(computerList)):
                if userLetter + " " == computerList[i]:
                    userList[i] = userLetter + " "
            userWord = "".join(userList)
            computerWord = "".join(computerList) 
            if userWord == previousState:
                currentLife += 1
            print(userWord)
            if currentLife == 1:
                print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========
          ''')
            elif currentLife == 2:
                print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
              ''')
            elif currentLife == 3:
                print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
              ''')
            elif currentLife == 4:
                print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
              ''')
            elif currentLife == 5:
                print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
              ''')
            elif currentLife == 6:
                print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
              ''')
            if userWord == computerWord:
                gameOver = True
                print(f"You won! The word was {noSpaces}.")
                currentLife = 0
            elif currentLife >= 6:
                gameOver = True
                print(f"You lost..The word was {noSpaces}. ")
                currentLife = 0
            previousState = userWord
        askAgain = input("Wanna play again (y/n)?: ")
        if askAgain == "n":
            playAgain = False
            print("Thanks for playing!")
gamemode = input("Would rather play singlplayer (against the computer) or multiplayer? (s/m): ")
gamemode = gamemode.lower()
if gamemode == "s":
    singleplayer()
else:
    multiplayer()

