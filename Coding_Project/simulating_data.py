##SIMULATING DATA FOR AN EXPERIMENT - SIMULATING ACCURACY AND ERROR RATES BASED ON CONDITION AND TARGET TYPE ##
#Not simulating reward because not relevant to analyze

#importing packages
import numpy as np
import pandas as pd
import random
import math
import matplotlib.pyplot as plt
import seaborn as sns

#setting up and random number generator (RNG) with a fixed seed of 21 (Lucky number!) for my starting point so I get the same sequence every time
rng = np.random.default_rng(21)

#-- POSTION VARIABLES -- #
FIX_DISTANCE = 4 #distance in degrees that stimuli appear AWAY from fixation
MIN_DIST = 4 #minimum distance stimuli have to be away from each other, we can push the shapes further away from each other to make it more difficult, play with this and see what you think
FIX_SIZE           = 0.2 # The radius of the fixation dot in degrees
TARGET_SIZE        = 2   # The size of the target shape, this value is for both the length and width
FIX_POS = (0, 0) #fixation point location
EDGE_MARGIN = 4 #degrees away from edge

#conditions#
# 0 = 1@100
# 1 = 1@50
# 2 = 1@67
# 3 = 1@80
conditions = [0, 1, 2, 3] 

part_total = range(1, 21) #how many participants in my experiment

#number of trials for each condition #
Trial_100         = [0]*100 # Number of reps for cond 1 @ 100% -100 reps
Trial_50         = [0]*50 + [1]*50 # Number of reps for cond(1@50) - 50 trials for circle and 50 trials for square
Trial_67         = [0]*100 + [1]*50 #Number of reps for cond 1@67, 100 trials for circle and 50 trials for square
Trial_80         = [0]*120 + [1]*30 # Number of reps for cond(1 @80), 120 trials for circle and 30 trials for square

# ---- DISTANCE ERROR CALCULATION SECTION ---- # 

#CREATING A PSEUDOBORDER #
#turns the size of current monitor unites from pixels to degrees
#I will be using this to help position my stimuli within screen borders of whatever monitor I am on
win_width_deg = 60.30 #0 gives width, total screen width in degrees of visual angle (my screen width is 2048 pixels so this is what it is based on)
win_height_deg = 37.69 #1 gives height, total screen height screen in degrees of visual angle (my screen height is 1280 pixels so this is what it is based on)

#horizontal position bounds of pseudoborder - equation below was figured out with help from CHAT_GPT
x_min = -win_width_deg/2 + EDGE_MARGIN #horizontal bound of the left side of screen (negative), adding the edge margin so stimulus can't get to close to border
x_max = win_width_deg/2 - EDGE_MARGIN #horizontal bound of right side of screen (positive), subtracting the edge margin so it does not appear to close to border

#vertical position bounds of pseduoborder
y_min = -win_height_deg/2 + EDGE_MARGIN #bottom of screen limit
y_max = win_height_deg/2 - EDGE_MARGIN #top of screen limit


