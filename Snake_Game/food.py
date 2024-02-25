from turtle import Turtle
import random
class Food(Turtle):
    #the food class will show up as a small circle on the screen and will move to a different location when it is touched by the snake
    def __init__(self):
        #food will inherit from the turtle class 
        super().__init__()
        self.penup()
        #since food is a turtle object we inherit the associated methods and can use them
        self.shape("circle")
        self.color("blue")
        #use shapesize method to change the size of the turtle 
        #technically shrinking it to 0.5 of its original size 
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
    def random_place(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        