#function with input
def greet_with_name(name):
    print(f"How do you do, {name}?")
greet_with_name("jai")
#in this case, the variable 'name' would be the parameter and the string name, "jai" would be the argument 

#functions with more than 1 input
def greet_with_name_and_location(name, location):
    print(f"Hello {name}! You are living in {location}.")
greet_with_name_and_location("bob", "london")
#this would be an example of a positional argument 

#in keyword arguments, you can just set it equal to the variable and not rely on positon. Position doesnt matter
greet_with_name_and_location(name = "bob", location = "london")
greet_with_name_and_location(location = "london", name = "bob")
#they provide the same output 