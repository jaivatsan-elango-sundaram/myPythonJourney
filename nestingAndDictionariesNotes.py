#dictionaries are useful because they help us group together and tag related pieces of information
#every dictionary has two parts to it: a key and a value.   

#to create a dictionary, use the following notation: {Key: Value}
#for example:
car_dictionary = {
    "accord": "a reliable sedan", 
     "sienna": "a family minivan", 
    "f-150_xl": "a utalitarian pickup truck" ,
}
#recommendations: 
#have the starting and ending curly braces in two seperate lines
#have one seperate line for each entry

# to retrieve information from the dictionary, use the key
print(car_dictionary["accord"])
# if the key is a string, make sure you are inclduing the quotation marks 

#to add an entry to the dictionary, follow the below format
car_dictionary["g_wagon"] = "a luxury SUV"
print(car_dictionary)
#you can also create a ditionary with nothing in it 
empty_dictionary = {}
#to edit a value in a dictionary, follow the below format:
car_dictionary["g_wagon"] = "a luxury suv also used to offroad "

#when you loop through a dictionary like how did i below, it just gives you the key value
for car in car_dictionary:
    print(car)

#to print the value
#example:
for car in car_dictionary:
    print(car_dictionary[car])

#wipe an existing dictionary
car_dictionary = {}

#nesting, you could even have a list or dictionary as a value for the keys 
#for example:
#if you wanted to store multiple values as a key, you would have to create a list and nest it inside a
travel_log = {
    "California": ["Santa Barbara", "Tracy"],
    "New York": ["Albany", "Buffalo", "NYC"]
}
#you could nest a list in a list 
["A", "b", ["C", "D", "E"]]
#you could also nest a dictionary in a dictionary
travel_log = {
    "California": {"cities visited": ["Santa Barbara", "Tracy"]},
    "New York": {"cities visited": ["Albany", "Buffalo", "NYC"]}
}
travel_log = [
    {
    "state": "California", 
     "cities visited": ["Santa Barbara", "Tracy"]
     },

    {
    "state": "New York", 
     "cities visited": ["Albany", "Buffalo", "NYC"]
     }
]
