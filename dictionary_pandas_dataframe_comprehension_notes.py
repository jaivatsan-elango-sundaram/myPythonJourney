import random
#new_dict = {new_key:new_value for item in list}
#can also create a dictionary based off of existing values in dictionary 
#new_dict = {new_key:new_value for (key,value) in dict.items()}
#now were looping through each of the keys and the values in the dictionary 
#conditional
#new_dict = {new_key:new_value for (key,value) in dict.items() if test}
#example of looping through a list 
names = ["bob", "jeff", "frank", "car", "moose"]
student_scores = {name:random.randint(0,100) for name in names
    
    }
print(student_scores)
#dictionary looping
students_passed = {name:score for (name, score) in student_scores.items() if score > 60}
print(students_passed)

#pandas dataframe iteration 
student_score = {
    "names": ["Bob", "Joe", "Frank"],
    "scores": [90, 80, 75]
}
#loop through a dictionary
for (key, value) in student_score.items():
    print(value)
#loop through a dataframe just like how you would through a dictioanaty
#dataframe similair to python dictionary
import pandas
student_dataframe = pandas.DataFrame(student_score)
print(student_dataframe)
#looping through dataframe
for (key_value) in student_dataframe.items():
    print(value)

#pandas has inbuilt loop
#loops through each of the rows 
for (index, row) in student_dataframe.iterrows():
    print(row)
#the above prints out the row
for (index, row) in student_dataframe.iterrows():
    print(index)
#the above prints out the index 
#can print certain aspects of the row
#for example, we can just print the names of the students 
for (index, row) in student_dataframe.iterrows():
    print(row.names)