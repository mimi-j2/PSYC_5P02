import random
import numpy as np

#makes an empty list
randomlist = []

#does a loop where it repetes the normalvariate function 100 times
for n in range(100):
    #produces random numbers in a normal distribution with a mean of 0.7 and a standard deviation of 0.2
    generate = random.normalvariate(0.7, 0.2)
    #appends what was generated to an empty list
    randomlist.append(generate)

#this is me just checking
print(np.mean(randomlist))
print(randomlist)
print(len(randomlist))

#this is to check if upper bound is working
#randomlist.extend([1.5])


#definition to take out outlier data and produce clean outlier-free data
def outlier_data(data, threshold = 2.5):

    #defining outlier list
    outliers = []
    #defining clean data list - to put non-outliers
    clean_data = []
 
    #where we store if it is an outlier or not numbers
    outlier_count = []
    
    #will calculate the inital mean of the data
    mean = np.mean(data)
    #will calculate the inital standard deviation of the data
    std = np.std(data)
    
    #will calculate the inital lower bound - 2.5 std below the threshold
    lower_bound = mean - threshold * std
    #will calculate the inital upper bound - 2.5 standard deviations above the threshold
    upper_bound = mean + threshold * std
    
    #this goes over each data point and determines if it is anoutlier with the new parameters set
    #0 = is not an outlier
    #1 = is an outlier
    for n in data:
        if lower_bound <= n <= upper_bound:
            outlier_count.append(0)  
        else:
            outlier_count.append(1)

    #if there are no outliers in the data just put the data into clean_data
    if sum(outlier_count) == 0:
        for num in data:
            clean_data.append(num)
        data = clean_data
    
    #loop where while there are any outliers (sum of outlier count is over 0) in the list it will do the calculation
    else:
        while sum(outlier_count) != 0:
            
            #making the list empty again
            clean_data = []
            
            #if the number is within the lower and upper bound add it ot the clean data
            #online help for the between bounds: https://stackoverflow.com/questions/13628791/determine-whether-integer-is-between-two-other-integers
            for num in data:
                if lower_bound <= num <= upper_bound:
                    clean_data.append(num)
                #if num is not within the bounds then add it to outliers
                else:
                    outliers.append(num)
    
            #will calculate the new mean of the data
            mean = np.mean(clean_data)
            #will calculate the new standard deviation of the data
            std = np.std(clean_data)
            
            #will calculate the new lower bound - 2.5 std below the threshold
            lower_bound = mean - threshold * std
            #will calculate the new upper bound - 2.5 standard deviations above the threshold
            upper_bound = mean + threshold * std
            
            #reseting the outlier list
            outlier_count = []
            
            #this goes over each data point and determines if it is anoutlier with the new parameters set
            #0 = is not an outlier
            #1 = is an outlier
            for n in data:
                if lower_bound <= n <= upper_bound:
                    outlier_count.append(0)  
                else:
                    outlier_count.append(1)
                
            #making data equal the new data
            data = clean_data
            
            #if the sum is equal to 0 (which means no outliers) it will break
            if sum(outlier_count) == 0:
                break

    return clean_data

#create a new list where the outlier_data function is applied
cleanedlist = outlier_data(randomlist)
print(cleanedlist)
print(len(cleanedlist))

#produces mean of the cleaned list
mean = np.mean(cleanedlist)
print("my mean is: " + str(mean))

#produces standard deviation of the clean list
std = np.std(cleanedlist)
print("my standard deviation is: " + str(std))

#Produces number of outliers removed by procedue
outliers = 100 - len(cleanedlist)
print("I removed " + str(outliers) + " outliers")


###     EVERYTHING BELOW HERE IS CHECKS FOR ME   ####

#old randomlist comparison
mean2 = np.mean(randomlist)
std2 = np.std(randomlist)
lower_bound = mean2 - 2.5 * std2
upper_bound = mean2 + 2.5 * std2

outlier_count1 = []

for n in randomlist:
    if n < lower_bound:
        outlier_count1.append(1)
    elif n > upper_bound:
        outlier_count1.append(1)
    else:
        outlier_count1.append(0)

print(len(outlier_count1))
print(outlier_count1)

#checking for leftover outliers
lower_bound1 = mean - 2.5 * std
upper_bound1 = mean + 2.5 * std


outlier_count = []

for n in cleanedlist:
    if n < lower_bound1:
        outlier_count.append(1)
    elif n > upper_bound1:
        outlier_count.append(1)
    else:
        outlier_count.append(0)

print(len(outlier_count))
print(outlier_count)

#recursive check
clean_data = []
outliers = []
data = randomlist 

for num in data:
    if lower_bound <= num <= upper_bound:
        clean_data.append(num)
    #if num is not add it to outliers
    else:
        outliers.append(num)



print(len(outliers))
print(len(clean_data))


# OLD DATA

# #for random list comparison
# lower_outliers = randomlist < lower_bound
# upper_outliers = randomlist > upper_bound
# print(lower_bound, upper_bound)
# total_outliers = lower_outliers + upper_outliers
# print(total_outliers)
# all(total_outliers)

# #for cleaned list
# lower_outliers1 = cleanedlist < lower_bound1
# upper_outliers1 = cleanedlist > upper_bound1
# total_outliers1 = lower_outliers1 + upper_outliers1
# print(total_outliers1)


#OLD
        #this recalculates the True and False of if the data is an outlier or not
        #False = not an outlier
        #True - an outlier
        # lower_outliers = data < lower_bound
        # upper_outliers = data > upper_bound
        # total_outliers = lower_outliers + upper_outliers