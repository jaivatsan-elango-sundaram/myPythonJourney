#idea by angela yu on udemy
#all code by me
import random
#creating variables and lists needed for program
x = 0
letters = ["q", "w", "e", "r", "t", "y", "u", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
characters = ["!", "@", "#", "$", "%", "^", "&", "*"]
useAgain = ""
anotherOne = True
passwordList = []
password = ""
randomLetter = ""
randomNumber = ""
randomCharacter = ""
randomPosition = 0
while anotherOne == True:
#user prompts
    maxLetters = int(input("How many letters should be there?: "))
    maxNumbers = int(input("How many numbers should be there?: "))
    maxCharacters = int(input("How many special characters should be there?: "))
    length = maxLetters + maxNumbers + maxCharacters
#creating placeholder
    for i in range(0,length):
        passwordList.append("-")
#putting in random letters, numbers, and special characters in random positions
    for i in range(0, maxLetters):
        randomPosition = random.randint(0, length -1) 
        randomLetter = random.randint(0, len(letters) - 1) 
        passwordList[randomPosition] = letters[randomLetter]
        print(letters[randomLetter])
    for i in range(0, maxNumbers):
        while passwordList[randomPosition] != "-":
            randomPosition = random.randint(0, length - 1)
        randomNumber = random.randint(0,len(numbers) - 1)
        passwordList[randomPosition] = numbers[randomNumber]
    for i in range(0, maxCharacters):
        while passwordList[randomPosition] != "-":
            randomPosition = random.randint(0, length - 1)
        randomNumber = random.randint(0,len(characters) - 1)
        passwordList[randomPosition] = characters[randomNumber]
#final password
    dashCount = 0
    for i in passwordList:
        if i == "-":
            dashCount += 1
    for i in range (0,dashCount):
        passwordList.remove("-")
    for i in passwordList:
        password = password + i
    print(f"Your password: {password}")
    passwordList.clear()
    password = ""
    useAgain = input("Would you like to generate another password? (y/n)")
    if useAgain == "n":
        anotherOne = False
    