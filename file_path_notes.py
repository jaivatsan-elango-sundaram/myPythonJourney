#/ is the root folder
#/Work will be the Work folder (examples)
#/Work/report.doc will be the doc in the Work folder (example)
#/Work/Project/talk.ppt will be the powerpoint in the Project folder which is in the Work folder 

#this is known as an absolute file path - they start with the root folder
#it starts from the origin, the root of the computer storage system

#relative file path 

#if we were already in the talk folder, the relative path for the talk.ppt is ./talk.ppt

#if we were in the work folder, the relative file path would be ./Project/talk.ppt

#if we were going backwards, for example
#if we were in the projects folder and wanted to go to report.doc
#the relative path would be ../report.doc
#the two dots means that you are going to the parent folder 

#to find the absolute path of a file in mac, right click and click on get info 

#now we will try to try to open file_for_paths_notes.txt, even though it is in a different directory the desktop
#we will first try using the absolute path to accomplish the goal 
with open("/Users/esundara/Desktop/file_for_paths_notes.txt") as file:
    content = file.read()
    print(content)
#lets try the relative path
#do ../ how many ever times you need to go up a level
with open("../../file_for_paths_notes.txt") as file:
    content = file.read()
    print(content)
