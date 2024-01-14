#idea inspired by Angela Yu on Udemy
#code all by me
#number of coins user has
coins = 5000
#travelling to the island
print("Welcome to the ChooseYourAdventure game. In this game, you can choose your path and make decisions for a possible chance at finding treasure")
print("You have 5000 coins with you and some supplies.")
print("After conducting some research, you were able to arrive at a place where the island with the treasure is about 25 miles through water.")
waterDecisions = input("The boat that will take you to the island will arrive 3 hours and will cost 1000 coins. You can either wait for the boat or starting swimming now. Type 'w' to wait for the boat or 's' to start swimming ")
if(waterDecisions == "s"):
    print("You drown. Game over")
else:
    coins -= 1000
    print(f"You decided to take the boat and paid for it. You have {coins} left.")
    #buying supplies 
    convenianceStoreDecision = input("After landing on the island, you see a conveniance store. Would you like to go inside and buy supplies? It will cost 500 coins (y/n)")
    if(convenianceStoreDecision) == "n":
        print("After a few days, you run out of supplies and die while travelling to the treasure. Game over.")
    else:
        coins = coins - 500
        #buying weapons
        weaponsDecision = input("After travelling for a few days, you stumble upon a weapons store. It will cost you 3500 coins. Would you like to go outside and purchase a weapon? (y/n)")
        if weaponsDecision == "y":
            coins -= 3500
            print(f"You have decided to purchase a few weapons. You have {coins} coins left")
        print("Hooray! After a few days, you were able to find the treasure chest. It contained 100,000 coins!")
        if weaponsDecision == "n":
            print("On your way back, you were approached by bandits. Since you did not own any weapons, they robbed you for all you treasure. Game over.")
        else:
            print("A group of bandits approach you, but you were able to scare them off with your weapon. You were able back to the shore and left in a boat. You won!")