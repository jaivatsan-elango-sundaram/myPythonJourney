#To get a certain character from a string, use can use the index to do so:
#example:
test = "hello"
print("hello"[0])
print(test[0])

#to better understand the values, you could use underscores in places of commas 
#for example:
#123_456_789 is the same 123456789

#in python, decimals are float not double 

#boolean fvalues start with a capital, either True or False 

#you cannot concatenate integers to a string 
#example:
#print("hello" + 2) - uncomment to see what happens 
#the above code will produce an error 

#the function type() will you tell the type a value is 
#example: 
print(type(3))

#use the str() function to convert values to string 
#example:
print("hello" + str(2))


#use the float() function to convert values to floats 
#example:
float(2)

#use the int() function to convert values to ints. When you convert a float to an int, it does not round
intTesting = int(2.9)
print("This is what you get when convert a double to an int (Our test value was 2.9): " + str(intTesting))

#however, you could use the round() function if you would like to actually round the number to the nearest whole number 
print(round(intTesting))

#you could also specify which decimal place you want to round it too. round(value, decimal place)
print(round(intTesting,2))
#you can add an int and a float together 

#use * for multiplication, and / for division 

#when you divide, you will end up with a float, unless you are converting it 
#example:
print(6/2)
# use ** to raise to the power of something. First number is the value being raised and the second number is the power 
#example: 
print(2 ** 3)

#PEMDAS is followed in python 

#if you peform any arithmetic operation with a float and an integer, your result will be a float    

#you could use floor division, //, to chop of the decimals after performing division
print(8 // 3)

#you can use the following shorthands: +=, -=, *=, /=

#if you want to add various values into a string, you can use an fstring
#example:
numSedans = 6
numHatchbacks = 9 
print(f"there are {numSedans} sedans and {numHatchbacks} hatchbacks in the parking lot") 