## SETTING THE STIMULI IN RANDOM POSITIONS ##
def rand_pos():
    """
    determines random positions of stimuli (in this case circle and square) on a 2D axis within a pseudoborder
    """
    global x_min, x_max, y_min, y_max, FIX_POS, FIX_DISTANCE, MIN_DIST
    #avoid fixation area and avoid each stimulus appearing on top of each other
    while True:
        #puts target on random position on x-axis
        pos_x_c = random.uniform(x_min, x_max) #picks a random x position between the right and left bounds for the CIRCLE stimulus
        pos_x_s = random.uniform(x_min, x_max) #picks a random x position between the right and left bounds for the SQUARE stimulus
        #puts target on random position on y-axis
        pos_y_c = random.uniform(y_min, y_max) #picks a random y position between the top and bottom bounds for the CIRCLE stimulus
        pos_y_s = random.uniform(y_min, y_max) #picks a random y position between the top and bottom bounds for the SQUARE stimulus
        
            
        #set the position of the CIRCLE stimulus to a random position 
        pos_c = (pos_x_c, pos_y_c)

        #set the position of the SQUARE stimulus to a random psotion
        pos_s = (pos_x_s, pos_y_s)
        

        #Caclulating point distance between fixation and point for CIRCLE stimulus
        pos_dis_c = math.dist(pos_c, FIX_POS)
        
        #Calculating point distance between fixation and point for SQUARE stimulus
        pos_dis_s = math.dist(pos_s, FIX_POS)
        
        #computing stimulus distance away from each other, using same logic as above
        #this allows you to see how far each position is away from each other
        stim_dis = math.dist(pos_c, pos_s)
        
    # This checks that if the distance between two points (either distance between stimulus and fixation or distance between stimulus and stimulus) are too close then to continue loop until they are far enough away from each other
        if (pos_dis_c >= FIX_DISTANCE and #is distance of x and y for CIRCLE stimulus far enough from fixation
        pos_dis_s >= FIX_DISTANCE and #is distance of x and y for SQUARE stimulus far enough from fixation
        stim_dis >= MIN_DIST):  #is distance of x from square and x from circle and y from square and y from circle far away from each other
            break
    return pos_c, pos_s, stim_dis  #return the distance of the stims away from each other


#calculates the error probability based on the degree of seperation between the two stimuli (square and circle)
#I needed help from Chat GPT for error_prob function as I was unsure of the math
#midpoint sets the seperation in which error probability is around 0.5 percent - which is above the amount the stimuli can be seperated in the experiment, but is honestly just a guess from me
# CALCULATE ERROR BASED ON DISTANCE
def error_prob(separation, steepness=0.03, midpoint=100):
    """
    #this one is specifically is that as SEPERATION between two points INCREASES error probability INCREASES
    
    Logistic function: higher separation → higher error probability.
    steepness: controls slope; midpoint: separation at 50% error.
    """
    return 1 / (1 + np.exp(-steepness * (separation - midpoint)))

## COLOR ERROR CALCULATION SECTION ##
#could also include stimuli difference but I am keeping this more simple for my sanity - also I have no idea how difference between stimuli color affects error rate
def color_sep(alt_min_sep = 15, alt_max_sep = 110):
    while True:
        target_hue = rng.uniform(0, 360) #returns a random float from 0 to 360 degrees in color
        alt_hue = rng.uniform(0, 360) #returns a random float from 0 to 360 degrees in color
        hue_diff = abs(alt_hue - target_hue) #to get the difference - subtracting alt 2AFC hue - target_hue
        hue_diff = min(hue_diff, 360 - hue_diff) ##this gets the least degree of seperation number - because the numbers might be far clockwise but might be close counterclockwise
        if alt_min_sep <= hue_diff <= alt_max_sep:#if hue_diff is within the accpeted range of hue diff
            break
    return hue_diff

# ---- RANDOM HUE GENERATION TO CALCULATE ERROR BASED ON COLOR SEPERATION OF 2AFC TASK ----#
#if there are no degrees of seperation (midpoint = 0) than prob is 0.5 
def reverse_error_prob(separation, steepness= 0.03, midpoint = 0):
    """
    #this one is the opposite is that as SEPERATION between two points DECREASES error probability INCREASES
    
    Logistic function: lower separation → higher error probability.
    steepness: controls slope; midpoint: separation at 50% error.
    """
    return 1 / (1 + np.exp(steepness * (separation - midpoint)))

