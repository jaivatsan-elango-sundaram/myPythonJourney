#following angela yu's tutorial on udemy 
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    #cancels the timer 
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text = "25:00")
    marks = ""
    timer_label.config(text = "Timer")
    reps = 1
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    if reps % 8 == 0:
        timer_label.config(text = "Break", fg = PINK)
        count_down(LONG_BREAK_MIN * 60)
        reps = reps + 1
    elif reps % 2 == 0:
        timer_label.config(text = "Break", fg = RED)
        count_down(SHORT_BREAK_MIN * 60)
        reps = reps + 1
    else: 
        timer_label.config(text = "Work", fg = GREEN)
        count_down(WORK_MIN * 60)
        reps = reps + 1
        
    #in terms of seconds
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
#to keep it counting down, instead of using a for loop(which messes with the program), we decide to call the function from the after method inside the loop
#you can create a method creating certain things before those things are even created, but you can only call those methods after those things are created 
def count_down(count):
    #gets rid of all the decimals after the end, just to get the minutes
    timer_minutes = math.floor(count /60)
    #now we have to find the seconds to get the remainder 
    timer_seconds = count % 60
    #need a solution so that when numbers that start with a 0 (00, 01, 02, 03...) we get that and not just one digit because it looks weird 
    if timer_seconds < 10:
        timer_seconds = f"0{timer_seconds}"
    #updating the display
    #similair to the config() method for the canvas
    #first arg is what ur configuring, second is what aspect/how
    #using f string
    canvas.itemconfig(timer_text, text = f"{timer_minutes}: {timer_seconds}")
    #the after method takes the amount of time it should wait, then after the period of time it calls a function u tell it to call
    #the time is in milliseconds
    #we have this while looop so we dont end up having negative values 
    if count > 0:
    #the arguments are the time in milliseconds, the commands that should be called, and then you have *args, so u have unlimited arguments that go inside the function being called
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    #when it reaches, the timer goes to the next section rather than just stopping at 0
    else:
        start_timer()
        #code to make a checkmark pop up everytime we end a work session and exactly when the timer hits 0
        mark = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            mark +="✅"
        check_mark.config(text = mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("The Pomodoro App")
#a canvas widget helps us layout things one on top of the other 
#we will use this to place text on top of an image 

canvas = Canvas(width=200, height=224)
#we are making the width 200 and the height 224 because that is roughly the size of the underlying image 
#adding imag eusing the create_image method 
#to actually create the image we also need something called a PhotoImage
#a PhotoImage is a Tkinter class, which is a way to read through a file and get hold of a particular at a particular file location
tomato_image=PhotoImage(file = "tomato.png")
#arguments are a xposition, y position, and the the PhotoImage for that picture
canvas.create_image(100, 112, image = tomato_image)
#now lets create the text that we will be laying on top of the image 
#arguments will be x position, y position, and the text 
timer_text = canvas.create_text(100, 130, text = "25:00", fill = "white", font = (FONT_NAME, 35, "bold"))
#now we change the background color
#we are getting the color from a website called colorhunt.co, which contains a lot of sample color pallettes professionals use 
#we will be changing both the background and palette color 
canvas.config(bg = YELLOW)
window.config(bg = YELLOW)
#also changing highlight thickness because without it it looks weird, u can comment the line to see what happens
canvas.config(highlightthickness = 0)
#finaly need to pack the image or lay it out onto the screen
canvas.grid(column = 1, row = 1)
start_button = Button(text = "Start", command = start_timer)
start_button.grid(column = 0, row = 2)
reset_button = Button(text = "Reset", command = reset_timer)
reset_button.grid(column = 2, row = 2)
#using the fg argument changes its color/the font color 
timer_label = Label(text = "Timer", fg = GREEN, bg = YELLOW, font = (FONT_NAME, 45, "bold"))
timer_label.grid(column = 1, row = 0)
check_mark = Label()
check_mark.grid(column = 1, row = 3)
#lets make the screen a bit larger so that the image does not take up the entire screen 
window.config(padx = 100, pady = 50)
window.mainloop()
