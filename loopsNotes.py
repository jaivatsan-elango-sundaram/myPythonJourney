#for loop format (the "in the part" is a list (so exclusive to lists only))
'''
for item in rang_of_items:
    do something for each item
'''
cars = {"camry", "accord", "passat"}
for car in cars:
    print(car)

#another loop format( can also be used when we are not working with a list):
'''
for i in range(a,b):
    do stuff for each thing

'''
#b is not included  
#you basically looop through a range of values
#you can choose by what value it iterates by
for i in range(0, 18, 2):
    print(i)