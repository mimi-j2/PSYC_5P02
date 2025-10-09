#Problem Set 2 Answers

import random
import numpy as np

#QUESTION 1

 '''      CODE STEPS FOR FINDING OUTLIERS
#think of code creating in steps so if trying to make a function to remove outliers
# Start by reading in data 
#then code mean and standard deviation 
#add lower and upper bound for outliers
#find all outliers in data
# were there outliers?
             # if no - STOP
             #if yes - do it again, recalculate mean and standard deviation '''

#create 100 random numbers with a mean of 0.7 and sd of 0.2 and put them in a list
random_numbers = [random.normalvariate(0.7, 0.2) for n in range(100)]

threshold = 2.5 #cutoff threshold - 2.5 above and below the mean

mean = np.mean(random_numbers) #calculate mean
sd = np.sd(random_numbers) #calculate sd

#transform it into a numpy array
data = np.array(data)

#calculate boundaires 2.5 sd above and below the mean
upper_limit = mean + threshold*sd
lower_limit - mean - threshold*sd

#removing outliers using a for loop
#value gets assigned a data point in data and if a data point is within the lower_limit and upper_limit it will put that in a new list called cleaned_data
cleaned_data = [value for value in random_numbers if lower_limit <= value >= upper_limit]

num_CleanedData = []
def trimmMeans(data, threshold):
    while True:
        
        #clean the list to start over
        num_CleanedData = []
        
        mean = np.mean(random_numbers) #calculate mean
        sd = np.sd(random_numbers) #calculate sd
        
        #transform it into a numpy array
        data = np.array(data)
        
        #calculate boundaires 2.5 sd above and below the mean
        upper_limit = mean + threshold*sd
        lower_limit - mean - threshold*sd
        
        #removing outliers using masking
        #remove outliers in numpy slicing, creates a mask and where the values are within the boundaries put it in a new list called num_CleanedData
        #the data in front is the orginal data that we are taking from and if a value within our boolen is true it will take that data and put it in a new list
        num_CleanedData = data[(data>upper_limit) & (data>lower_limit)]
        
        #if old data and new data are the same length (have the same amount of items in it- break)
        if len(num_CleanedData) == len(data):
            break
        #if the cleaned data (data from current loop) and old data (either original data or data from last loop) are not the same it means something was taken out so make data equal to the cleaned data and start again
        else:
            data = num_CleanedData
    
        return num_CleanedData

#QUESTION 2

names = ["Alyssa", "Rosa", "Christine", "Holly", "Joel", "Mimi"]
grades = np.random.randint(71, 90,6)

#variable all is a list of list
all = [["Alyssa", 88], ["Rosa", 90]]

#to get just the grade 88 from ALyssa then you do this
# and if I wanted to get just Alyssa then the index would be [0][0]
# because this is a list inside a list so I need to index to the specific list and then index to a specific variable within that list (which in itself is in a list)
all[0][1]

#.index will give you 
names.index("Joel")


inputName = input("Please enter a name: ")

#find the location in my varriable names that correspond to that word
idx = names.index(inputName)

#once I have the name pull out the grade for that name that is in the same location index wise (idx is same)
print(names[idx] + "s grade is:" + str(grades[idx]))

#when you loop through a list the value in the thing your looping (so the i in for i in names) becomes the actual value of the object
# this will print out all the names and all the grades in order 
#the range(len(names)) then makes the i a number (index number) instead of the value itself, which would be the name
for i in range(len(names)):
#this allows you to use it as a index so it is saying print out the name in position 1 and grade in position i
    print(names[i] + ", grade: " + str(grades[i]))
    