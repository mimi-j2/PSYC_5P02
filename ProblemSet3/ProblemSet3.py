from psychopy import visual, event, core, data, gui
from psychopy.tools.filetools import fromFile
import random
import numpy as np


##creating a dictonary called info to store participant number
#sets experiment name to VisualSearch
expName = 'VisualSearch'

##making the key called participant = to nothing
##https://discourse.psychopy.org/t/saving-data-from-gui-input/9822
#brings up a input box for participants
dlg = gui.Dlg()
#asks for subject ID
dlg.addField('SubjectID:')
#asks for number of trials
dlg.addField('Trials Per Cond:')
#shows dlg box on screen to user
ok_data = dlg.show()
#quits if the user does not click OK
if not dlg.OK:
    core.quit()

#sets sub_ID to user input of participant number
sub_ID = dlg.data[0]
#sets trials to the integer of the input
trials = int(dlg.data[1])

#names the file the subject ID plus the experiment name
fileName = sub_ID + "_" + expName

#opens the datafile we just created as a csv file ready to write in it (w)
dataFile = open(fileName+'.csv', 'w')

##SetSize what setsize condition it is
##TP = is target present or not (0 or 1)
##RT = Response Time
##Correct = if correct or not (0 or 1)
##Missed = if got it wrong because could nto respond in time
#this sets our columns that we want to write in , /n is new line
dataFile.write('SetSize,TP, RT, Correct, Missed\n')

#creatng our window to draw on
#fullscreen is false so it wont take up the whole screen
win = visual.Window([400,400], fullscr = False, units = 'pix')



#the set size conditions
conditions = [5, 8, 12]

#size of stimulus, if I need to change something later easier to change it once here
stim_size = 30

#gets target stimuli from stimuli folder (T)
T = visual.ImageStim(win,'Stimuli\T.png', size = stim_size)

#gets distractor stimuli from stimuli folder (L)
L = visual.ImageStim(win,'Stimuli\L.png', size = stim_size)

#this sets the positions and orientations of all my stimuli and draws them on the screen
def pos_and_ori(target, distract, samp_size):
    #making a list from number -190 to 190 with step of 25 betweeen each number to prevent letters from being stacked on top of each other
    samplelist = list(range(-180, 180, 25))
    #randomly sampling numbers from the samplelist above up to the setsize of the list for the x-values, the last x-value in the list is ofr the target
    x = random.sample(samplelist, samp_size)
    #doing the same for the y values, the last y-value in the list is for the target
    y = random.sample(samplelist, samp_size)
    #this for loop randomly changes the orientation, and position of my distractors
    #for up to the amount of numbers in my set size - 1
    for n in range(0, samp_size - 1):
        #possible orientations
        orientations = [0, 90, 180, 270]
        #randomly choose an orientation for each distractor
        orin = random.choice(orientations)
        #apply the orientation to the distractor
        distract.ori = orin
        #change the x and y position of the distractors to the number in the index of what set size number we are 
        distract.pos = (x[n], y[n])
        #draw the distractor on the window
        distract.draw()
    #for the last value in the samp_size generate the target in the position of the last x and y values
    for n in range(samp_size - 1, samp_size):
        target.pos = (x[n], y[n])
        #draw the target on teh window
        target.draw()
    #returns the distractor and target to draw them on screen
    return distract, target

#this one takes the range of trials as a list as well as the total_trials for each condition to determien where half of the trials would be
#this allows it to determine if in a trial the target would be present or not (this way ensures that in around 50% of trials the target WILL be present in a random order)
#also takes your stimuli and conditions as well so it knows what to draw and how many to draw(see above) from pos and ori
def targ_pres(trial_list, total_trials, distract, target, condition_index):
    #randomly chooses a number out of the list in the range of trials and assigns it to pres or not
    pres_or_not = random.choice(trial_list)
    #that number is then removed from the trial list so that it can not be chosen again for future trials
    trial_list.remove(pres_or_not)
    #if the number in pres or not is smaller than the median (smaller than half the numbers)
    #the target WILL NOT be present
    if pres_or_not <= np.median(total_trials):
        #targ_there is made to equal 0 which means target is not present
        targ_there = 0
        #draws the version of stimuli on the screen that does not include the target
        stimuli = pos_and_ori(distract, distract, condition)
    #if pres_or_not is bigger than the median (bigger than half the numbers in the range)
    #the target WILL be present
    else:
        #sets targ there = 1 which means that the target is present
        targ_there = 1
        #draws the stimuli that includes distractors + the target
        stimuli = pos_and_ori(target, distract, condition)
    #returns if the target was present, and returns the drawn stimuli
    return targ_there, stimuli



