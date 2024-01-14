#idea inspired from Angela Yu
#all code by me 
#creating all variables needed
mealPrice = 0
tax = 0
fee = 0
tip = 0
totalBill = 0
#starting prompts
print("Welcome to the Dining Cost Calculator!")
print("This program will provide a rough estimator of your dining cost")
#first requesting the meal price and setting it to totalBill
mealPrice = input("How much did your meal cost, before any service fees, tips, or sales taxes? Please type it in as a number: ")
mealPrice = int(mealPrice)
while(mealPrice < 0):
    print("Please type in a  positive numberical value")
    mealPrice = input("Type in the meal price again: ")
mealPrice = round(mealPrice)
totalBill = mealPrice
#calculating the total bill with the service fee 
fee = input("Please enter the service fee, only the numerical value: ")
fee = int(fee)
while(fee < 0 ):
    print("Please ensure that the fee is more than 0")
    fee = input("Type in the service fee again: ")
if fee != 0:
    totalBill += fee
#calculating the total bill with the tax percentage
tax = input("Please enter the tax percentage, only the numerical value: ")
tax = int(tax)
while(tax < 0 or tax > 100):
    print("Please ensure that the sales tax is between 0 and 100")
    tip = input("Type in the sales tax perentage again: ")
if tax != 0:
    tax = round(tax)
    tax = 1 + (tax/100)
    totalBill = totalBill * tax
tip = input("Please enter the tip percentage, only the numerical value: ")
#calculating the total bill with the tip 
tip = int(tip)
while(tip < 0 or tip > 100):
    print("Please ensure that the tip percentage is between 0 and 100")
    tip = input("Type in the tip perentage again: ")
if tip != 0:
    tip = round(tip)
    tip = 1 + (tip/100)
    totalBill = totalBill * tip
totalBill = round(totalBill)
#printing the prompt and the final value 
print(f"The total cost for your meal is approximately ${totalBill}. Thank you for using this program!")