# ---- INITIALIZING SIMULATED EXPERIMENT FUNCTION  ---- #
#this goes through the full experiment once
def Probability(part, conditions):
    """
    Runs through all conditions for a participant
    
    part = Part_ID
    conditions = list of conditions it will run through
    
    """
    #importing global variables for function
    global Trial_100, Trial_50, Trial_67, Trial_80
    
    accuracy_list = [] #was the participant correct (1 = correct, 0 = incorrect)
    seperation_list = [] #seperation distance between the two stimuli
    error_prob_list = [] #error probability for each trial based on stimuli seperation
    trial_count = [] #trial number for each trial
    part_num = [] #participant ID number
    condition_list = [] # list what condition we are on (0 = 1@100, 1 = 1@50, 2 = 1@67, 3 = 1@80)
    target_list = [] #list of what is the target for each trial (0 = circle, 1 = square)
    color_sep_list = [] #list of color seperation between 2AFC choices for each trial
    trial_num = 0  #starting with trial = 0
    for condition in conditions:
        ## 1@100 ##
        if condition == 0: #if the probability is 100% for circle
            for each_trial in Trial_100: #for each trial
                trial_num += 1 #counting what trial we are on
                pos_c, pos_s, seperation = rand_pos() #computing position of circle, square, and seperation between the two shapes
                error_probs = error_prob(seperation) #computing error based on stimuli distance with more distance = to more error
                dist_error = error_probs * 0.2 #lowering error probability because the SQUARE is a distractor and is not relevant so I am weighing it less
                hue_diff = color_sep() #computing hue based on 360 degrees in a color wheel, 
                error_prob_color = reverse_error_prob(hue_diff)*0.5 #as difference in hue between color choices decreases , error probability increases- I am also lowering error rate- due to participants only needing to pay attention to one item
                total_error = error_prob_color + dist_error #total error is from distance between stimuli + seperation in color hue for 2AFC options
                if each_trial == 0: #if circle is the target
                #in previous experimenst the average was around 95% accuracy for circle in 1@100 - so put between 0.9 - 9.99 for total error
                    p_circle = max(0.9, 0.99 - total_error) #probability of correctness - total_error from distance and 2AFC color distance
                # each trials accuracy for circle is based on probability of correctness (which I put as .95) this rng type also samples from a binomial distribution (so 1 for correct and 0 for incorrect)
                #using rng.binomal to mimic real life variability
                    accuracy = rng.binomial(n=1, p= p_circle) 
                elif each_trial == 1: #if target is a square -WHICH IT WONT BE FOR 1@100
                #each trials accuracy for square
                    accuracy = rng.binomial(n=1, p= .6 - total_error) #probability of correctness- error from seperation of stimuli
                #appending to my lists
                accuracy_list.append(accuracy)
                seperation_list.append(seperation)
                error_prob_list.append(total_error)
                trial_count.append(trial_num)
                part_num.append(part)
                condition_list.append(condition)
                target_list.append(each_trial)
                color_sep_list.append(hue_diff)
        ## 1@50 ##
        if condition == 1: #if the probability is 50% for circle
            for each_trial in Trial_50: #for each trial
                trial_num += 1 #counting what trial we are on
                pos_c, pos_s, seperation = rand_pos() #computing position of circle, square, and seperation between the two shapes
                error_probs = error_prob(seperation) #computing error based on stimuli distance with more distance = to more error
                dist_error = error_probs * 0.9 #lowering error probability because while SQUARE is weighed just as much, people tend to still be weighted toward the circle
                hue_diff = color_sep() #computing hue based on 360 degrees in a color wheel
                error_prob_color = reverse_error_prob(hue_diff)*0.90 #as difference in hue between colro choices decreases , error probability increases
                total_error = error_prob_color + dist_error #total error is from distance between stimuli + seperation in color hue for 2AFC options
                if each_trial == 0: #if circle is the target
                #in previous experiments accuracy was 77% for the circle - I assume it will be higher with less shapes - so put between 0.75 - 0.80 error
                    p_circle = max(0.75, 0.8 - total_error) #probability of correctness - total_error from distance and 2AFC color distance, with the lowest probability it can be being 0.5 as there are only two color choices so at worse it will alwasy be a coin flip
                # each trials accuracy for circle is based on probability of correctness (which I put as .7) this rng type also samples from a binomial distribution (so 1 for correct and 0 for incorrect)
                #using rng.binomal to mimic real life variability
                    accuracy = rng.binomial(n=1, p= p_circle) 
                elif each_trial == 1: #if target is a square
                #put as .65 even though it is equal because people tend to still pay some more attendtion to circle (as least based on our previous study)
                    p_square = max(0.65, 0.75 - total_error)  #probability of correctness - total_error from distance and 2AFC color distance, with the lowest probability it can be being 0.5 as there are only two color choices so at worse it will alwasy be a coin flip
                #each trials accuracy for square
                    accuracy = rng.binomial(n=1, p= p_square) #probability of correctness- error from seperation of stimuli
                #appending to my lists
                accuracy_list.append(accuracy)
                seperation_list.append(seperation)
                error_prob_list.append(total_error)
                trial_count.append(trial_num)
                part_num.append(part)
                condition_list.append(condition)
                target_list.append(each_trial)
                color_sep_list.append(hue_diff)
        ## 1@67 ##
        if condition == 2: #if the probability is 67% for circle
            for each_trial in Trial_67: #for each trial
                trial_num += 1 #adding 1 to trial count
                pos_c, pos_s, seperation = rand_pos() #computing position of circle, square, and seperation between the two shapes
                error_probs = error_prob(seperation) #computing error based on stimuli distance with more distance = to more error
                #distance between stimuli does not matter as much if people are not paying as much attention to the lower probability item
                dist_error = error_probs * 0.5 #lowering error probability because the SQUARE has less probability so is weighed less
                hue_diff = color_sep() #computing hue based on 360 degrees in a color wheel
                error_prob_color = reverse_error_prob(hue_diff)*0.80 #as difference in hue between colro choices decreases , error probability increases
                total_error = error_prob_color + dist_error #total error is from distance between stimuli + seperation in color hue for 2AFC options
                if each_trial == 0: #if circle is the target
                #error rate generated between 0.85 - 0.90 - total_error to use in binomal function
                    p_circle = max(0.85, 0.9 - total_error) #probability of correctness - total_error from distance and 2AFC color distance, with the lowest probability it can be being 0.5 as there are only two color choices so at worse it will alwasy be a coin flip
                # each trials accuracy for circle is based on probability of correctness (which I put as .85) this rng type also samples from a binomial distribution (so 1 for correct and 0 for incorrect)
                #using rng.binomal to mimic real life variability
                    accuracy = rng.binomial(n=1, p= p_circle) 
                elif each_trial == 1: #if target is a square
                    p_square = max(0.6, 0.7 - total_error)  #probability of correctness - total_error from distance and 2AFC color distance, with the lowest probability it can be being 0.5 as there are only two color choices so at worse it will alwasy be a coin flip
                #each trials accuracy for square
                    accuracy = rng.binomial(n=1, p= p_square) #probability of correctness is .6 - error from seperation of stimuli
                #appending to my lists
                accuracy_list.append(accuracy)
                seperation_list.append(seperation)
                error_prob_list.append(total_error)
                trial_count.append(trial_num)
                part_num.append(part)
                condition_list.append(condition)
                target_list.append(each_trial)
                color_sep_list.append(hue_diff)
        ## 1@80 ##
        if condition == 3: #if the probability is 80% for circle
            for each_trial in Trial_80: #for each trial
                trial_num += 1 #adding 1 to trial count
                pos_c, pos_s, seperation = rand_pos() #computing position of circle, square, and seperation between the two shapes
                error_probs = error_prob(seperation) #computing error based on stimuli distance with more distance = to more error
                #distance between stimuli does not matter as much if people are not paying as much attention to the lower probability item
                dist_error = error_probs * 0.4 #lowering error probability because the SQUARE has less probability so is weighed less
                hue_diff = color_sep() #computing hue based on 360 degrees in a color wheel
                error_prob_color = reverse_error_prob(hue_diff)*0.70 #as difference in hue between colro choices decreases , error probability increases
                total_error = error_prob_color + dist_error #total error is from distance between stimuli + seperation in color hue for 2AFC options
                if each_trial == 0: #if circle is the target
                #error rate generated between 0.85 - 0.95 - total_error to use in binomal function
                    p_circle = max(0.85, 0.95 - total_error) #probability of correctness - total_error from distance and 2AFC color distance, with the lowest probability it can be being 0.5 as there are only two color choices so at worse it will alwasy be a coin flip
                # each trials accuracy for circle is based on probability of correctness (which I put as .85) this rng type also samples from a binomial distribution (so 1 for correct and 0 for incorrect)
                #using rng.binomal to mimic real life variability
                    accuracy = rng.binomial(n=1, p= p_circle) 
                elif each_trial == 1: #if target is a square
                    p_square = max(0.5, 0.6 - total_error)  #probability of correctness - total_error from distance and 2AFC color distance, with the lowest probability it can be being 0.5 as there are only two color choices so at worse it will alwasy be a coin flip
                #each trials accuracy for square
                    accuracy = rng.binomial(n=1, p= p_square) #probability of correctness is .6 - error from seperation of stimuli
                #appending to my lists
                accuracy_list.append(accuracy)
                seperation_list.append(seperation)
                error_prob_list.append(total_error)
                trial_count.append(trial_num)
                part_num.append(part)
                condition_list.append(condition)
                target_list.append(each_trial)
                color_sep_list.append(hue_diff)
    #returning all my lists in a dataframe
    return pd.DataFrame({
        'part_ID': part_num,
        'trial': trial_count,
        'condition': condition_list,
        'target': target_list,
        'accuracy': accuracy_list,
        'dist_sep': seperation_list,
        'color_sep' : color_sep_list,
        'total_error_prob': error_prob_list
        })

