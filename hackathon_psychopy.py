#import psychopy tools
from psychopy import visual, event, core, data, gui

#creatng our window to draw on
#fullscreen is false so it wont take up the whole screen
win = visual.Window([400,400], fullscr = False, units = 'pix')

#initalise fixation - setting size to 5 pixels tall (we specified our units are pixels in win)
# creates a variable called fixation which contains a stimulus that we made (a cross, which is the plus sign on the keyboard so that is why it is a text stim)
fixation = visual.TextStim(win, text = '+', height =20, color = 'white')

#visual stimuli of GO to tell participant to go to press space
message = visual.TextStim(win, text = 'GO!')

#end text to tell participant to press escape to exit
message3 = visual.TextStim(win, text= 'Press ESCAPE to exit' , pos = (0, -100), height = 20)

#drawing fixation of screen
fixation.draw()

#showing what was drawn on back screen to front screen
win.flip()

#waiting 1 second before showing stimuli
core.wait(1)

#drawing the Go message
message.draw()

#flipping the message on screen
win.flip()
#when the message of 'Go! is on screen do a start time right after it appears on screen to be able to (when the trial starts)
StartTime = core.getTime()

#assigning keys that when participant presses does two things
keys = event.waitKeys(keyList=['space', 'escape'])

#if keys are pressed
if keys:
    #assign variable key to the first key pressed
    key = keys[0]
    #if the key pressed is space
    if key == 'space':
        #record the response time by getting total time of experiment - when the trial started to get the response time
        rt = core.getTime() - StartTime
        #to convert the rt into ms times it by 1000
        ms_rt = rt * 1000
        #message2 is the reaction time in ms rounded to 2 decimal points
        message2 = visual.TextStim(win, text = str(round(ms_rt, 2)) + 'ms', pos = (0, 50), height = 20)
        #draw message 2 (reaction time) on screen
        message2.draw()
        #draw the exit message on screen (press escape to exit
        message3.draw()
        #flip it so user can see results on screen
        win.flip()
        #wait for the escape key to be pressed..
        keys = event.waitKeys(keyList = ['escape'])
        #when the escape key is pressed, exit the program
        core.quit()
    #if during the trial the participant presses escape quit the whole program before results
    if key == 'escape':
        core.quit()