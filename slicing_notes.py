#slicing gets you part of the list
#for example
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
#slice from certain indexes to another index 
#ending value is not included
print(letters[2:5])
#you could just slice till the end of the list by not having an ending value
print(letters[2:])
#you could also get everything up to a certain position
print(letters[:5])
#you could also modify the increment
print(letters[2:5:2])
#above gets us ever other item 
#you could also just get the increment
print(letters[::2])

#a negative increment will reverse the list
print(letters[::-1])

#could do the same for tuples
animals = ('dog', 'cat', 'bird', 'hamster')
print(animals[0:3])