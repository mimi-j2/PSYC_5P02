# can use ! before your command to use bash commands
# python script is saved as  .py

#Python libraries - can add libraries to your script/session, you can expand on capabilities, this are pre made packaged libraries
#gotta import libraries and name it in your script to activate it in your code

import numpy as np

#now can use functions in that package - this is the sqrt function from the library numpy in which we are using the abriveation np to call it
#when just calling the variable or function by itself it will tell you what its data type is (in this case it is a float)- use print to just get the number
number = np.sqrt(4)
np.sqrt(4)
number
print(np.sqrt(4))
print(number)

#can also specify sub-packages or specific methods from a library (as seen below to get only speciifc things and not the whole library)
from math import cos, pi

#only imported cos and pi from math so do not need a prefix name (like np) can just call the methods as long as they are unique
print('cos(pi) is', cos(pi))

myVar = "hello world" #writing hello world to myVar

#Loops! repeats until a specific condition is met
    # Two loops in Python
        # A for loop - that runs for a present number of times
        # A while loop- is repeated as long as an expression is true (keeps running until conditional returns a false)
        
#For loop Example:

    #for loop uses a variable which is defined as a series of values (in this case 1 through 5)
    #ranges are non-inclusive so range(1,5) only prints the numbers 1-4 (does not include final number, which is 5)

for i in range(1,5):
    print("I am in a loop")
    print(i)

print("I am out of a the loop")

#indenting is important! Make sure your indenting is consistent - eveyrthing in the indent after the for loop starts is in the for loop and as soon as you unindent the loop is done and it steps out of the loop and can't get back in
#l is equal to 4 because we defined it in the loop and it stops at 4

for l in range(1,5):
    print("I am in the loop")
print(l)

#New loop - x is going to take the value of each value in that list, each time it loops move to a new value
mylist = ["apple", "banana", "cherry"]
for x in mylist:
    print(x)

#converts list which is a string and converting it into numerical values (int), r
mylist = ["apple", "banana", "cherry"]
for n in range(len(mylist)):
    print(n)

myRange = range(len(mylist))

#Note: putting clear in yoru console clears up your console

#While Loop Example
# i += 1, i starts at 1 and at the end of each loop will add 1 to i so starts out as i (1) < 6 and next loop its i (2) < 6 and keeps going until i is no longer < 6
i = 1
while i < 6:
    print(i)
    i += 1
    
#the break command will exit out of the loop entirley
#if i == 3:
#    break

#the continue command will skip the remaining commands in the loop and move on to the next loop iteration
#so in this case if i is equal to 3, it will skip into the next iteration without printing i
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


for i in range(0,5):
    x = i
    print(x)

print(i)
print(x)

#for creating experiments the Random library/ methods helps randomize thinsg like stimuli 
# random number generators (RNG) are seeded (they are tied to a specific value) - if someone has the same seed as they can experience the same thing

import random

#prints a random number from 0 to 10 - not the same as range
print(random.randint(0,10))

#prints you the state of your current random number generator
print(random.getstate())

#this creates a tuple that has your state
myState = random.getstate()

#saving your state of your random generator
random.setstate(myState)

#sets seed of RNG to 1, gives participants a certain seed- this makes it so you can replicate random things like assigning participants numbers to a specific seed - try to control the randomness a bit
random.seed(1)

#tab lists all the possible methods contained in a particullar library - can auto complete commands
#ctrl and left arrow or ctrl and right arrow lets you move cursor quickly

#Functions - way to reuse code to increase effeciency, can assign a function to carry out a particular task
#functions can also take arguments (inputs) and can return values (outputs) - python has a lot of built in functions but we can create our own to do what we want

#Function Example:
#name is an argument, it does not need to exist it is a label - a stand in for some other code you want to put in there

def nameprintfunc(name):
    myname = print('The name is ' + name)
    return myname

nameprintfunc("Mimi")

#Scope - region of the code in which a variable or resource is visible and accessible
# global variables (things not within a function) these exist without an indent
# Built-in scope - these are built into python
# things within a function are considered local scope as they only exist within a function
# x only exists in the function it does not exist as a global variable only as a local variable
#alwasy use return in functions to return something and get out of the function - close it or else your local variables will bleed out

def adderfunc(val):
    x = val + val
    print(x)
    return x

adderfunc(2)

#now I have created a variable of x that is a different x from the x in the local scope
x = adderfunc(2)

#you can have some arguments optional by setting a deafault value
#below we set the default value to 4 so if I don't put an argument when I call the function it will use 4 as a default

#can also return multiple variables - will return both x and y

def addtwofunc(val1 = 1, val2 = 4):
    '''
    
    x = adds two values
    y = adds two values and then multiples by two
    returns both results
    
    triple quotes are for multi line comments while # is for single line comments

    '''
    x = val1 + val2
    y = (val1 + val2) * 2
    return x, y

addtwofunc()

#to assign these two outputs from each (from x and y) specify two variables when recalling - this creates two seperate variables with a having the x value and b having the y value
a, b = addtwofunc()

#this creates a tuple with the two output values- which is unchangeable
c = addtwofunc()

#Classes- they are like functions that have data, a way to combine functions and data- its a good way to build flexibility in the code and re-use common procedures

#class has attributes (data) and methods (operations)
# for example for a class called car- create attrubutes such as color and model
# for this same class methods may be - drive and brake

class car:
    def __init__(self, color = 'white'): #all classes has an init definition where initialize the attributes of every instance of the class, and I set the default color of the car to white, self refers to THIS object
        self.speed = 0 #self allows you to access variable
        self.color = color #color is defined by (optional) input

    def drive(self):                #this is a method for the object (car)
        self.speed = self.speed + 1
        
    def breaking(self):
        self.speed = self.speed - 1
        
vw = car() #creates a variable of vw of object car

vw.speed #returns the speed of this object (car)

vw.drive() #calls the object and function that increases the speed by 1

vw.speed #now the speed should be 1 as vw.drive() increased the speed of the car

for i in range(1, 100): #for 99 times in a row increase the speed of vw
    vw.drive()

print(vw.speed) #now the speed of vw is 100

#can import classes from a script so can call a class into another script like a public library
