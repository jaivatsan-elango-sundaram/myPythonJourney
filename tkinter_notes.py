#use tkinter to create a gui
#tkinter is preinstalled with python, just import it 
#import tkinter 
from tkinter import *
#imports every single class from tkinter
#create a window
window =Tk()
#change the title
window.title("My first GUI program")
#to addd padding for a widget, use the config method
window.config(padx = 20, pady = 20)
#while the window automatically scales when you have a lot if items inside it, it is good to specify a minimum size it will have when there is not a lot inside it 
window.minsize(width = 500, height = 300)

#create a label by creating a Label object 
#make sure u use keyword arguments
my_label = Label(text = "I am a label", font = ("Arial", 24, "italic"))
#you can also just leave out the last item in the font tuple so it is neither bold or italic 
#dont even need the font argument either 

#in tkinter, we also have to specify how something will be laid out on the screen before it actually shows up 
#my_label.pack()
#.pack() lays it onto the screen and automatically centers it 
#basically packs all the widgets together in a vaguely logical format 
#we can also specify how it should be aligned 
my_label.pack()
#can do left, bottom, right, top

#can also specify if you want to expand it to take up the entire creen
#my_label.pack(expand = True)
#uncomment to see what happens 

#tkinter uses keyword arguments, thats why we cant see all of them in the function popup; it just says kwargs 
#furthermore, we have the option if we want to put in those arguments when calling the method 
'''
Handy Reference
Setting Options
Options control things like the color and border width of a widget. Options can be set in three ways:

At object creation time, using keyword arguments
fred = Button(self, fg="red", bg="blue")

After object creation, treating the option name like a dictionary index
fred["fg"] = "red"
fred["bg"] = "blue"

Use the config() method to update multiple attributes after the  object creation
fred.config(fg="red", bg="blue")

'''
#for example:
my_label["text"] = "New text"
#other way
my_label.config(text = "Other new text instead")

#can also create buttons 
#setting the label to the textbox input when the button is clicked
def button_click():
    my_label.config(text = input1.get())
button1 = Button(text="Click me", command = button_click)
#command keyword makes a function get called when the button is clicked. do not include paranthesis
#lay out the button on the screen
#can use the .place method to exactly place the widget in an exact (x,y) coordinate
#button1.place(x = 0, y = 0)
#places it in the top left corner 
#need to use pack, place, or grid for the widget to actually show up  
#text input 
input1 = Entry()
#can insert some text for the entry to start offf with 
input1.insert(END, string="Some text to begin with.")
#can be used to give the user a hint on what to type 
input1.pack()
#use get method to return the value typed into the textbox 

#can also create a textbox, which is a large area for the user to type in 
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#you always need the END keyword when using the insert commnand 
#can also use the get method for textboxes too
print(text.get("1.0", END))
#can also use the grid method to layout the widget. it imagines that your entire program is a grid and u can divide into any number of columns and rows u want to 
#text.grid(column = 0, row = 0)
#the column and row of these grids is relative to other widgets on the screen 
#best to place the top left widget first so all the other columns are relative 

#you can only use the layout format for the entire program, you can use a mix of all three 

#creating a spinbox 
def spinbox_used():
    print(spinbox1.get())
spinbox1 = Spinbox(from_ =0, to =10, command = spinbox_used) 
spinbox1.pack()
#dont rlly plan on using a scale(scrolling bar thing), if a time arises look at tkinter instructor notes 

#create a checkbox
checked_state = IntVar()
#checked_states keep track of the checbox by using 0 = unchecked and 1 = checked 
def checkState():
    print(checked_state.get())
checkbox1 = Checkbutton(text = "checker", variable = checked_state, command = checkState)
checkbox1.pack()
def radio_used():
    print(radio_state.get())
#create a radio button; options the user can check 
#radio_state contains the value of whichever button is currently checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#dont plan on using listbox, similair to radio buttons, look at intructor notes 










#keeps the window open and listening for any user input without it automatically closing 
#this has to be in the very end of your program 
window.mainloop()