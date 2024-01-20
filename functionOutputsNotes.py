#you can return a value

#.title() capitalizes the starting letter in each word 
'''def format_name(first, last):
    format_first = first.title()
    format_last = last.title()
    return f"{format_first} {format_last}"
formatted_string = format_name("JAI", "sundaram")
print(formatted_string)
'''
#the return statement tells the computer that it is the end of the function and that it should exit the function
# you could also have early return function that makes it leave the function
'''def format_name(first, last):
    if first == "" or last == "":
        return "You did not provide a vald input"
    format_first = first.title()    
    format_last = last.title()
    return f"{format_first} {format_last}"
formatted_string = format_name(input("Enter first name: "), input("Enter last name: "))
print(formatted_string) '''

#docstrings are a way for us to create little bits of documentation as we are coding along, usually for a function
#it will be on the first line of the function
#surrounded by three quotation marks 
def format_name(first, last):
    """Take a first and last name and format it to return the title case version of the name. """
    if first == "" or last == "":
        return "You did not provide a vald input"
    format_first = first.title()
    format_last = last.title()
    return f"{format_first} {format_last}"
formatted_string = format_name(input("Enter first name: "), input("Enter last name: "))
print(formatted_string)

#to have a multiline string use """"
#for example:
a = """  test
"""

#it is best to use single line comments, avoid multiline comments 