#definition that states while the timer is under the trial duration take key input from select keys and once key is pressed or trial time expires break the loop
#response usually starts at NONE and same with rt and are defined in this function, as there are no response yet, 
#resp is what the first key pressed is stored as
#rt is the response time that goes with when the key was pressed
def KeyGet(trial_duration = 2.0, rt = None, resp = None):
    #start timer
    startTime = core.getTime() #marks the time of the start of each trial when the stimulus is shown
    #while the timer (which is reset for each trial)minus the start time (so it is never negative) is lower than the trial duration and there is currently no response from the user present stimulsu and wait for response for 2 seconds
    while core.getTime() - startTime < trial_duration and resp is None:
        #this sets what the keys are going to be for the trail which is a for absent, d for there, and escape to leave
        #the timeStamped modifier gets the time the key was pressed
        #d = dere (target present)
        #a = absent (target absent)
        #escape to quit program
        keys = event.getKeys(keyList = ['a','d', 'escape'])
        #if a key is pressed then break loop
        if keys:
            #specifically first set variable key to letter pressed and then set rt to the timeStamped (the second item in a list of lists)
            key = keys[0]
            #response time is current time when key is pressed - the startTime of the trial when the stimuli was shown
            rt = core.getTime() - startTime
            #if key is as set resp to a and break loop
            if key == 'a':
                resp = 'a'
                break
            #if key is d set resp to d and break loop
            elif key == 'd':
                resp = 'd'
                break
            #if key is escape quit program
            elif key == 'escape':
                core.quit()
        core.wait(0.01) #prevent CPU overload
    #if timer exceeds 2 seconds and there is no response set resp to no response, rt to NA, 
    if resp is None:
        resp = 'no_response'
        rt = 999 #will write 999 in the file for RTS with no response
    return resp, rt

#takes the response of resp and rt to provide feedback to the user about thier performance
def Response(resp, rt, targ_there):
    if resp == 'd' and targ_there == 1: #saying target is there when it is there
        corr = 1 #set corr to 1, 1 = correct
        feedback = 'Correct!'  #feedback to correct
        response_time = round(rt, 2) #response time to rt (the timetsamped key press to 2 decimal points
    elif resp == 'a' and targ_there == 1: #saying target is absent when it is there
        corr = 0 #set corr to 0, 0 = wrong
        feedback = 'Incorrect!' #feedback to Incorrect
        response_time = round(rt, 2) #response time to rt to 2 decimal places
    elif resp =='a' and targ_there == 0: #saying target is absent when it is absent
        corr = 1 #set corr to 1
        feedback = 'Correct!' #feedback to Correct
        response_time = round(rt, 2) #rt
    elif resp == 'd' and targ_there == 0: #saying that the target is there when it is not present
        corr = 0 #set corr to 0
        feedback = 'Incorrect' #feedback to incorrect
        response_time = round(rt, 2) #round rt to 2 decimals
    elif resp == 'no_response': #if participant times out of trial without giving a response
        corr = 0 #set corr to 0, since did not answer did not get it correct
        feedback = 'No Response' #feedback to no response
        response_time = 'NA' #response time to rt, which since there is no response is NA
    #returns the corr (0 or 1), feedback (correct, not, no response) and response_time (rt)
    return corr, feedback, response_time


#https://codewithsusan.com/notes/psychopy-easy-introduction/2-coding-experiments
#Thanks Susan
#this is the starting wlecome text
welcome = ''''
Welcome to the Visual Search Taks Experiment

You will see an assortment of shapes in different positions and orientations
Most of these shapes will be an 'L' shape
However among these 'L' shapes there may be a 'T' shape

Your task for each trial is to try to find the 'T' shape and report if it is present on screen

If the T is present on screen press the 'd' key to indictae that the T is there
If the T is not present on screen press the 'a' key to indicate that the T is absent

Each trial will only be present for a short time, so respond quickly!
You will be gievn feedback on your response time 
and if you were correct after each trial

press SPACE to begin 5 practice trials
'''

