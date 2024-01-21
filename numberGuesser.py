#idea by angela yu on udemy
#all code by jai sundaram
import random
#creating variables needed
numGuesses = 0
askLevel = input("Would you like easy (10 tries) or hard mode (5 tries)? (easy/hard)")
COMPNUMBER = random.randint(1, 100)
print(COMPNUMBER)
#function for easy mode 
def easy():
    guesses = 10
    guessNum = 0
    gameRunning = True
    while guesses >= 1 and gameRunning ==True:
        guessNumber = int(input("Guess a number"))
        if (guessNumber > COMPNUMBER):
            print("Too high")
            guesses = guesses - 1
            guessNum += 1
        elif guessNumber < COMPNUMBER:
            print("Too low")
            guessNum += 1
            guesses = guesses - 1
        elif guessNumber == COMPNUMBER:
            print("Correct")
            guessNum += 1
            gameRunning = False
    return guessNum
#function for hard mode 
def hard():
    guesses = 5
    guessNum = 0
    gameRunning = True
    while guesses >= 1 and gameRunning ==True:
        guessNumber = int(input("Guess a number"))
        if (guessNumber > COMPNUMBER):
            print("Too high")
            guesses = guesses - 1
            guessNum += 1
        elif guessNumber < COMPNUMBER:
            print("Too low")
            guessNum += 1
            guesses = guesses - 1
        elif guessNumber == COMPNUMBER:
            print("Correct")
            guessNum += 1
            gameRunning = False
    return guessNum



#chooses the level depending on user response
if askLevel == "easy":
    numGuesses = easy()
elif askLevel == "hard":
    numGuesses = hard()
#provides final outputs 
if askLevel == "easy":
    if numGuesses >= 10:
            print(f"You lost! You never guessed the number in 10 tries! The answer was {COMPNUMBER}")
    else:
        print(f"You won! You guessed the number correctly in {numGuesses} tries.")
elif askLevel == "hard":
    if numGuesses >= 5:
            print(f"You lost! You never guessed the number in 5 tries! The answer was {COMPNUMBER}")
    else:
        print(f"You won! You guessed the number correctly in {numGuesses} tries.")