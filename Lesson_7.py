
#tulpes are fixed sets- they are unchangeable
#can have a list of cordinates that is a lits of paired tulpes

#here is our list of tulpes
coords = [(1, 1), (1, 2), (1, 3)]

#return the type list = because over all it is a LIST with tulpes in it
type(coords)

#each item indexed in the list is a tulpe
type(coords[0])

#Dictonaires are a type of data structure in python that allows you to store items in key-value pairs
#has an assigned key to reference an item
#they are not indexed by location like a list

#indexed by the keys themselves, they are key:value pairs
#the keys have to be unique, but the values can be non-unique so can't get key through values
nbaTeams = {'Los Angeles': 'Lakers', 'Toronto': 'Raptors', 'Chicago':'Bulls'}

#can also use the dict() function to construct a dictonary. Takes in a sequence of key-value pairs but slightly different in syntax
#nbaTeams = dict([('Los Angeles','Lakers'),('Toronto','Raptors'),('Miami','Heat')])

#retrieve a dictonary item by key

nbaTeams["Toronto"]

#or can use .get to retrieve a dictonary value (item)
nbaTeams.get("Toronto")

#Python has a number of libraries commonly used in (data)science to deal with n-dimensional arrays
import numpy as np

#to create an array in numpy, you have to call the array method

arr = np.array([1, 2, 3, 4, 5])

#You can seperate different dimensions of an array using:
    #first set of brackets start the function .array
    #to create a second dimension you have to create a second set of brackets
    
#below creates an array that is a size 3X3 - a multidimensional array
#multidimensional arrays require 
mdArr = np.array([[[1,2,3], [4, 5, 6]],[[1, 2, 3], [4, 5, 6]]])
print(mdArr)

arrMd = np.array([[0, 1, 2], [3, 4, 5]])

#takes first slice out of multidimensional array
arrMd[0]

#takes the item in the first row and the second column from the array
arrMd[0, 1]

#each element in mdArr is a multidimensional list 
for x in arrMd:
    print(x)
    for y in x:
        print(y)

array3d = np.array([[[0,0,0], [0, 0, 0]], [[1, 1, 1], [1, 1, 1]]])
print(array3d)

#make an array of numbers
newArr = [5,  6, 4, 7, 8]
newArr = np.array(newArr)

#create a mask - numbers in the array where it is bigger or equal to 2
mask = newArr >= 2

#apply that mask to the data to clean it up
cleanData = newArr.mask(mask)

# can also do it this way as well 
#cleanData = newArr[mask]

#our clean data is data that is larger than 2
#cleanData = newArr[newArr > 2]

newArr2 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])

x = newArr[newArr2 > 4]

#example of how we may use masks to clean up data
#cleanData = rt[(cond == 1) and (block > 4)]

#np.nonzero(a) returns all the non-zero elements

#np.where(condition, [x, y], /) returns elements from x or y depending on condition

#NaN is not a number - numpy will ignore that value

#importing a csv file as an array
data = np.loadtxt(fname = 'inflammation-01.csv', delimiter =',')


#sliciing data
print(data[0:4, 0:10])

#slicing data from the first to fourth row, and the last column
sliced = data[0,5:-1]
print(sliced)

#calculating the mean of the columns specifically
meanvalcol = np.mean(data, 0)

#printing the mean of the columns
print(meanvalcol)

#calculating the mean of the columns specifically
meanvalrow = np.mean(data, 1)

#printing the mean of the rows
print(meanvalrow)

#calculates the whole mean of one row (first whole row)
meanonerow = np.mean(data[0,:])
print(meanonerow)
#claculates the whole mean of one column (first whole column)
meanonecol = np.mean(data[:,0])
print(meanonecol)

from numpy import random

#generates a random number from 0 to 100
random.randint(100)

#generates random data of 50 columns and 10 rows
randData = random.randint(5, 10, size = [10,50])

#generates a random number from 0 to 1
random.rand()

#random choice takes an argument of an array that is one dimension long (so either from a column or a row)
random.choice(data[0,:])

#makes a list of conditions
conds = [1, 0, 2]

#shuffles the list - changes the original list
random.shuffle(conds)

arrg = np.arange(9).reshape((3, 3))
#generates a new array that is shuffled based on the original array = so does not change the orginal list
random.permutation(arrg)

#can simulate data on a normal curve

#numpy is mainly for numbers while pandas is also able to deal with different kinds of data better, like text based 
#pandas can handle multiple data types at once while numpy cannot

#Series = is a one dimensional array and can handle multiple data types
#Dataframe = is two ddimensional and can handle multiple data types

import pandas as pd

#a series in pandas is simply a 1 dimensional list with only 1 column

pd.Series(['4 cups','1 cup', '2 large', '1 can'])

volumes = pd.Series(data = ['4 cups','1 cup', '2 large', '1 can'])

 #different data types in one series
s = pd.Series(data= [1, '2',3, 4, '5', 6, 7, 8, '99', '100'])

#will turn all strings into an integer in a series
#can also turn all integers into a string as well
x = s.astype('int')

#computes the mean of our new series of integers
x.mean()

#pd.NA is no data or missing data
data = pd.Series([1, 2, pd.NA, 4,5])

#this will drop all missing values
data.dropna(inplace=True)


data = pd.Series([1, 2, pd.NA, 4,5])

#replace the missing data with Null when previously it was NA
data.fillna('Null', inplace = True)


data = pd.Series([1, 2, 3, 4, 5])

#if there is function you want to apply from  or scipy you can use the apply method to call it (such as np.sqrt from numpy)
data.apply(np.sqrt)

#we are applying our own function where we add one to each notion of x (so each number in the list)
#lambda applies it to the series and transforms it with teh function we created 
data.apply(lambda x: x + 1)

data = pd.read_csv('RTdata.csv')

#can see all the rows from a specific column by 
data['subjs']

#can also see info from a specific column and from a specific row ( so see a specific data point)
data['subjs'][5]

#index_col lets you choose what column you want to index by
data = pd.read_csv('RTdata.csv', index_col = 'subjs')

#can index and specify a location within a DataFrame using row x column indices using iloc
#range of 
data.iloc[2:5, 2:5]

#takes all the columns in K 
# list of rows and name of column
data.loc[:, 'K']

#first bracket by rows and second bracket by columns
data[:]['K']

#able to seperate the data by race and sex and then get the mean for each group
data.groupby(['sex','race']).mean()

data.loc[:,'sex']

titanic = pd.read_csv('titanic.csv')

#creates a new column of only the last names 
titanic["Surname"] = titanic["Name"].str.split(',').str.get(0)

