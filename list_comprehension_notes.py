#unique to python
#list comprehension case where you create a new list from a previous list 
#less code and easier to read
#for example if we had one list and wanted to create a new list that has all the values increased by one we woud do the following code
'''
old = [1, 2, 3]
new = []
for number in old:
    add_1 = number +1
    new.append(add_1)
'''
'''
list comprehension format:
new_list = [new_item for item in list]
'''
#now lets do the same example but with list comprehension
old = [1,2,3]
new = [number + 1 for number in old]
print(f"new list after adding 1: {new}")
#can also work with other sequences like strings for example 
myName = "Jai"
wordsList = [letter for letter in myName]
print(wordsList)
#can put the sequence directly into the comprehension statement 
new_range = [number*2 for number in range(1,5)]
print(new_range)
#there is also conditional list comprehension
#format 
#new_list = [new_item for item in list if test]
names = ["bob", "jeff", "frank", "car", "moose"]
#only print out the names/words that are less than four characters and making them uppercase
new_names_list = [word.capitalize() for word in names if len(word) < 4]
print(new_names_list)
