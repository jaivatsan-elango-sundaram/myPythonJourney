from turtle import Turtle
ALL_COORDINATES = [(0,0), (-20, 0),(-40, 0)]
class Snake():
    def __init__(self):
        self.pieces_list = []
        self.create_snake()
        self.snake_head = self.pieces_list[0]
    def create_snake(self):
        #when you create a turtle it has dimsensions of twenty pixels wide and twenty pixels tall
        #to create the snake body we choose to line up three squares (which will be the turtles). basically will be right equal to eacdh other
        for a_coordinate in ALL_COORDINATES:
            self.add_segment(a_coordinate)
        #to organize the segments, lets add them to the list
        #still utillizing above for loop       
    def add_segment(self, position):
            piece = Turtle(shape = "square")    
            #dont want markings when the snake is moving 
            piece.penup()
            piece.color("white")
            piece.goto(position)
            self.pieces_list.append(piece)

    def extend(self):
        #were gonna add the new piece to the last position 
        self.add_segment(self.pieces_list[-1].position())
    #method to reset the snake and basically start a new game when the old snake crashes
    def reset(self):
        #makes the crashed snake go off screen
        for piece in self.pieces_list:
            piece.goto(-1000, -1000)
        self.pieces_list.clear()
        self.create_snake()
        self.snake_head = self.pieces_list[0]        
    def move(self):
        #we're gonna move the third segment to the second segment position, second segment to the first segment position, and the first segment forward to move the snake
        for i in range(len(self.pieces_list) -1, 0, -1):
            #moving the part to the position of the part before it 
            #to do so, we have to get the x and y coordinate of the piece before it 
            front_x = self.pieces_list[i - 1].xcor()
            front_y = self.pieces_list[i - 1].ycor()
            #now were actually gonna move the current piece to the x and y coordinate of the one in front of it 
            self.pieces_list[i].goto(front_x, front_y)
        #We also need to move the very first segment 
        self.pieces_list[0].forward(20)
    #only need to change the direction of the head, rest of the body will follow 
    def up_arrow(self):
        self.snake_head.setheading(90)
    def right_arrow(self):
        self.snake_head.setheading(360)
    def down_arrow(self):
        self.snake_head.setheading(270)
    def left_arrow(self):
        self.snake_head.setheading(180)