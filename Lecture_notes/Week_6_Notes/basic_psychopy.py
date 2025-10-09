#Psychopy needs to open a window in which information needs to be passed (tell where you are going to put information- like on another monitor)
#1st open a screen where nothing is there and use python to write some code in the back buffer (code) that is then drawn to the primary surface from the back burfer and then is presented onto a screen
#this is so it can display images at an exact timing by storing it on a back buffer first before you need

#import psychopy library - as well as import specific methods from the library (visual, event, data, and core)
from psychopy import visual, event, core, data


#creating the window to draw on and assigns that window a name, MUST inclide window size it also can include other options
#options like fullscr lets you determine if you want it to be fullscreen and if TRUE you do not need to specify dimensions but will take up whole window
#determines the units you want to draw your stimulus in (can be pixels, degrees, etc.)
win = visual.Window([400,400], fullscr = False, units = 'pix')


#this draws some stimulus to the back buffer and assigns it a label which you want to assign a label to every object you draw so you can change it
#specify the type of stimulus (TextStim - can also specify if other type of stimulus)
#also dictates where you are drawing it to (win - the window we created)
#the text I make is hello (text = 'hello')
message = visual.TextStim(win, text ='hello')

#message2 has not been drawn on the screen (win) so it will not show up when I call I run it, it is still on the backend, it will not appear until drawn which I do after the first flip
#this is a seperate instance of the visual which is a part of the class, with the object TextSTim to modify it
message2 = visual.TextStim(win, text = 'Mimi', pos= (-0.5, -0.5))

#if autoDraw == True it will draw it on every frame
#want to do that when we are changing the location of a stimulus over time, a moving dot
#this makes it so it will stay on teh screen until we tell it to go away
message.autoDraw = True #Automatically draw every frame

#first created an instance of a Clock called timer, which gives current time
timer = core.Clock()

#x position on axis (2D object)
x = 0.0
#y position on axis (2D object)
y = 0.0

#get the current time it is at that moment of starting the task
startTimer = timer.getTime()

#I want an event to last a certain amount of time,
#start at the current time - the start time and keep going until it reaches 2 seconds
while timer.getTime() - startTime < 2.0:
    #every loop add 0.01 to x and y
    x += 0.01
    y += 0.01
    #make the message position equal the new position of x and y
    message.pos = (x,y)
    #draws message before every flip of teh screen to flip the message at the new position which was modified above
    message.draw()
    #put it on the win
    win.flip()
    
#Flip the stimulus to the screen - everything before thsi is happening on the back buffer so this where we make it appear on screen, 
# we prepare a bunch of things before performing a flip so it happens with quick timing
win.flip()

#Says that this will wait 2 seconds before anything else happens, 2 seconds before it reads any other code below it
#may want to put message.text ebfore the core.wait so if it takes 30ms for messgae.txt to happen if I put message.text after core.wait than I will haev to wait 2.30 seconds before the flip, but if I do it before the wait I will only need to wait 2 seconds
core.wait(2.0)

#modify the text property to world
# modifying the variable message and modifying specifically the text (the text property) of message do message.text because this calls the message and specifcies specifically the text
#can also do this with another property such as .font so can do message.font
# the text does not change until we change it so when we flipped it before it would say 'hello' because we have not changed it until after the flip has happened
message.text = 'world' # Change properties of existing stim

#stops drawing the message variable, so will disappear upon new flip
message.autoDraw = False

# starts drawing the message2 variable, so will appear upon new flip
message2.autoDraw = True

#flips the new message2 text - so now the message 'hello' will dissappear and now  'Mimi' will appear on screen instead
win.flip()

#wait 2 more seconds before it executes any other code
core.wait(2.0)

