#working with weather_data.csv
#the file is organized into columns of values 
#use the following package to work with csv files
'''
import csv 
with open("weather_data.csv") as weather_files:
    #the reader method can read the data and output it 
    data = csv.reader(weather_files)
    #this object can be looped through
    #for example, we could get each row of the file
    temp = []
    for row in data:
        print(row)
        #now lets make a list that only has all the temperatures
        if row[1] != "temp":
            temp.append(int(row[1]))         
print(temp)

#this is very tedious, the pandas library can help '''
import pandas 
#use the read_csv method to read the data
data= pandas.read_csv("weather_data.csv")
#put the name of the column inside the square brackets 
print(data["temp"])
#a dataframe would be be the entire table or sheet
#a series is equivalent is a list and is kind of like a single column in ur table
#for example the temp column would be a series 

#can convert the dataframe to a variety of other formats 
# so can also convert it to a dictionary
data_dict = data.to_dict()
print(data_dict)
#can also convert a series to a variety of formats, like a list
temp_list = data["temp"].tolist()
print(temp_list)
'''
sum = 0
for temp in temp_list:
    sum = sum + temp
average = sum/len(temp_list)
print(average) '''
#can also use a pandas method to get the same goal 
#can call the mean method 
#can also get other mathematical values by using other methods
print(data["temp"].max())
print(data["temp"].min())
#pandas assumes that the first row is the name of the columns
#instead of doing all that  you can just call the attribute 
print(data.temp)

#getting rows of the dataframe 
print(data[data.day == "Monday"])

#above prints the row where the day is equal to Monday 
#printing the row where the temp was the max 
max_temp = data.temp.max()
print(data[data.temp == max_temp])
#can also get an attribute of that row 
hottest_day = data[data.temp == max_temp]
#getting condition of the row in which the temp was the highest
print(hottest_day.condition)
#convert temp of monday to faranheit 
#dont even have to convert the type 
monday = data[data.day == "Monday"]
monday_temp = (monday.temp * (9/5)) + 32
print(monday_temp)

#create a dataframe from scratch 
#lets say we have a dictionary
data_dict = {
    "students": ["jeff", "bob", "frank"],
    "scores": [90, 84, 88]
}
#to convert it to a dataframe
score_data = pandas.DataFrame(data_dict)
#can even convert this to a csv file 
#the parameter would be the path
score_data.to_csv("/Users/esundara/Downloads/test_score_data.csv")
#created a csv called test_score_data in the Downloads folder 