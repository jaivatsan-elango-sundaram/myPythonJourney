from turtle import Turtle, Screen
tim = Turtle()
tim.pendown()
orientation = 15
#fumctions for moving forward, backward, turn left and right 
def key_right():
    global orientation
    orientation = orientation - 15
    tim.setheading(orientation)
def key_left():
    global orientation
    orientation = orientation + 15
    tim.setheading(orientation)
def move_forward():
    tim.forward(20)
def move_back():
    tim.backward(20)
def clear_screen():
    tim.clear()
    tim.home()

screen = Screen()
#event listeners 
screen.listen()
screen.onkey(key = "w", fun = move_forward) 
screen.onkey(key = "s", fun = move_back)
screen.onkey(key = "a", fun = key_left)
screen.onkey(key = "d", fun = key_right)
screen.onkey(key = "c", fun = clear_screen) 
screen.exitonclick()
