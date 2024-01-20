#creating the variables needed 
first = 0
number = 0
prevResult = 0
result = 0
operation = ""
askAnother = ""
firstOperation = True
anotherOperation = False
usingCalc = False
#functions for the oeprations
def add(result, number):
    result = result + number
    return result 
def subtract(result, number):
    result = result - number
    return result 
def multiply(result, number):
    result = result * number
    return result
def divide(result, number):
    result = result / number
    return result 
#function for the first function, when the calculator is first started or the user says they want to do a new operation
def firstOperation(first,operation, number):
    if operation == "+":
        result = add(first, number)
    elif operation == "-":
        result = subtract(first, number)
    elif operation == "x":
        result = multiply(first, number)
    elif operation == "/":
        result = divide(first, number)
    print(f"{first} {operation} {number} = {result} ")
    return result
#function for another function, when the user continues the current
def anotherOperation(prevResult, operation, number):
    if operation == "+":
        result = add(prevResult, number)
    elif operation == "-":
        result = subtract(prevResult, number)
    elif operation == "x":
        result = multiply(prevResult, number)
    elif operation == "/":
        result = divide(prevResult, number)
    print(f"{prevResult} {operation} {number} = {result} ")
    return result
#when the calculator is first started
first =float(input("What is the first number?"))
operation = input("""
+
-
x
/
Choose an operation: """)
number =float(input("What other number is involved in the operation?: "))
prevResult = firstOperation(first, operation, number)
usingCalc = True
#asks the user if they want to keep using the calculator 
keepUsing = input("Would you like to continue using the calculator? (y/n)")
if keepUsing == "n":
    print("Thank you for using this calculator!")
    usingCalc = False
#asks if they want to continue the operation or do a new operation 
while usingCalc == True:
    askAnother = input("Would you like to continue the current operation or start a new operation? (continue/new): ")


    if askAnother == "continue":
        operation = input("""
+
-
x
/
Choose an operation: """)
        number =float(input("What other number is involved in the operation?: "))    
        prevResult = anotherOperation(prevResult, operation, number)
    elif askAnother == "new":
        first =float(input("What is the first number?"))
        operation = input("""
+
-
x
/
Choose an operation: """)
        number =float(input("What other number is involved in the operation?: "))    
        prevResult = firstOperation(first, operation, number)