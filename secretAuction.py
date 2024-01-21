#idea by angela yu on udemy
#all code by jai sundaram
from getpass import getpass
#created variables necessary
anotherBidder = True
askAnother = ""
bidList = {}
#function to add a bid to the dictionary
def bid(name, bid):
    bidList[name] = bid
while anotherBidder == True:
#preliminary information for adding the bid
    name = input("What is your name?")
    bidValue = int(getpass("How much would you like to bid? (Enter the numerical value only) "))
    bid(name, bidValue)
    askAnother = input("Is there another bidder? (y/n) ")
    if askAnother == "n":
        anotherBidder = False
#code for checking the maximum bid
maxBidValue = bidValue
print(maxBidValue)
maxBidder = name
print(bidList)
for bidder in bidList:
    if bidList[bidder] > maxBidValue:
        print(bidder)
        maxBidder = bidder
        maxBidValue = bidList[bidder]
#outputs final information 
print(f"The winner is {maxBidder} with a bid of ${maxBidValue}!")
    