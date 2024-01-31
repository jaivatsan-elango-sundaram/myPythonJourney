#to use random number, first import the random module: import random
import random
#to get a  random numbers use the randint() function. randint(a,b) (they are inclusive)
#example:
print(random.randint(2,5))

#to get a random random float between 0 and 1, use random.random(). IMPORTANT: 1 is not included, but 0 is.
print(random.random())
#if you want the ending value to be something other than 1, multiple the function by that nunber
#for example:
#to get a random float between 0 and 5
print(5*random.random()) 

#to create a list, x = []
#example:
x = ["one", "two"]
#can be mixed, holding many different data types
#for example:
y = [3, "example1", False]

#in a list, if your index is negative, it starts counting from the end of the list 
#example:
print(y[-1])

#to change a value at a certain position, just setting it equal to the values you would like to change it to
y[0] = 7
print(y[0])

#use .append() to add a single item to the end of the list
#for example:
y.append(9)

#to add multiple new values to to the end of the list, use the .extend() function
#for example
y.extend(["car", True])
print(y)

#to add values at a certain position, use the .insert(i, x)
#it will insert x at position i and move the item at i 
y.insert(0, "minivan")
print(y)

#to remove items at a certain value, use pop(i); it will also return the value. If the i is not speicified, it will remove the last item in the list and
a = y.pop(0)
print(y)
print(a) 

#use the .remove(x) function to remove the first item whose value is equal to x
y.remove("example1")
print(y)

#nested lsts: when a list contains another list
best_selling_cars = []
best_selling_sedans = ["Camry", "Civic", "Jetta"]
best_selling_trucks = ["F-150", "Sliverado", "RAM 1500"]
best_selling_cars = [best_selling_sedans, best_selling_trucks]
print(best_selling_cars)

#.split() splits the inputs and puts each indivdual item into a list 