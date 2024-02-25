#you can create a function with default arguments so that you wouldnt have to enter it in every single time you call the function
#for example
def function_one(a =1, b =2, c =3):
    return b
#when calling it without any arguments, a=1,b=2, c=3
value1 = function_one()
print(value1)
#you could still call it with an argument 
value2 = function_one(b = 3)
print(value2)

#unlimited arguments for a function 
#for example, in the below function we are only restricted to adding 2 number unless we add more values to function parameter
def add(n1, n2):
    return n1 + n2 

#to overcome this limitation we can put *args in the function parameter
#you dont need the *args, you need the * and can put any word after that
#args standards for arguments 
def add_a_lot(*args):
    sum = 0
    for n in args:
        sum = sum + n
    #can also acess them through an index because it is a tuple after all
    print(args[0])
    return sum
#basically iteration through the tuple of arguments 
#data type is a tuple s
print(add_a_lot(5, 10, 10, 10, 10))
#in this case, the position matters a lot when it comes to interacting with arguments 


#kwargs: many keyworded arguments 
#for example
#you NEED two asterisks in front of the word 
def calculate(starting_number,**kwargs):
    #when you print the keyword arguments, it it shown that they are a dictionary
    print(kwargs)
    #can also loop through it 
    for (key,value) in kwargs.items():
        print(key)
        print(value)    
    #can also fetch the value at a certain key 
    print(kwargs["add"])
    starting_number += kwargs["add"]
    starting_number += kwargs["multiply"]
    

calculate(2,add = 3, multiply =5)


#can also do this with classes
class Car:
    def __init__(self, **kwargs): 
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        #it is better to use .get because if there is no key in the dictionary because it was not an argument entered, it will return None rather than giving us an error
my_car = Car(make = "Jeep", model = "Grand Cherokee")
print(my_car.model)
my_other_car = Car(make = "Kia")
print(my_other_car.model)

#you can use both args and kwargs in the same function call
#for example
def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)