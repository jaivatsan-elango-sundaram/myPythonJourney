#consider the following situation
enemies = 1 

def decrease_enemies():
    enemies  = enemies - 2
decrease_enemies()
print(enemies)
#enemies stays as 1

#the variable enemies inside the function is only exclusive to that function and is not the same as the variable outside of it
#this is called local scope 

#global scope 
#for example:
playerHealth = 0
def drink_potion():
    potion_health = 2
    print(playerHealth)

drink_potion()
#playerHealth is global and therefore can also be called in the variable. basically because it was created outside any function it can be called anywhere
#potion_strength would be a local variable because it is created inside a function

#this also applies to functions
#when you create something, pls be aware of where you created it   

#there is no block scope in python
#for example:
if 3>2:
    a = 9
#in this the scope is the overall program, even though the variable was created inside an if statement
    
print(a)
#the above is perfectly valid code

#this also applies to for loops and while loops

#modifying a global scope 
enemynumber = 1
def increase_enemies():
    global enemynumber
    enemynumber += 2
increase_enemies()
print(enemies)

#try to avoid modiyfying global scope, makes it more confusing 
#but, there may be times you need to use it

#global scope can be used when you are creating global constants
#global constants are variables which you define but never plan on changing
# for example:
pi = 3.14 
#to make it a global constant, make it all uppercase
PI = 3.14
def calc():
    answer = PI