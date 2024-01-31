from words import word_list
import random 
currentLife = 0
computerWord = ""
p1List = []
p2Word = ""
p2List = []
previousState = ""
gameOver = False
p1Word = input("Enter a random word: ")
p1Word = p1Word.lower()
for i in range (0, len(p1Word)):
    p1List.append("x")
    p2List.append("_")
    previousState += "_"
for i in range(0, len(p1Word)):
    p1List[i] = p1Word[i]
print(p1List)
while gameOver == False:
    userLetter = input("Enter a letter you think may be in the word:")
    userLeter = userLetter.lower()
    for i in range(0, len(p1List)):
        if userLetter == p1List[i]:
            p2List[i] = userLetter
    p2Word = ''.join(p2List)
    if p2Word == previousState:
        currentLife += 1
        print(f"current life: {currentLife}")
    print(p2Word)
    if p2Word == p1Word:
        gameOver = True
    elif currentLife >= 6:
        gameOver = True
    previousState = p2Word


