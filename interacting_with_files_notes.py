#using file_for_notes.txt
'''
#use the open command to open a file
#we shall open files_for_notes.txt and then save it to a variable 
file = open("file_for_notes.txt")
#can read the file using the read method. the method returns the contents of the file
contents = file.read()
print(contents)
#once were done with the files we have to close it 
file.close()
#we close the file to free up the resources by closing it. otherwise, the system may automatically close the file or that may not even happen. bettter to tell it to close the files manually 
'''
#there is also another way to open up files and use them 
#use the with keyword and name it as the variable you will use to interact with the file. so in this case we name the variable file
with open("file_for_notes.txt") as file: 
    contents = file.read()
    print(contents)
#nest the commands into the calling
#with this way, we do not have to manually close the file. It will close after all the commands are down executin. 
    
#can also write to the file 
#similair way 
#the second parameter is the mode, it is set to "read" in default 
with open("file_for_notes.txt", mode = "w") as file:
    file.write("i also like m2s")
'''
previously the file said:
i love m340is. :D
hellcats are also cool

now it says:
i also like m2s.
'''
#you can also just add to a file by having the mode as "a", which stands for append
with open("file_for_notes.txt", mode = "a") as file:
    file.write("\ntryna learn more about bmws")
#this adds text after a new line
#if you attempt to open a file that does not exist in write mode, the system will create the file for you 
#this ONLY occurs in write mode 
#.readlines() lists a list containing each line of the program 