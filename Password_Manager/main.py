from tkinter import *
from tkinter import messagebox
import random
#followed angela yu's python tutorial on udemy
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for char in range(nr_letters)]

    password_symbols =[random.choice(symbols) for char in range(nr_symbols)]

    password_numbers= [random.choice(numbers) for char in range(nr_numbers)]
    passwordList = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(passwordList)
    passwordEntry.insert(END, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
my_password = ""
my_website = ""
my_email = "je.sundaram@gmail.com"
def save_password():
    global my_password
    global my_website
    isEmpty = False
    my_website = websiteEntry.get() 
    my_password = passwordEntry.get()
    #deleting/clearing the entries when the user adds it. 
    websiteEntry.delete(0, END)
    passwordEntry.delete(0, END)
    #alows the user to confirm their option
    if len(my_website) == 0 or len(my_password) == 0:
        isEmpty = True
        messagebox.showwarning(title = {my_website}, message = "Make sure no fields are empty")
    if isEmpty == False:
        goAhead = messagebox.askokcancel(title = my_website, message = f"Password: {my_password}. Save?")
    if goAhead == True and isEmpty == False:
        with open("sample_passwords.txt",mode = "a") as file:
            file.write(f"{my_website} | {my_email} | {my_password} \n")
        
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx = 50, pady = 50)
#You NEED to set a width and height 
canvas = Canvas(width = 200, height = 200)
pass_image = PhotoImage(file = "logo.png")
#first two positions are the coordinates 
canvas.create_image(100, 100, image = pass_image)
canvas.grid(row=0, column=1)
websiteLabel = Label(text = "Website: ")
websiteLabel.grid(row=1, column=0)
emailLabel = Label(text ="Email/Username: ")
emailLabel.grid(row=2, column=0)
passwordLabel = Label(text = "Pasword: ")
passwordLabel.grid(row=3, column=0)
websiteEntry = Entry(width = 35)
websiteEntry.grid(row=1, column=1, columnspan=2)
websiteEntry.focus()
emailEntry = Entry(width = 35)
emailEntry.grid(row=2, column=1, columnspan=2)
emailEntry.insert(END, "je.sundaram@gmail.com")
passwordEntry = Entry(text = "Pasword: ", width = 21)
passwordEntry.grid(column = 1, row = 3)
generateButton = Button(text = "Generate", command = generate_password)
generateButton.grid(column = 2, row = 3)
addButton = Button(text = "Add password", command = save_password)
addButton.grid(column = 1, row = 4)








window.mainloop()