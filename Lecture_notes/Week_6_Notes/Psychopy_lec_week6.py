#import my mouse
from psychopy import visual, event, core, data

#make my window
win = visual.Window([400,400], fullscr = False, units = 'pix')

#make my message
message = visual.TextStim(win, text='hello')

''' To make it so the text follows the mouse position
first make the mouse
then find the mouse position
next update the text position to be at the mouse position '''


#first created an instance of a Clock called timer, which gives current time
timer = core.Clock()

#make a mouse on screen that the use can control
#mouse is an object part of the library event
mouse = event.Mouse(visible=True)

#x position on axis (2D object)
x = 0.0
#y position on axis (2D object)
y = 0.0

#get the current time it is at that moment of starting the task
startTimer = timer.getTime()

#I want an event to last a certain amount of time,
#start at the current time - the start time and keep going until it reaches 2 seconds
while timer.getTime() - startTime < 2.0:

    '''getPos calls the method get position which takes the index of mouse position
    at the x axis (which 0 means x) and assigns it to the x position of the text'''
   # x = mouse.getPos()[0]
    '''getPos calls the method get position which takes the 
    index of the mouse position at the y axis (which 1 means y axis because the positions of the mouse 
    are an updating list of the [x, y] value so x is at posiiton 0 and y is at position 1 in the
    list and assigns it to the y position of the text '''
    # y += mouse.getPos()[1]
    
    pos = mouse.getPos()
    
    message.pos = (pos[0], pos[1])
    
    #make the message position equal the new position of x and y
    message.pos = (x,y)
    #draws message before every flip of teh screen to flip the message at the new position which was modified above
    message.draw()
    #put it on the win
    win.flip()
    
