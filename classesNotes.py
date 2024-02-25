#syntax
'''
Class [class name]:

'''
#example
#each word in the name of the class should be capitalized (PascalCase, NOT camelcase )
#snake case is all lowercase but the words are seperated by underscores
#in python, use pascal case for classes and snake case for everything else
class User:
    pass
    #pass keyword makes the class empty. this can also be used for functions 
#to create an attribute, just tap into it
user_1 = User()

user_1.id = "001"
user_1.username = "bob"
print(user_1.username)

#instead of having to follow this process for each object, you could just use a constructor 

#__init__ is used to initialize attributes 
class Car():
    #name of the parameter is usually equal to the name of attribute, but not compulsary
    def __init__(self, seats, make):
        #this is called everytime a new object is called
        #self needs to stay, that is the object itself
        #new attribute called seats
        #kinda similair to functions
        self.seats = seats
        self.make = make 
        #can also set default values
        self.num_sales = 0
        #another default value
        self.tires ="summer"
    #you can also add methods to a class
    #methods also always need to have self as the first parameter 
    def weight_reduction(self):
        self.seats = self.seats - 3 
    def changeTires(self, tires):
        self.tires = tires
my_car = Car(5, "Nissan")
#can still extract attribute values
print(my_car.make)
my_car.weight_reduction()
my_car.changeTires("winter")
print(my_car.seats)
print(my_car.tires)