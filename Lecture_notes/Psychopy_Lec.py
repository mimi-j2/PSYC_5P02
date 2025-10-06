##### POSNER CUEING TASK #####

import random
#import psychopy library - as well as import specific methods from the library (visual, event, data, and core)
from psychopy import visual, event, core, data


#creating the window to draw on and assigns that window a name, MUST inclide window size it also can include other options
#options like fullscr lets you determine if you want it to be fullscreen and if TRUE you do not need to specify dimensions but will take up whole window
#determines the units you want to draw your stimulus in (can be pixels, degrees, etc.)
win = visual.Window([400,400], fullscr = False, units = 'pix')

#initalise some stimuli - setting size to 5 pixels tall (we specified our units are pixels in win)
# creates a variable called fixation which contains a stimulus that we made (a circle from visual.Circle)
fixation = visual.Circle(win, size =5,
    lineColor = 'white', fillColor = 'lightGrey')

#creating a clock to record response time
respClock = core.Clock()

#Global event key (with modifier) to quit the experiment, 
#this says if someone preses q and the control key then what that function is is to quit the experiment
event.globalKeys.add(key='q', modifiers=['ctrl'], func=core.quit)

#can do event.Mouse to track what the mouse is doing

#creates a variable that opens a NEW file
#fileName = expInfo['observer'] + expInfo['dateStr']
#fileID = open(Posner_cue+'.csv', 'w')
#dataFile.write('targetSide, oriIncrement, correct\n')
#w = write, x = open, a = append

#second stimulus
probe = visual.GratingStim(win, size = 80, # 'size' is 3XSD for gauss
    pos = [50, 10], #for position everything is measured relative to the middle of the screen
    tex = None, mask = 'gauss',
    color = 'green')
#mask stimulus that covers part of it and only allows part of something to pass through like an image on a face on an oval
#for images go to image = 'path of image'

#creating a third stimulus
cue = visual.ShapeStim(win, 
    vertices = [[-30, -20], [-30,20], [30,0]],
    lineColor = 'red', fillColor = 'salmon')
    
info = {} #creating a dictonary
info['fixTime'] = 0.5 #creating a key in the dictonary(info) that has a value of how long the fixation is on screen in seconds (500 ms)
info['cueTime'] = 0.5 #second key in dictonary(info) that has a value of how long the cue is on screen in seconds (200 ms)
info['probeTime'] = 0.5 #third key in dictonary(info) that has a value of how long the probe is on screen in seconds (200 ms)



#another way to do random stuff
#side = [1, 2]
#orient = [1, 2]

#run 5 trials
for trial in range(5):
    fixation.autoDraw = True #Automatically draws the fixation every frame, will stay on screen until we tell it to turn it off, basically keeps it on screen until we tell it to turn off
    win.flip()
    
    chance = random.randint(1, 4)
    print("trial " + str(trial) + " chance " + str(chance))
    
    #another way to do random stuff
#    random.shuffle(side)
#    print('orient' + str(side[0]))
#    random.shuffle(orient)
#    print('orient' + str(orient[0]))
    
    #probe on left side with left facing cue (valid left cue)
    if chance == 1:
        cue.draw() #draws the cue
        win.flip() #puts it on screen
        core.wait(info['cueTime']) #keep it on screen for 0.2 as per the cuetime key in dictonary info
        
        probe.pos = (-50, 10)
        probe.draw() #draw the probe
        win.flip() #put it on screen
        core.wait(info['probeTime']) #keep it on screen for 0.2 ms as per the probetime key in dictonary info
        
        respClock.reset() #rest my clock so it will start once participants sees the probe
        
        win.flip() #clear screen
        
        #look for keyboard response
        keys = event.waitKeys(keyList = ['left', 'right', 'escape']) #these are the keys that are accepted as a response 
        resp = keys[0] #takes the first response of the keys
        rt = respClock.getTime() #set rt (reaction time) to when participant made a response, records the time
        
        #check for response accuracy
        if resp == 'left' and chance == 1: #if the participants response was left and the type of trial was a chance trial 1 than get correct
            corr = 1 #1 = correct
        else:
            corr = 0 # 0 = wrong

    #probe on opposite side (right) with invalid cue (left)
    elif chance == 2:
        cue.draw() #draws the cue
        win.flip() #puts it on screen
        core.wait(info['cueTime']) #keep it on screen for 0.2 as per the cuetime key in dictonary info
        
        probe.draw() #draw the probe
        win.flip() #put it on screen
        core.wait(info['probeTime']) #keep it on screen for 0.2 ms as per the probetime key in dictonary info
    
    #probe on right side with right cue (valid right cue)
    elif chance == 3:
        
        cue.ori = 180
        cue.draw() #draws the cue
        win.flip() #puts it on screen
        core.wait(info['cueTime']) #keep it on screen for 0.2 as per the cuetime key in dictonary info
        
        probe.draw() #draw the probe
        win.flip() #put it on screen
        core.wait(info['probeTime']) #keep it on screen for 0.2 ms as per the probetime key in dictonary info
    
    elif chance == 4:
        cue.ori = 180
        cue.draw() #draws the cue
        win.flip() #puts it on screen
        core.wait(info['cueTime']) #keep it on screen for 0.2 as per the cuetime key in dictonary info
        
        probe.pos = (-50, 10)
        probe.draw() #draw the probe
        win.flip() #put it on screen
        core.wait(info['probeTime']) #keep it on screen for 0.2 ms as per the probetime key in dictonary info
    
    #writes result of this trial to a file
#    fileID.write('%i, %3f, %i\n', %(targetSide, thisIncrement, thisResp))
    #%i = integer, %f = float with 3 decimal points, and %i = integer)

#at end of experiment close the file
fileID.close()




    