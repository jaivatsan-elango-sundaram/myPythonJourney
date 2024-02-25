from turtle import Turtle, Screen
import time 
from snake import Snake 
from food import Food 
from scoreboard import Scoreboard 
#followed angela yu's python tutorial on udemy 
screen = Screen()
#sets up a screen that is 600 pixels wide and 600 pixels hgh
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game replica")
#the tracer method either delays or does not show the animation during the drawing
#we are using tracer because without it will look very weird, you can comment the tracer line to see it if u wish. basically will not update the drawing 
screen.tracer(0)
#when you create a turtle it has dimsensions of twenty pixels wide and twenty pixels tall
#to create the snake body we choose to line up three squares (which will be the turtles). basically will be right equal to eacdh other 
'''
square1 = Turtle(shape = "square")
square1.color("white")
square2 = Turtle(shape = "square")
square2.color("white")
square3 = Turtle(shape = "square")
square3.color("white")
#positioning them twenty apart bc the width of one turtle is twenty and we want them to be connected basically
square1.goto(0, 0)
square2.goto(-20, 0)
square3.goto(-40, 0)
 '''

# you could also do this with a for loop - will be much more efficient
my_snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()    
screen.onkey(key = "Up", fun = my_snake.up_arrow) 
screen.onkey(key = "Right", fun = my_snake.right_arrow)
screen.onkey(key = "Down", fun = my_snake.down_arrow)
screen.onkey(key = "Left", fun = my_snake.left_arrow)
gameRunning = True
while gameRunning == True:
    #after every single part of the snake moves, we update the screen, so it looks like the entire snake is moving 
    screen.update()
    #delays/waits for 0.1 seconds after all the pieces move
    time.sleep(0.1)
    my_snake.move()
    score = 0
    #checking if snake ate food
    if food.distance(my_snake.snake_head) < 15:
        food.random_place()
        scoreboard.increase_score()
        my_snake.extend()
    #checking if it goes off screen
    if (my_snake.snake_head.xcor() > 295 or my_snake.snake_head.xcor() < -295) or (my_snake.snake_head.ycor() > 295 or my_snake.snake_head.ycor() < -295):
        #resets the scoreboard when the game ends bc of wall crash 
        scoreboard.reset()
        my_snake.reset()
    #check if head hits body
    #check if the head hits any of the segments
    for a_piece in my_snake.pieces_list:
        if a_piece == my_snake.snake_head:
            pass
        elif my_snake.snake_head.distance(a_piece) < 10:
            #resets the scoreboard when the game ends bc of head hitting b  ody
            scoreboard.reset()
            my_snake.reset()


screen.exitonclick()