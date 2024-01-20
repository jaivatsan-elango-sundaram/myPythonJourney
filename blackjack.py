#idea and ascii art by angela yu
#all other code by jai sundaram
import random
#creating variables necessary
cardList = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "A"]
userList = []
dealerList = []
userTotal = 0
userCard = 0
dealerCard = 0
dealerTotal = 0
gameRunning = True
askAnother = ""
playAgain = True
askOption = ""
print('''
Welcome to Blackjack!
The goal of this game is to have the total value of your cards be as close as possible to 21. 
Hit if you would like to increase your overall value, and stand if you do not want to crease the value.
      ''')
#function for when the dealer of user draws a card
def addCard(total):
    randomCard = random.randint(0, len(cardList) - 1)
    card = cardList[randomCard]
    if card == "A":
        if total + 11 > 21:
            return 1
        else:
            return 11
    else:
        return card
#function to check if either the user or dealer has blackjack
def isBlackjack():
    if (dealerTotal == 21 and ((dealerList[0] == 10 and dealerList[1] == 11) or (dealerList[1] == 10 and dealerList[0] == 11))):
        print("The dealer has blackjack!")
        return True
    elif (userTotal == 21 and ((userList[0] == 10 and userList[1] == 11) or (userList[1] == 10 and userList[0] == 11))):
        print("You have blackjack!")
        return True
    else:
        return False 
#code for the overall game
while playAgain == True:
    print('''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/   
          ''')
    for i in range (0, 2):
        randomPosition = random.randint(0,len(cardList) - 1)
        if randomPosition == len(cardList) -1:
            if userTotal + 11 > 21:
                userList.append(1)
                userTotal+=1
            else:
                userList.append(11)
                userTotal += 11
        else:
            userList.append(cardList[randomPosition])
            userTotal += cardList[randomPosition]
        randomPosition = random.randint(0,len(cardList) - 1)
        if randomPosition == len(cardList) -1:
            if dealerTotal + 11 > 21:
                dealerList.append(1)
                dealerTotal+=1
            else:
                dealerList.append(11)
                dealerTotal += 11
        else:
            dealerList.append(cardList[randomPosition])
            dealerTotal += cardList[randomPosition]
    #provides final outputs
    print(f'''
Your cards: {userList}
Value: {userTotal}
''')
    print(f"The dealer's first card: {dealerList[0]}")
    while gameRunning == True:
        if isBlackjack() == True:
            gameRunning = False
        while askOption != "stand" and gameRunning == True:
            askOption = input("Would you like to hit or stand? ")
            askOption.lower()
            if askOption == "hit":
                userCard = addCard(userTotal)
                userTotal += userCard
                userList.append(userCard)
                print(f'''
Your cards: {userList}
Value: {userTotal}
''')
                if isBlackjack() == True:
                    gameRunning = False
                if userTotal > 21:
                    print(f'''
You went over 21! Bust! You lose!
Your cards: {userList}
Dealer's cards: {dealerList}     
                          ''')
                    gameRunning = False
        while dealerTotal <= 16 and gameRunning == True:
            dealerCard = addCard(dealerTotal)
            dealerTotal += dealerCard
            dealerList.append(dealerCard)
            if isBlackjack() == True:
                gameRunning = False
            if dealerTotal > 21:
                print(f'''The dealer went over 21! Bust!
Your cards: {userList}
Value: {userTotal}

Dealer's cards: {dealerList} 
Value: {dealerTotal}
                      ''')
                gameRunning = False
        if (21 - userTotal < 21 - dealerTotal) and (userTotal < 21 and dealerTotal < 21):
            print(f'''
You won!
                  
Your cards: {userList}
Value: {userTotal}

Dealer's cards: {dealerList} 
Value: {dealerTotal}
              ''')
            gameRunning = False
        elif 21 - userTotal > 21 - dealerTotal and (userTotal < 21 and dealerTotal < 21):
            print(f'''
You lost!
                  
Your cards: {userList}
Value: {userTotal}

Dealer's cards: {dealerList} 
Value: {dealerTotal}
              ''')
            gameRunning = False
        elif 21 - userTotal == 21 - dealerTotal and (userTotal < 21 and dealerTotal < 21):
            print(f'''
You drawed!
                  
Your cards: {userList}
Value: {userTotal}

Dealer's cards: {dealerList} 
Value: {dealerTotal}
              ''')
            gameRunning = False
    #resetting the values
    cardList = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "A"]
    userList = []
    dealerList = []
    userTotal = 0
    userCard = 0
    dealerCard = 0
    dealerTotal = 0
    gameRunning = True
    askOption = ""
    #prompt that determines if the user would like to play the game again
    askAgain = input("Would you like to play another game of Blackjack? (y/n)")
    if askAgain == "n":
        playAgain = False 




        





