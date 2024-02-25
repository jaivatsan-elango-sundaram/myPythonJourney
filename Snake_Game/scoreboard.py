from turtle import Turtle 
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.high_score = 0 
        #we dont want to see the turtle itself, just the scoreboard
        self.hideturtle()
        #goes to center top
        self.goto(0, 270)
        self.score = 0
        self.write_score()
    def write_score(self):
        self.clear()
        #one of the things who can do with a turtle is to get it to write a piece of text using the write() method 
        self.write(f"Score: {self.score} High score: {self.high_score}", align = 'center', font= ('Arial', 24, 'normal'))


    def increase_score(self):
        self.score += 1
        #clears the previous text that was written so it does not overlap 
        self.write_score()
    def reset(self):
        #wanna update the high score too 
        if self.score > self.high_score:
            self.high_score = self.score 
        self.score = 0 
        self.write_score()

