#following angela yu's tutorial on udemy 
#the only image format the turtle module works with is .gif 
import turtle 

import pandas
states_image = "blank_state_image.gif"
screen = turtle.Screen()
screen.title("The US State Guessing Game")
states_image = "blank_states_img.gif"
##to add in a turtle that has a shape of something that is not standard, use the addshape command 
screen.addshape(states_image) 
#now we can use that shape/image in our programs
turtle.shape(states_image)
writer = turtle.Turtle()
#require on screen text input for the user to guess a state
#there are 50 stats
correct_guesses = []
not_guessed = []
state_data = pandas.read_csv("50_states.csv")
#check if the users is a state by first converting the state column to a list and checking if the answer was any of the entries in the list
all_states = state_data.state.to_list()
while len(correct_guesses) < 50:
    #require on screen text input for the user to guess a state
    user_answer = screen.textinput(title = f"{correct_guesses}/50 correct", prompt ="Guess the name of a state in the U.S.")
   #title case makes the first letter of both words capital 
    user_answer = user_answer.title()
    if user_answer == "Exit":
        break
    elif user_answer in all_states:
        #create a turtle that will write the state name at the state's x and y 
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        #pull up the row that has the info about the correct state
        correct_state = state_data[state_data.state == user_answer]
        #YOU MUST CONVERT ANY NUMBERS EXTRACTED TO INTS 
        t.goto(int(correct_state.x), int(correct_state.y))
        t.write(user_answer)
        correct_guesses.append(user_answer)
#checks the main list to check if the list with all the sates guessed was missing stuff
for state in all_states:
    #if anything is missing, it is added to the appropriate list
    if state not in correct_guesses:
        not_guessed.append(state)
#converted to datframe and then to a csv 
missed_states = pandas.DataFrame(not_guessed)
missed_states.to_csv("/Users/esundara/Desktop/Jais_Python_Projects/myPythonJourney/State Identifying Project/not_guessed.csv")