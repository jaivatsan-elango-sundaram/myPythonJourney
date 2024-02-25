#lets us an example
'''
#in this case the Fish class inherits from the Animal Class
class Fish(Animal):
    def __init__(self):
    #to get hold of everything a superclass does and is, use the structure below
        super().__init__()
        
'''

#working example

class Animal():
    def __init__(self):
        self.num_eyes = 2
    def breathe(self):
        print("Inhale, exhale")

class Fish(Animal):
    def __init__(self):
    #inherits the num_eyes and breathe method
        #this super().__init() call is recommended but not needed 
        super().__init__()
    def breathe(self):
        #lets say in fish class for the breathe method we want to do what the animal's breathe method does and smn extra 
        print("Underwater")
        super.breathe()
    #the above method overwrites the superclass method's breathe 
    #a subclass can also have its own methods 
    def swim(self):
        print("swimming in water.") 

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)