#this welcome text put into a textstim called instructions
instructions = visual.TextStim(win, color='white', text=welcome, units='pix', height=10)
#drawing instructions on the backend screen
instructions.draw()
#flipping instructions to the screen
win.flip()
#will not move to actual task until the space key is pressed
keys = event.waitKeys(keyList=['space'])
#this wait is so key presses don't bleed over
core.wait(0.25)

#sets the number of practice trials to 5
practice_trials = range(1, 6)

##PRACTICE TRIALS ###
for condition in conditions:
    #appear is a list of total trials and is used to determine if the target will appear yes or no
    #does this for each condition, so starts with a clean list to remove from
    appear = list(practice_trials)
##Practice trials have 5 trials for each condition
#Needed to use chatGPT for this i didn't realize I was overwriting trials I just had to change it to prac_trials
    for prac_trials in practice_trials:
        #assigns targ_there to (0 or 1) if target is present in that trial yes or no
        #it also takes teh drawn stimuli from targ_pres
        targ_there, stimuli = targ_pres(appear, practice_trials, L, T, condition)
        #set resp to none at start of each trial to change later
        resp = None
        #set rt to None so can change it later, also this clears it for each trial
        rt = None
        #present the stimulus
        win.flip()
##STIMULUS ON SCREEN AND PARTICIPANT NEEDS TO RESPOND ###
        #while the timer (which gets a new CurrentTime minus StartTime (when each trial starts) is lower than the trial duration and there is currently no response from the user present stimulsu and wait for response for 2 seconds
        #resp is assigned to the key response and rt is assigned to the response time
        resp, rt = KeyGet()
##RESPONSE SECTION ###
        #sets the varriables corr, feedback, and response_time to the variables corr, feedback, and response time to use for feedback and data collection
        corr, feedback, response_time = Response(resp, rt, targ_there)
##FEEDBACK SECTION ###
        #print feedback if got correct or not, in a certain position with a size of 40 pix
        cor_feedback = visual.TextStim(win, text=feedback, pos = (0, 30), height = 40)
        #print response time below cor or not feedback
        back_rt = visual.TextStim(win, text=response_time, pos = (0, -30), height = 40)
        #draw feedback on screen
        cor_feedback.draw()
        #draw rt time on screen
        back_rt.draw()
        #window flip (this clears stimulus and puts feedback on screen instead)
        win.flip()
        #wait for .25 seconds before going to next trial so participant sees feedback
        core.wait(0.5)

welcome = ''''
Congrats you have done the practice trials!
Now for the real thing!

Remember:
You will see an assortment of shapes in different positions and orientations
Most of these shapes will be an 'L' shape
However among these 'L' shapes there may be a 'T' shape

Your task for each trial is to try to find the 'T' shape and report if it is present on screen

If the T is present on screen press the 'd' key to indictae that the T is there
If the T is not present on screen press the 'a' key to indicate that the T is absent

Each trial will only be present for a short time, so respond quickly!
You will be gievn feedback on your response time 
and if you were correct after each trial

press SPACE to begin the Real Trials

'''

#overwriting previous instructions
instructions = visual.TextStim(win, color='white', text=welcome, units='pix', height=10)
#drawing instructions on the backend screen
instructions.draw()
#flipping instructions to the screen
win.flip()
#will not move to actual task until the space key is pressed
keys = event.waitKeys(keyList=['space'])

#this wait is so key presses don't bleed over
core.wait(0.25)

#set total trials from the range of 1 to the trials input at start dialog box + 1 since range will always stop short of the last number
total_trials = range(1, trials + 1)

#making a list of reaction times so can get the average reaction time at the end
rt_list = []
#making a list of if participant got it correct or not so can get average correctedness at the end
corr_list = []
#making a list of when someone didn't respond so can get a total of missed responses at the end
miss_rt_list = []

