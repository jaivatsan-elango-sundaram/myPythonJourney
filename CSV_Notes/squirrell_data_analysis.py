#column name - Fur Color 
import pandas
squirell_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = squirell_data["Primary Fur Color"]
#do not have to use a for loop - prints all possible instances 
#you can just use the len method because it gets treated like a list 
gray_count = len(squirell_data[squirell_data["Primary Fur Color"] == "Gray"])
black_count = len(squirell_data[squirell_data["Primary Fur Color"] == "Black"])
cinnamon_count = len(squirell_data[squirell_data["Primary Fur Color"] == "Cinnamon"])
count_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_count, black_count, cinnamon_count]
}
print(count_dict)
#must conver to the dataframe first
count_frame = pandas.DataFrame(count_dict)
count_frame.to_csv("/Users/esundara/Desktop/Jais_Python_Projects/myPythonJourney/Day 25 - Working with CSV files/squirell_count_data.csv")