# ---- PUTTING ALL RESULTS OF SIMULATED DATA TOGETHER ---- #
all_results = [] #intialize an empty list to store all my dataframes for each participant and condition results 

for participant in part_total: #for each participant
    prob_total = Probability(participant, conditions)  #create a dataframe for each participant that has data for all conditions     
    all_results.append(prob_total) #append all my dataframes to a list

#put all the dataframes from my list of dataframes into an ultimate dataframe
df_all = pd.concat(all_results, ignore_index = True) 
df_all = df_all.round(4) #rounding floats to four decimels for readibility

print(df_all.head()) #print first 10 rows to check

##EXTRAS BELOW - NOT PART OF DATA SIMULATION - MOSTLY FOR A MIMI CHECK##
#grouping participant accuracy by condtion
group_cond_acc = df_all.groupby(['part_ID', 'condition', 'target'])['accuracy'].mean()

#plot a pivot table with the average accuracy for conditonx target for each participant
pivot_cond_acc = df_all.pivot_table(
    values='accuracy',
    index='part_ID',
    columns=['condition', 'target'],
    aggfunc='mean')

#this pivot table for accuracy for condition x target averaged across all participants
pivot_avg_cond_acc = df_all.pivot_table(
    values='accuracy',
    index = 'condition', #rows are condition
    columns='target', #columns = target
    aggfunc='mean')

#this pivot table for error for condition x target averaged across all participants
pivot_avg_cond_error = df_all.pivot_table(
    values='total_error_prob',
    columns=['condition', 'target'],
    aggfunc='mean')

#plotting accuracy by condition in bars
pivot_avg_cond_acc.plot(kind='bar')
plt.ylabel("Mean Accuracy")
plt.title("Accuracy by Condition and Target Type")
plt.legend(title="Target")
plt.show()

#plotting accurcy by condition through heatmap
sns.heatmap(pivot_avg_cond_acc, annot=True, cmap="viridis")
plt.title("Accuracy Heatmap (Condition x Target)")
plt.ylabel("Condition")
plt.xlabel("Target")
plt.show()

