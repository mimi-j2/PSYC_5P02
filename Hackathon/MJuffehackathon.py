import random
import numpy as np

#QUESTION 1
#make the rt range from 450 to 750
response_options = range(450, 750)

#generates random trials that raneg between 10, 20 total trials
trials = range(1, random.randrange(10, 20))

#creating a function that creates complete list of trails with randomized rts 
def complete_trials(trial_range, rt_range):
    #takes the list of the range of rts it can be
    rt = list(rt_range)
    #initializes an empty list to put participants random rts in
    rt_list = []
    #for each trial in the trial range
    for trial in trial_range:
        #randomly choose one of the rts  between the 450 and 750 range
        rand_rt = random.choice(rt)
        #append that rt to the list
        rt_list.append(rand_rt)
    #return the rt list of all the rts from a range of trials from 10-20
    return rt_list

#make a new list using our function (1 participant)
rt_list = complete_trials(trials, response_options)

#get the mean of that list of rts using numpy method (mean)
rt_mean = np.mean(rt_list)

#get the std of that list of rts using numpy method (std)
rt_sd = np.std(rt_list)

#get the max rt from the list using numpy method (max)
rt_max = np.max(rt_list)

#get the minimum rt from the list using numpy method (min)
rt_min = np.min(rt_list)

#get the total number of triials completed using the len (length of list as each rt value corresponds to one trial)
trials_done = len(rt_list)

#printing it all on screen
print(rt_list)
print(rt_mean, rt_sd, rt_max, rt_min, trials_done)

###QUESTION 2##

#assigning the lower limit to 600
lower_limit = 600

#making another function to trim rts over 600ms from the orginal list
def trim_rt(og_list, limit):
    #initializing an empty list to put our valeus we want (under 600ms)
    clean_list = []
    #initializing an empty list to put our values we don't want (over 600ms)
    dirty_list = []
    #for each item in the original list
    for n in og_list:
        #if that number in the list is under the limit
        if n < limit:
            #add it to the clean (keep) list
            clean_list.append(n)
        #if number not under the limit
        else:
            #add to the list that we do not want to keep
            dirty_list.append(n)
    #give back the clean list and the dirty list
    return clean_list, dirty_list

#uses our function and assigned the clean list to trimmed_rts and the dirty list to removed rts
#plugs in our original list and lower limit (600ms)
trimmed_rts, removed_rts = trim_rt(rt_list, lower_limit)

#to calculate the number of trials removed using the len function to count the amount of items in the dirty list
trials_removed = len(removed_rts)

#getting the new mean of values that are under 600ms
trim_mean = np.mean(trimmed_rts)

#printing our lists as well as the number of trials removed and our mean
print(trimmed_rts)
print(removed_rts)
print(trials_removed)
print(trim_mean)

###QUESTION 3##

#function to summerize the rts in a list
def summarize_rts(rt_list):
    #using numpy function mean to get the mean of an item in a list
    mean = np.mean(rt_list)
    #printining the mean
    print('the mean of the rts is ' + str(mean))
    #using numpy std to get the standard deviations between the items in a list
    std = np.std(rt_list)
    #printg the std
    print( 'the std is: ' + str(std))
    #using len to get the total trials of items in a list
    trial_tot = len(rt_list)
    #printing the trial total
    print( ' the total trials removed is: ' + str(trial_tot))
    #retruning the mean
    return mean

#applying our function to the original list to get the mean of unrtimmed rts
og_mean = summarize_rts(rt_list)

#applying our function to the cleaned list to get the mena of the trimmed rts
trim_mean = summarize_rts(trimmed_rts)

#printing out the mean, std, and trials removed of og list
og_mean 

#printing out the mean, std, and trials removed of trimmed list
trim_mean

#comparing the means of the og list and trimmed list by subtracting the menas and rounding it by two decimal places and turning it into a string to print
compare_means = "Trimmed data are faster by " + str(round(og_mean - trim_mean, 2))

#printing new string
print(compare_means)

#QUESTION 4

#I just took the part that was relevant to the means so it would be less messy
def summarize_rt_means(rt_list):
    #this part is teh same as summarize_rts function
    mean = np.mean(rt_list)
    print('the mean of the rts is ' + str(mean))
    return mean

#Setting the number of subjects to 10
NumSubj = range(1, 11)

#function that generates a dictonary of subjects and their rt list
def subject_list(subject_tot):
    #initializing an empty dictonary of subjetcs
    subjects = {}
    #initializing an empty list of means
    means = []
    #for each subject...
    for subject in subject_tot:
        #calculate a range of response options
        response_options = range(450, 750)
        #calculate a random range of trials
        trials = range(1, random.randrange(10, 20))
        #turn the range into a list
        rt = list(response_options)
        #initalize an empty list to put the rts into for each subject
        rt_list = []
        #for each trial
        for trial in trials:
            #randomly choose on of the rts
            rand_rt = random.choice(rt)
            #put that rt in the rt list
            rt_list.append(rand_rt)
        #get the mean for each subject rts (after the trials are completed)
        sub_mean = summarize_rt_means(rt_list)
        #append the subjects mean to means list so we can get our group mean of everybody later
        means.append(sub_mean)
        #save the rt_list once full of all trial rts to a subject key (assigned to subject number) as a value
        subjects[subject] = rt_list
    #return the list of the means of each subject as well as each subject and their full rt list
    return means, subjects

#get rid of np.float64 thing
#https://stackoverflow.com/questions/78630047/how-to-stop-numpy-floats-being-displayed-as-np-float64
np.set_printoptions(legacy='1.25')

#assign the variables sub_mean to the means and subject list to the subject list
sub_mean, Subject_List = subject_list(NumSubj)
#print teh subject list (so each subject and their rt list)
print(Subject_List)
#print the mean of each subject (which is in this list)
print(sub_mean)

#the group mean is the means of the means, so the average of teh average
group_mean = np.mean(sub_mean)
#print teh groups total mean
print(group_mean)

#Question 5
#using the complete_trials function from question 1 for a specific participant
rt_list_P1 = complete_trials(trials, response_options)

#creates a class that stores each participant
class Participant:
    def __init__(self, pID, rts):
        #each participant gets a participant number assigned to them
        self.pID = pID
        #each participant has a list of rts for themselves
        self.rts = rt_list
    
    #method that calculates the mean rt from the list of rts of the participant
    def mean_rt(self):
        mean_rt = np.mean(self.rts)
        #returns the mean_rt
        return mean_rt
    
    #appends a new rt to the ned of a participanst rt list
    def add_rt(self, rt):
        self.rts.append(rt)
        #prints the new rt list of that participant
        print(self.rts)
        return self.rts
    
    #determines the total trials completed for each participant using the len function
    def num_trials(self):
        total_trials = len(self.rts)
        return total_trials

#participant 1 and their rt_list from above
S01 = Participant(1, rt_list_P1)

#adds the rt 505 to the end of the list
S01.add_rt(505)
print(S01.pID)
#prints the mean of the rts after 505 is added
print(S01.mean_rt())
#prinst the total number of trials after 505 is added as is another tr trial
print(S01.num_trials())


    
        