### REAL TRIALS ###
#shuffles the conditions so starting with the different conditions each time to avoid practice or fatigue effects
random.shuffle(conditions)
for condition in conditions:
    #appear is a list of total trials and is used to determine if the target will appear yes or no
    #does this for each condition, so starts with a clean list to remove from
    appear = list(total_trials)
    ##FOR EACH TRIAL OUT OF TRIALS INDICATED AT START ###
    for trial in total_trials:
        targ_there, stimuli = targ_pres(appear, total_trials, L, T, condition)
        #set resp to none at start of each trial to change later
        resp = None
        #set rt to None so can change it later, also this clears it for each trial
        rt = None
        #present the stimulus
        win.flip()
##STIMULUS ON SCREEN AND PARTICIPANT NEEDS TO RESPOND ###
        #while the current time - the startTime is lower than the trial duration and there is currently no response from the user present stimulsu and wait for response for 2 seconds
        resp, rt = KeyGet()
##RESPONSE SECTION ###
        #sets the varriables corr, feedback, and response_time to the variables corr, feedback, and response time to use for feedback and data collection
        corr, feedback, response_time = Response(resp, rt, targ_there)
##FEEDBACK SECTION ###
        #print feedback if got correct or not, in a certain position with a size of 40 pix
        cor_feedback = visual.TextStim(win, text=feedback, pos = (0, 30), height = 40)
        #print response time below cor or not feedback
        back_rt = visual.TextStim(win, text=response_time, pos = (0, -30), height = 40)
        #draw feedback on screen
        cor_feedback.draw()
        #draw rt time on screen
        back_rt.draw()
        #window flip (this clears stimulus and puts feedback on screen instead)
        win.flip()
        #wait for .25 seconds before going to next trial so participant sees feedback
        core.wait(0.5)

###COLLECTING DATA FOR OVERALL PARTICIPANT FEEDBACK
        #if rt is not equal to 999 (which means it is not a miss) do this:
        if rt != 999:
            #append rt to the rt list for later feedback
            rt_list.append(rt)
            #variable miss_rt is given a 0 as there is no miss (because want total misses)
            miss_rt = 0
            #if correct append 1 to the correct list for overall participant feedback
            if corr == 1:
                corr_list.append(1)
            #if incorrect append 0 to the correct list for overall participant feedback
            if corr == 0:
                corr_list.append(0)
        #if rt is equal to 999 (which means it is a miss) do this:
        if rt == 999:
            #append to the amount of miss rt lust to get the total misses
            miss_rt_list.append(1)
            #variable miss_rt given a 1 as there is a miss
            miss_rt = 1
            #append 0 to correct list since if participants could not respond in time it is incorrect
            corr_list.append(0)
        #write to dataFile the condition it is in, if the target was present, the response time, if participant got it correct or not, and if it was incorrect due to a miss or not
        dataFile.write('%i, %i, %.3f, %i, %i\n' %(condition, targ_there, rt, corr, miss_rt))

#close datafile before reporting averages
dataFile.close()

###Reporting Averages##
#take the average response time from the rt_list and round it to 2 decimal places
average_rt = round(np.mean(rt_list), 2)
#turn it into text that reports avg rt
avg_rt_text = 'average rt: ' + str(average_rt) 
#take the average correctdness from the corr_list to 2 decimal places
average_corr = round(np.mean(corr_list), 2)
#turn it into text that reports average correct
avg_corr_text = 'average correct: ' + str(average_corr)
#take the sum of how many were missed in the rt miss list
total_miss = sum(miss_rt_list)
#turn it into text that reports how many trials there was no response
miss_text = 'no response on ' + str(total_miss) + ' trials'
#tells participanst to press SPACE to exit program
leave_text = '''press SPACE to exit'''
#print feedback if got correct or not, in a certain position with a size of 40 pix
cor_avg_back = visual.TextStim(win, text=avg_corr_text, pos = (0, 50), height = 20)
#print response time below cor or not feedback
rt_avg_back = visual.TextStim(win, text=avg_rt_text, pos = (0, -10), height = 20)
#print total no response below
miss_tot_back = visual.TextStim(win, text=miss_text, pos = (0, -35), height = 20)
#tells user what button to press to exit
exit_text = visual.TextStim(win, text=leave_text, pos = (0, -100), height = 20)

#draws all this on the screen
cor_avg_back.draw()
rt_avg_back.draw()
miss_tot_back.draw()
exit_text.draw()

#flips it so the user can see it
win.flip()

#wait until user hits space to close program
keys = event.waitKeys(keyList=['space'])

#quit the program
win.close()
core.quit()

    
