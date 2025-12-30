### PROBABILITY AND REWARD DIFFERENCES BETWEEN TWO SHAPES ##
## WE MAY NEED TO MAKE THIS HARDER - IT IS WAY TOO EASY - REDUCE ENCODING TIME OR INCREASE DISTANCE BETWEEN STIMULI PERHAPS? ##

#importing packages
from psychopy import visual, core, event, data, gui
from psychopy.tools.colorspacetools import dkl2rgb
import psychopy.tools.coordinatetools
import psychopy.tools.monitorunittools
from psychopy import monitors
from psychopy.tools.monitorunittools import pix2deg
import os
import random
import numpy as np
from PIL import   Image
import math
import csv
import pandas as pd
import colorsys

## GUI AND SUBJECT INFO ##
#This code is suing code from probLetter task#
#Create a dictionary that contains information about subject number
info = {} 
info['Participant'] = '999'          #Subject number - with default set to 999 (practice trials), key is participant and value is 999


#error message for if putting a participant number that is already used - this is to avoid overwriting a exisiting file
errinfo = {}
errinfo['Error:'] = 'Filename already exists. Overwrite existing file ("OK")?' #error message, Error is the key

#Create a dialogue box that takes participant number as input
dlg = gui.DlgFromDict(info) #takes the key participant and value of 999 (which it puts in the box)
if not dlg.OK:              #If 'OK' is not selected on dialogue box (i.e.,user cancels)
    core.quit()             #Quit the experiment (close task window)

#folder for where data is put into
SubjectDataFolder = 'data/'
#Name of each file - which is priorialpha nad participant number for each participant
filename = 'PriorAlpha_' + info['Participant']

#create a datafile in the folder data
SubjectDataFile = os.path.join(SubjectDataFolder + filename + '.csv')

#Sanity check - prevents writing over existing file unless intentional (closes task window if "cancel")
if os.path.exists(SubjectDataFile):
    dlg = gui.DlgFromDict(errinfo) 
    if not dlg.OK:              #if click cancel exits the program
        core.quit()   


###HEADINGS TO INCLUDE FOR EACH DATAFILE ###
#subject = subject number
#trial = trial that we are on
#(cond) condition = 1@100 = 0, 1@50 = 1, 1@67 = 2, 1@80 = 3
#block = when was this condition presented (first, second, third, or fourth)
#pos_c_x = x position of the circle; pos_c_y = y position of the circle
#pos_s_x = x position of the square; pos_s_y = y position of the square
#ProbeSide = which side was the probed item: left = 0 and right = 1
#opt_r = value of red for opisitional in RGB; opt_g = value of green for opisitional in RGB; opt_b = value of blue for opisitional in RGB
#circle_r = value of red for circle in RGB; circle_g = value of green for circle in RGB; circle_b = value of blue for circle in RGB
#square_r = value of red for square in RGB; square_g = value of green for square in RGB; square_b = value of blue for square in RGB
#delay = what was the delay time (fixation time between trials)
#target = Was the circle or square the target (square = 0 and circle = 1)
#resp_r = value of red for what the participant responded with for RGB; resp_g = value of green for what the participant responded with for RGB; resp_b = value of blue for what the participant responded with for RGB;
#points = points earned per trial
#2AFC_acc = did the participant get it correct (incorrect = 0 and correct = 1)
#stim_dis = distance that each stimuli is away from each other
#pos_dis_c = distance circle is away from fixation
# pos_dis_s = distance square is away from fixation
#stimuli_diff = difference in hue (color) between the square and circle - includes counterclockwise direction
#alt_diff = difference in hue (color) between the target shape and 2AFC opisitional color -includes counterclockwise direction

#list of headers
header = [
    "subject", "trial", "cond", "block",
    "pos_c_x", "pos_c_y",
    "pos_s_x", "pos_s_y",
    "probeSide",
    "opt_r", "opt_g", "opt_b",
    "circle_r", "circle_g", "circle_b",
    "square_r", "square_g", "square_b",
    "delay",
    "target",
    "resp_r", "resp_g", "resp_b",
    "points",
    "2AFC_acc",
    "stim_dis", 
    "pos_dis_c", 
    "pos_dis_s",
    "stimuli_diff",
    "alt_diff" 
]

#opening the datafile to write something new in it
with open(SubjectDataFile, "w", newline="") as f:
    writer = csv.writer(f) #creating a writer object to write in csv format
    writer.writerow(header) #writing the headers



## GLOBAL VARIABLES ##

#-- POSTION VARIABLES -- #
FIX_DISTANCE = 4 #distance in degrees that stimuli appear AWAY from fixation
MIN_DIST = 4 #minimum distance stimuli have to be away from each other, we can push the shapes further away from each other to make it more difficult, play with this and see what you think
FIX_SIZE           = 0.2 # The radius of the fixation dot in degrees
TARGET_SIZE        = 2   # The size of the target shape, this value is for both the length and width
FIX_POS = (0, 0) #fixation point location
EDGE_MARGIN = 4 #degrees away from edge

# -- COLOR VARIABLES -- #
COLOR_WHEEL_IMAGE =  "images/square_wheel.png" #color wheel image from images file
COLOR_SEPERATION   = 120  # The Distance between  colours for the two stimuli in degrees on the wheel
ALT_SEP            = 30  # The Distance between alternative choice colours in degrees on the wheel, Play with this and see what works best! :)
MIN_DEG_APART = 10 #minimum degrees the colors are apart from each other

#--- TEXT SPECIFICS --#
TEXT_HEIGHT        = 0.75   # Height of the instructions text
TEXT_WRAPPING      = 30  # Wrapping width of the instructions text

# ---TIMING ---#

ENCODE_TIME = .25 #time when stimuli are on screen - it 250 ms- may need to reduce this -try .10 or even .05 - which i tried and honestly .05 was the best but .10 might be best for an hour or longer exp
ISI = 1.5 #inbetween delay time between stimulus and 2AFC - 1.5 seconds (can't change this)
REWARD_SCREEN = .5 #reward screen time

#targ_type = 0 means the circle is the target
#targ_type = 1 means the square is the target
#starts at none for me to change later
TARG_TYPE = None
TRIAL_NUM = 0

#--- DISPLAY TEXTS --- #
#introduction text
insMsg   = '''You will be presented with two coloured shapes. Try to remember their colours.
            \n\nOne shape will be a circle and the other shape will be a square. 
            \n\nYou will be asked to recall the colour of a target shape by selecting one of two colors with your mouse.
            \n\nYou will be rewarded points for each correct answer
            \n\nOn some blocks, the circle item will have a higher probability of being the target item and be worth more points than the square. 
            \n\nYou will be informed of the probabilty before each block of trials.
            \n\nPlease be as accurate as possible.
            \n\nClick the mouse when you are ready.'''
thankMsg = "Thank you for your participation. Please let the experimenter know you are finished." #thank you message

#BLOCK MESSAGES FOR EACH COND ##
block100Msg = "On this block, there is a 100% chance that the CIRCLE will be the target for each trial. \n\nThe CRICLE will also be worth 10 points for correct answers. \n\nBefore you continue to the next block take a quick break and when you are ready to continue- click the mouse" 
block50Msg = "On this block, all shapes are equally likely to be the target for each trial. \n\nThe CRICLE and SQUARE will be worth 5 points each for correct answers. \n\nBefore you continue to the next block take a quick break and when you are ready to continue- click the mouse" 
block67Msg = "On this block of trials, there is a 67% chance that the CIRCLE will be the target for each trial. \n\nThe CRICLE will also be worth 7 points for correct answers. While the SQUARE will be worth 3 points. \n\nBefore you continue to the next block take a quick break and when you are ready to continue- click the mouse" 
block80Msg = "On this block of trials, there is a 80% chance that the CIRCLE will be the target for each trial. \n\nThe CRICLE will also be worth 8 points for correct answers. While the SQUARE will be worth 2 points.\n\nBefore you continue to the next block take a quick break and when you are ready to continue- click the mouse"

#list of which trig will be the one with the correct color
#0 = left trig has correct color
#1 = right trig has correct color
trig_correct = [0, 1]

#--- LISTS --- #
#--- INITLIZING EMPTY LISTS -- #
accuracy_list = [] #list of users accuracy
TargTypeList = [] #is target the square or circle? (0 for circle and 1 for square)
ConditionList = [] #list of what condtion it was (0 = 1@100, 1 = 1@50, 2= 1@67, 3 = 1@80)
CorrTrigList = [] #list of which trig has the correct color (0 = left trig and 1 = right trig)
PointList = [] #list of points earned for each trial 
ColorList = [] #list of colors picked
Square_posList = [] #ist of square positions for each trial
Circle_posList = [] #list of circle positions for each trial
Square_colorList = [] #lits of square color for each trial
Circle_colorList = [] #list of circle color for each trial
Opt_colorList = [] #list of other 2AFC colors for each trial
between_timeList = [] #list of delay time between trials

#set my monitor as this monitor
mon = monitors.Monitor('MyMonitor')

#window 
# win        = visual.Window(fullscr=True, screen=0, allowGUI=False, allowStencil=False, monitor=MONITOR_NAME, color=[0,0,0], colorSpace='rgb', units='deg')
win = visual.Window(fullscr=True, color=[-.5,-.5,-.5], colorSpace='rgb', units='deg', monitor = mon)

#setting my mouse
mouse = event.Mouse(visible = False, win = win)

##POSITIONING ##

# ---- CREATING A PSEUDOBORDER --- #
#turns the size of current monitor unites from pixels to degrees
#I will be using this to help position my stimuli within screen borders of whatever monitor I am on
win_width_deg = pix2deg(win.size[0],  mon) #0 gives width, total screen width in degrees
win_height_deg = pix2deg(win.size[1], mon) #1 gives height, total screen height screen

#horizontal position bounds of pseudoborder - equation below was figured out with help from CHAT_GPT
x_min = -win_width_deg/2 + EDGE_MARGIN #horizontal bound of the left side of screen (negative), adding the edge margin so stimulus can't get to close to border
x_max = win_width_deg/2 - EDGE_MARGIN #horizontal bound of right side of screen (positive), subtracting the edge margin so it does not appear to close to border

#vertical postion bounds of pseduoborder
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
    return pos_c, pos_s, stim_dis, pos_dis_c, pos_dis_s #return the circle and square position tulpes as well as distance of stim away from each other and away from fixation

##COLOR MADNESS##
#configuring color using Holly Lockharts code- and some help from chat-GPT specifically for making it clearer for me
#this uses the color wheel image and samples from it returning a list of colors (using a margin so it does not hit the edge and sampel from the edge)

#-- SAMPLE FROM COLOR WHEEL and TURN INTO RGB COLORS --- #
def getColors(margin = 50):
    """
    sample colors from the color wheel image in a 360 degree circle
    
    margin = this is cropping to sampel a certain degrees away from edge of image so do not accidentally pick up background color from image that is not the color wheel
    """
    global COLOR_WHEEL_IMAGE
    #this opens the image file and forces it in a RGB format
    im = Image.open(COLOR_WHEEL_IMAGE).convert('RGB')
    #this gets the images width and height and stores it into variabels with a corresponding name
    width, height = im.size
    #this ensures the image is square (width = height) to be used for a circle wheel
    assert width == height
    #computes images center and radius - center_x and center_y are for center of image
    center_x = width / 2 
    center_y = height / 2
    
    #this is for the radius - which is half of the width (minusing the margin to avoid background)
    radius = width/2 - margin
    #initilizes empty output list of colors, which will store colors at each degree in the image
    colors = []
    
    #loops for each degree in the image - samples one color per angle
    #this basically goes in a spiral - larger and larger until it collects all of the colors
    for deg in range(360):
        #converts degrees to radians as the function below requires radians to compute
        angle = math.radians(deg)
        #cos and sin is used to compute x/y positions on a circle
        #cos(angle) gives horizontal position (x) of the specific color
        #since RGB uses integer int ensures it all stays an int so its valid
        #need cx as it is teh horizontal center so you are computing teh dgerees away from horizontal center
        x = int(center_x + math.cos(angle)*radius)
        #this does the same thing for the y coordinate - degrees from y center
        y = int(center_y - math.sin(angle)*radius) #minus for clockwise
        #samoles the pizel color, so stores the pixel color into the r,g,b and RGB is a matrix of red, green, and blue values
        #basically uses the sample position of the image and takes the color of the pixel from there
        r, g, b = im.getpixel((x, y))
    
        #convert 0-255 -> -1 to 1 (psychopy RGB)
        #converts it into psychopy format as psychopy rgb uses [-1, 1] not [0, 255] for each color
        #so what this conversion does is take the color value of the pixel in normal RGB and divides it by 127.5 (the middle value which will represent 0) - 1
        #the minus 1 is to make sure it stays within the bounds of -1 to 1
        colors.append([
        r/ 127.5 -1,
        g / 127.5 -1,
        b / 127.5 -1
        ])
    
    #returns the list of 360 RGB colors to be used in psychopy
    return colors

#initializing the get color definition to create a list of 360 possible colors to use for stimulus
wheel_colors = getColors()

## IN CASE YOU WANT TO LOOK AT THE COLOR FILE - UNCOMMENT THIS ##
#store the colors in a file
#color_file = os.path.join(SubjectDataFolder + 'color_file' + '.csv')
#
#this csv file has the RGB combinations with one column for each RGB combination
#with open(color_file, 'w', newline='') as f:
#    writer = csv.writer(f) 
#    writer.writerow(['r','g','b'])
#    writer.writerows(wheel_colors)
#
#turns csv file into a dataframe
#c_df = pd.read_csv("data/color_file.csv")

#turning rgb to hue to make it so it is a certain degrees apart from each other, which will allow me to compute color distance
def rgb_to_hue(rgb):
    """
    converts list of rgb colors to hsv (hue) to compute color distance in degrees for setColors
    
    rgb = a list of rgb for a specific color on the list
    """
    # Convert from [-1, 1] to [0, 1] to make it compatiable with colorsys
    #the specific equation to turn each color variable into hsv is from chat GPT
    r = (rgb[0] + 1) /2 #transposes first column (red) for compatibility with colorsys
    g = (rgb[1] + 1) / 2 #second column is green
    b = (rgb[2] + 1) / 2 #third column is blue
    h, _, _ = colorsys.rgb_to_hsv(r, g, b) #this converts rgb to hsv - but we only have hue (not saturation and value) so the other two are left blank
    return h * 360 #this puts hue in degrees, in order to make it degrees apart


#-- SETTING COLORS FOR STIMULUS AND ALT --- #
#i have to turn my rgb to hue in order to make it so its a certain degrees away
#set color of stimulis and alt color - I am using teh degrees in seperation from previous experimenst for stim sep (square) and alt sep (TAFC task)
#this sets the colors of stimulus (circle and square) and oppositional 2AFC color for EACH TRIAL
#can go from min - max seperation for either direction (counter and normal clockwise) so up to 110 degrees seperation for alt color for both counter and clcokwise
def setColors(color_list, target_type, stim_min_sep = 15, stim_max_sep = 90, alt_min_sep = 15, alt_max_sep = 110):
    """
    sets colors for circle, square, and opisitional colro for 2AFC task within a range of colors from the color_wheel
    
    color_list = colors that will be using
    target_type = square or circle (0 = circle, and 1 = square)
    stim_min_sep = minimum color seperation between the two stimuli
    stim_max_sep = maximum color seperation between the two stimuli
    alt_min_sep = minimum color seperation between target shape and oppisitional color for 2AFC
    alt_max_sep = maximum color seperation between target shape and oppisitional color for 2AFC
    """
    CircleColor = random.choice(color_list) #samples a one colors from the list of colors
    circle_hue = rgb_to_hue(CircleColor) #turns the the row color into a hue in degrees
    
    diffs = [] #initialize empty list
    #Compute hue difference for stimuli, and checks which colors are close enough to the circle color
    for color in color_list: #loops over all of the colors in the list
        if color != CircleColor: #except the color that is the circle color which it skips
            hue_diff = abs(rgb_to_hue(color) - circle_hue) #computes the hue difference between each color and the circle color
            #this hue_diff part below is from Chat_GPT
            hue_diff = min(hue_diff, 360 - hue_diff) #this handles the other side of the circle, this is the range of distance for each color
            diffs.append((color, hue_diff)) #appends the differences of the circle color and each color to a list
            
    #creates a new df of a set of colors that are within a range of colors away from the circle colors
    square_candidates = [c for c, d in diffs if stim_min_sep <= d <= stim_max_sep] #this filers all of the colors in diffs to include only those within the minimum and maximum seperation between circle colro and square
    SquareColor = random.choice(square_candidates) #sets the square color to one of the colors that are within the low and high values of the circle
    square_hue = rgb_to_hue(SquareColor) #turning the chosen color to a hue
    stimuli_diff = abs(square_hue - circle_hue) #computes the difference of the square hue from circle hue
    stimuli_diff = min(stimuli_diff, 360- stimuli_diff) #coonverting so it takes path of least seperation between colors
    
    #this creates a new list that only includes the colors that are not already picked for the stimulus
    TAFC_candidates = []
    if target_type == 0: #if the target is the CIRCLE
        for color in color_list: #for each color in the color list
            #I know i don't really need this because of the hue diff comparison below but its good insurance anyway
            if color not in [CircleColor, SquareColor]:     #excludes the square color and circle color that was pciked previously for the TAFC color
                hue_diff = abs(rgb_to_hue(color) - circle_hue) #computes the hue difference of each color from circle color - clockwise
                hue_diff = min(hue_diff, 360 - hue_diff) #makes sure it accounts for counterclockwise and makes sure I take the shortest angle for a particular color from the target color (which would eitehr be clockwise = hue diff or counterclockwise  = 360 - hue-diff)
                if alt_min_sep <= hue_diff <= alt_max_sep: #keeps only those within the seperation amount in the new list (hue differences between minimum and maximum- so we keep only a hues within a degree seperation from circle
                    TAFC_candidates.append(color) #appends color to TAFC candidiates list
                    #sets the TAFC other choice color to one from the sample
                    TAFCColor = random.choice(TAFC_candidates)
                    #Hue diff between TAFC color and circle hue - a high number means counterclokcwise
                    alt_diff = abs(rgb_to_hue(TAFCColor) - circle_hue)
                    alt_diff = min(alt_diff, 360 - alt_diff) #converting it so it takes path of least seperation between colors
    elif target_type == 1: #if the target is the SQUARE
        for color in color_list: #for each color in the color list
            if color not in [CircleColor, SquareColor]:     #excludes the square color and circle color that was pciked previously for the TAFC color
                hue_diff = abs(rgb_to_hue(color) - square_hue) #computes the hue difference of each color from square color - clockwise
                hue_diff = min(hue_diff, 360 - hue_diff) #makes sure it accounts for counterclockwise and makes sure I take the shortest angle for a particular color from the target color (which would eitehr be clockwise = hue diff or counterclockwise  = 360 - hue-diff)
                if alt_min_sep <= hue_diff <= alt_max_sep: #keeps only those within the seperation amount  in the new list- keeps only hues within a certain degree away from the square hue
                    TAFC_candidates.append(color) #appends color to TAFC candidates list
                    #sets the TAFC other choice color to one from the sample
                    TAFCColor = random.choice(TAFC_candidates)
                    #Hue diff between TAFC color and square hue - a high number means counterclockwise
                    alt_diff = abs(rgb_to_hue(TAFCColor) - square_hue)
                    alt_diff = min(alt_diff, 360 - alt_diff) #converting it so it takes the path of least seperation between colors
        


    #return the circle color, squarecolor, and alt choice color for 2AFC
    return CircleColor, SquareColor, TAFCColor, stimuli_diff, alt_diff

#fixation cross that will appear for 500-800ms variably
fixation = visual.Circle(win, pos=(0,0), radius=(FIX_SIZE), lineColor='white', fillColor='white', colorSpace = 'rgb')  # create a black fixation point that will be called in before initiating a trial


# ----CONDITIONS --#
# 0 = 1@100
# 1 = 1@50 each
# 2 = 1@67
# 3 = 1@80
conditions = [0, 1, 2, 3]
random.shuffle(conditions) #shuffling the conditions for each participant to avoid practice and fatigue effects

# ---AMOUNT OF TRIALS FOR EACH CONDITION FOR PRACTICE ---#
#for each trials (except 1@100) I am creating a list of 0 and 1's, where 0 equals a circle and 1 equals a square as the target for that trial
#these lists are shuffled for each condition to keep it random
#if participant number is put as 999 - do the practice trials
if info['Participant'] == '999':
    Trial_100         = 5 # Number of reps for cond 1 @ 100% -100 reps
    Trial_50         = [0]*3 + [1]*2 # Number of reps for cond(1@50) - 50 trials for circle and 50 trials for square
    Trial_67         = [0]*7 + [1]*3 #Number of reps for cond 1@67, 100 trials for circle and 50 trials for square
    Trial_80         = [0]*8 + [1]*2 # Number of reps for cond(1 @80), 120 trials for circle and 30 trials for square

# ---AMOUNT OF TRIALS FOR EACH CONDITION FOR REAL ---#
#for each trials (except 1@100) I am creating a list of 0 and 1's, where 0 equals a circle and 1 equals a square as the target for that trial
#these lists are shuffled for each condition to keep it random
else: #else (if not 999) do the normal number of trials
    Trial_100         = 100 # Number of reps for cond 1 @ 100% -100 reps
    Trial_50         = [0]*50 + [1]*50 # Number of reps for cond(1@50) - 50 trials for circle and 50 trials for square
    Trial_67         = [0]*100 + [1]*50 #Number of reps for cond 1@67, 100 trials for circle and 50 trials for square
    Trial_80         = [0]*120 + [1]*30 # Number of reps for cond(1 @80), 120 trials for circle and 30 trials for square

#--- POSITION OF 2AFC TRIANGLES -- #
 #putting position of TAFC triangles
def TAFC_pos(targ_pos):
    """
    puts the 2AFC triangles on position of target shape
    
    targ_pos = position of target shape
    """
    #offset of left triangle from the target
    left_offset = (-0.5, 0)
    #offset of right triangle from the target
    right_offset = (0.5, 0)
    #applying the offsets by taking the x position of the tagrte (which is in the first position of the list)
    #and adding the x value of the left offset by it
    #also doing it to the y value of the targ position and left offset but it doesn't do anything since there is no offset
    left_pos = (targ_pos[0] + left_offset[0], targ_pos[1] + left_offset[1])
    #doing same as above but for the right triangle
    right_pos = (targ_pos[0] + right_offset[0], targ_pos[1] + right_offset[1])
    return left_pos, right_pos #return position for left triangle and position for right triangle




#HEY GLOBAL KEYS DO NOT WORK FOR SOME REASON AND MULTIPLE PEOPLE HAVE BEEN HAVING THIS ISSUE SO YOU WILL SEE ME DO A CONVOLUTED THING- JUST KNOW I TRIED THIS
event.globalKeys.add(key='escape', func=core.quit) 

##MESSAGES FUNCTIONS ##
def show_instructions(message):
    """
    displays message on screen
    
    message = text you want to display
    """
    # ---- SET  INSTRUCTIONS ----#
    fixation.setAutoDraw(False) #remove fixation from screen
    #draw message as text stimulus
    instructions = visual.TextStim(win=win, ori=0, name='text', text=message, font=u'Arial', pos=[0, 0], height=TEXT_HEIGHT, wrapWidth=TEXT_WRAPPING, color=u'white', colorSpace=u'rgb', opacity=1, depth=-1.0)
    instructions.setAutoDraw(True) #draw instructions
    win.flip() #flip to screen
    mouse = event.Mouse(visible = True, win = win) #make mouse visible
    while not mouse.getPressed()[0]: #while mouse is not pressed - keep on instruction screen and wait for it to be pressed
        core.wait(0.01) #this wait is so key presses don't bleed over
        if 'escape' in event.getKeys(): #if escape is pressed it quites the program
            win.close() #program can only quit when taking user input
            core.quit()
    # ---GET TO REST OF EXPERIMENT #
    fixation.setAutoDraw(True) #put fixation back on screen
    instructions.setAutoDraw(False) #turn off instructions
    win.flip() #flip screen
    core.wait(0.25) #to prevent key bleed

## FUNCTION FOR EACH TRIAL##
def run_trial(win, targ_type, wheel_colors, TAFC_corr_trig, circle_points, square_points):
    """
    Runs a single trial
    
        win : screen
        targ_type: 0 = circle and 1 = square
        wheel_colors: list of RGB colors
        TAFC_corr_trig: which 2AFC is correct (0 = left trig, 1= right trig)
        circle_points = amount of points for circle condition
        square_points = amount of points for square condition
        """
    
    #-- importing global variables -- #
    global TARGET_SIZE, ENCODE_TIME, ISI, REWARD_SCREEN
    #--- BEFORE EACH TRIAL --- #
    mouse = event.Mouse(visible = False, win = win) #make mouse invisible
    # wait for 500-800ms variability for each trial
    ## for  delay time between trials do we want to pick specific values for a list? or have it be completely random between a range
    #uniform includes lowest value but excludes highest value which is why I put 0.81 instead of 0.80
    wait_time = random.uniform(0.5, 0.81)
    core.wait(wait_time)
    
    #----- SET COLORS ---#
    #set circle, square, and alt color for this trial using setColors function
    circle_color,square_color, opt_color, stimuli_diff, alt_diff = setColors(color_list =wheel_colors, target_type = targ_type)
    
    # -- SET STIMULI POSITIONS -- #
    #setting positions of the stimuli using rand_pos function
    pos_c, pos_s, stim_dis, pos_dis_c, pos_dis_s = rand_pos() #pos_c is circle position and pos_s is square position
    
    #--- CREATE STIMULI --- #
    
    #make the circle stimuli 
    circle = psychopy.visual.Circle(win, radius= TARGET_SIZE/2, fillColor = circle_color, lineColor = circle_color, colorSpace = 'rgb', pos = pos_c)
    #make the square stimuli
    square = psychopy.visual.Rect(win, width=TARGET_SIZE, height=TARGET_SIZE, fillColor=square_color, colorSpace='rgb', lineColor=square_color, pos= pos_s)
    
    #---- ENCODING PHASE --- #
    circle.draw() #drawing the cirlce on screen
    square.draw() #drawing the square on screen
    win.flip() #flipping the screen so the user can see
    
    # --- ISI ---- #
    core.wait(ENCODE_TIME) #wait for .250 seconds before putting anything else
    win.flip() #clearing screen except fixation
    core.wait(ISI) #flipping the screen to show only fixation
    
    #--- 2AFC setup -- #
    if targ_type == 0: #circle is the target
        left_pos, right_pos = TAFC_pos(pos_c) #applying the TAFC positions based on target position (in this case circle)
        target_color = circle_color #setting correct color to circle color for trial
        #setting the unprobed shape (square) as white to show up during 2AFC task
        unprobed_shape = psychopy.visual.Rect(win, width=TARGET_SIZE, height=TARGET_SIZE, fillColor="white", colorSpace='rgb', lineColor="white", pos= pos_s)
    else: #square is the target
        left_pos, right_pos = TAFC_pos(pos_s) #appllying  the TAFC positions based on target shape position (in this case square)
        target_color = square_color #setting correct color to square color for trial
        #setting the unprobed shape (circle) as white to show up during 2AFC
        unprobed_shape = psychopy.visual.Circle(win, radius= TARGET_SIZE/2, fillColor = "white", lineColor = "white", colorSpace = 'rgb', pos = pos_c)
    if TAFC_corr_trig == 0: #if left trig chosen to have the correct color is the left trig
        #left triangle for TAFC task - with color being equal to target shape color
        left_trig  = visual.ShapeStim(win, vertices=((0,TARGET_SIZE), (-TARGET_SIZE,0), (0,-TARGET_SIZE)), pos= left_pos, fillColor= target_color, fillColorSpace='rgb', lineColor=target_color, lineColorSpace='rgb')
        #right triangle for TAFC task - with color being equal to opisitional color
        right_trig = visual.ShapeStim(win, vertices=((0,TARGET_SIZE), (TARGET_SIZE,0), (0,-TARGET_SIZE)), pos= right_pos, fillColor= opt_color, fillColorSpace='rgb', lineColor=opt_color, lineColorSpace='rgb')
    else: #if right trig chosen to have the correct color is the right trig
        #left triangle for TAFC task - with color being equal to opisitional color
        left_trig  = visual.ShapeStim(win, vertices=((0,TARGET_SIZE), (-TARGET_SIZE,0), (0,-TARGET_SIZE)), pos= left_pos, fillColor= opt_color, fillColorSpace='rgb', lineColor=opt_color, lineColorSpace='rgb')
        #right triangle for TAFC task- with color being equal to target shape color
        right_trig = visual.ShapeStim(win, vertices=((0,TARGET_SIZE), (TARGET_SIZE,0), (0,-TARGET_SIZE)), pos= right_pos, fillColor= target_color, fillColorSpace='rgb', lineColor=target_color, lineColorSpace='rgb')
        
    #--- DRAW 2AFC --- #
    #drawing the two triangles on screen
    left_trig.draw()
    right_trig.draw()
    unprobed_shape.draw() #drawing unprobed shape
    #flipping the window
    win.flip()
    
    #---RESPONSE COLLECTION --- #
    #accuracy = was participant correct with 1 = correct and 0 = incorrect
    #reward = points earned on each trial (which could be 0 if incorrect)
    #color picked = what color did the participant pick for this trial
    accuracy, reward, colorPicked = None, None, None #setting accuracy, reward, and colorpicked to None for each trial until something is picked
    mouse = event.Mouse(visible=True, win = win) #makes mouse visible
    while True: #while the mouse is not clicked

        #-- CIRCLE IS THE TARGET -- #
        if TAFC_corr_trig == 0 and targ_type == 0: #if left trig is the one chosen to have the correct color and circle was the target
            if mouse.isPressedIn(left_trig, buttons = [0]): #if the user clicks over the left triangle
                accuracy = 1 #correct
                reward = circle_points #point reward
                colorPicked = target_color #set color picked to target color
                break #exit loop
            elif mouse.isPressedIn(right_trig, buttons=[0]): #if the user left clicks over the right (wrong) triangle
                accuracy = 0 #incorrect
                reward = 0 #point reward
                colorPicked = opt_color #set color picked to opt_color
                break #exit loop
            elif 'escape' in event.getKeys(): #if escape is pressed it quites the program
                win.close() #program can only quit when taking user input
                core.quit()
        elif TAFC_corr_trig == 1 and targ_type == 0: #if right trig is the one chosen to have the correct color and circle was the target
            if mouse.isPressedIn(right_trig, buttons=[0]): #if the user left clicks over the right triangle
                accuracy = 1 #correct
                reward = circle_points #point reward
                colorPicked = target_color #set color picked to target color
                break #exit loop
            elif mouse.isPressedIn(left_trig, buttons=[0]): #if the user left clicks over the left (wrong) triangle
                accuracy = 0 #incorrect
                reward = 0 #point reward
                colorPicked = opt_color #set color picked to opt_color
                break #exit loop
            elif 'escape' in event.getKeys(): #if escape is pressed it quites the program
                win.close() #program can only quit when taking user input
                core.quit()
        
        #--- SQUARE IS THE TARGET --- #
        elif TAFC_corr_trig == 0 and targ_type == 1: #if left trig is the one chosen to have the correct color and square was the target
            if mouse.isPressedIn(left_trig, buttons = [0]): #if the user clicks over the left triangle
                accuracy = 1 #correct
                reward = square_points #point reward
                colorPicked = target_color #set color picked to target color
                break #exit loop
            elif mouse.isPressedIn(right_trig, buttons=[0]): #if the user left clicks over the right (wrong) triangle
                accuracy = 0 #incorrect
                reward = 0 #point reward
                colorPicked = opt_color #set color picked to opt_color
                break #exit loop
            elif 'escape' in event.getKeys(): #if escape is pressed it quites the program
                win.close() #program can only quit when taking user input
                core.quit()
        elif TAFC_corr_trig == 1 and targ_type == 1: #if right trig is the one chosen to have the correct color and square was the target
            if mouse.isPressedIn(right_trig, buttons=[0]): #if the user left clicks over the right triangle
                accuracy = 1 #correct
                reward = square_points #point reward
                colorPicked = target_color #set color picked to target color
                break #exit loop
            elif mouse.isPressedIn(left_trig, buttons=[0]): #if the user left clicks over the left (wrong) triangle
                accuracy = 0 #incorrect
                reward = 0 #point reward
                colorPicked = opt_color #set color picked to opt_color
                break #exit loop
            elif 'escape' in event.getKeys(): #if escape is pressed it quites the program
                win.close() #program can only quit when taking user input
                core.quit()
        
        core.wait(0.01) #to avoid overloading
    
    # --- REWARD SCREEN -- #
    reward_text = '+' + str(reward) #reward text that is what reward participant got
    if targ_type == 0 and accuracy == 1: #if circle was the target and user is correct
        targ_shape = psychopy.visual.Circle(win, radius= TARGET_SIZE/2, fillColor = "white", lineColor = "white", colorSpace = 'rgb', pos = pos_c) #drawing the reward shape on screen
        point_text = visual.TextStim(win, reward_text, colorSpace = 'rgb255',pos = pos_c, height = TARGET_SIZE/2) #point text is circle points
    elif targ_type == 0 and accuracy == 0: #if circle was the target and user is incorrect
        targ_shape = psychopy.visual.Circle(win, radius= TARGET_SIZE/2, fillColor = "white", lineColor = "white", colorSpace = 'rgb', pos = pos_c) #drawing the reward shape on screen
        point_text = visual.TextStim(win, reward_text, colorSpace = 'rgb255',pos = pos_c, height = TARGET_SIZE/2) #point text is 0
    elif targ_type == 1 and accuracy == 1: #if square was the target and user is correct
        targ_shape = psychopy.visual.Rect(win, width=TARGET_SIZE, height=TARGET_SIZE, fillColor="white", colorSpace='rgb', lineColor="white", pos= pos_s)
        point_text = visual.TextStim(win, reward_text,  colorSpace = 'rgb255',pos = pos_s, height = TARGET_SIZE/2) #point text is square points
    else: #if square was the target and user is incorrect
        targ_shape = psychopy.visual.Rect(win, width=TARGET_SIZE, height=TARGET_SIZE, fillColor="white", colorSpace='rgb', lineColor="white", pos= pos_s)
        point_text = visual.TextStim(win, reward_text, colorSpace = 'rgb255',pos = pos_s, height = TARGET_SIZE/2) #point text is 0
    
    targ_shape.draw() #draw shape on screen
    point_text.draw() #draw points on shape
    win.flip() #flip reward to screen
    core.wait(REWARD_SCREEN) #wait .5 seconds for user to see reward
    win.flip() #clear window
    
    return accuracy, reward, colorPicked, pos_c, pos_s, circle_color, square_color, opt_color, wait_time, stim_dis, pos_dis_c, pos_dis_s, stimuli_diff, alt_diff #returning variables to store in participant file

## INTIATE PRACTICE EXPERIMENT ##

#INSTRUCTIONS - START EXPERIMENT #
show_instructions(insMsg) #show instructions

for each_cond in conditions: # do this for every condition
    ## 1@100 CONDITION ##
    if each_cond == 0: #for the 1@100 condition
        TARG_TYPE = 0 #CIRCLE is always the target
        show_instructions(block100Msg) #show block instructions
        for trial in range(Trial_100): #for each trial
            TRIAL_NUM += 1 #add 1 to trial number for each trial - to keep track of what trial we are on
            TAFC_corr_trig = random.choice(trig_correct) #on each trials randomly choose which trig will contain the correct color
            accuracy, reward, colorPicked, pos_c, pos_s, circle_color, square_color, opt_color, wait_time, stim_dis, pos_dis_c, pos_dis_s, stimuli_diff, alt_diff = run_trial(win, TARG_TYPE, wheel_colors, TAFC_corr_trig, 10, 0)
            with open(SubjectDataFile, "a", newline="") as f:
                writer = csv.writer(f) #creates something that will write the values as csv
                writer.writerow([
                    info['Participant'], #subject ID
                    TRIAL_NUM, #current trial number
                    each_cond, #condition code (0 = 1@100, 1 = 1@50, 2 = 1@67, and 3 = 1@80)
                    conditions[each_cond], #what block we are on - so we can see the order of which the conditiosn appeared
                    round(pos_c[0], 4), #x-value of circle position to 4 decimal places
                    round(pos_c[1], 4), #y value of circle position to 4 decimal places
                    round(pos_s[0], 4), #x-value of square position to 4 decimal places
                    round(pos_s[1], 4), #y-value of square position to 4 decimal places
                    TAFC_corr_trig, #which side has the correct color from target shape (0 = left, 1= right)
                    *(round(x, 4) for x in opt_color), #unpacking RGB of opt_color, red- green- blue gets its own column, to 4 decimal places
                    *(round(x,4) for x in circle_color),  #unpacking RGB of circle_color, red- green- blue gets its own column, to 4 decimal places
                    *(round(x, 4) for x in square_color), #unpacking RGB of square_color, red- green- blue gets its own column, to 4 decimal places
                    round(wait_time, 4), #delay before trial to 4 decimal places
                    TARG_TYPE, #target shape for the trial (0 = circle, 1 = square)
                    *(round(x, 4) for x in colorPicked), #unpack RGB of participants chosen color, red- green- blue gets its own column, to 4 decimal places
                    reward, #points earned for trial
                    accuracy, #2AFC accuracy (1 = correct, 0 = incorrect)
                    round(stim_dis, 4), #distance that each stimuli is away from each other
                    round(pos_dis_c, 4), #distance circle is away from fixation
                    round(pos_dis_s, 4), #distance square is away from fixation
                    round(stimuli_diff, 4),#difference in hue (color) between the square and circle
                    round(alt_diff, 4) #difference in hue (color) between the target shape and 2AFC opisitional color
                ]) #at end the file is closed 
    ## 1@50 CONDITION ##
    elif each_cond == 1: #1@50 condition
        show_instructions(block50Msg) #show block instructions
        random.shuffle(Trial_50) #shuffle the list of 0s and 1s
        for trial in Trial_50: # do this for each trial
            TRIAL_NUM += 1 #add 1 to trial number
            TAFC_corr_trig = random.choice(trig_correct) #for each trial randomly chooses from trig list for which trig will have the correct color
            if trial == 0: #for trials where CIRCLE is the target
                TARG_TYPE = 0 #CIRCLE is  the target
                accuracy, reward, colorPicked, pos_c, pos_s, circle_color, square_color, opt_color, wait_time, stim_dis, pos_dis_c, pos_dis_s, stimuli_diff, alt_diff = run_trial(win, TARG_TYPE, wheel_colors, TAFC_corr_trig, 5, 5)
            if trial == 1: #for trials where SQUARE is the target
                TARG_TYPE = 1 #SQUARE is  the target
                accuracy, reward, colorPicked, pos_c, pos_s, circle_color, square_color, opt_color, wait_time, stim_dis, pos_dis_c, pos_dis_s, stimuli_diff, alt_diff = run_trial(win, TARG_TYPE, wheel_colors, TAFC_corr_trig, 5, 5)
            with open(SubjectDataFile, "a", newline="") as f:
                writer = csv.writer(f) #creates something that will write the values as csv
                writer.writerow([
                    info['Participant'], #subject ID
                    TRIAL_NUM, #current trial number
                    each_cond, #condition code (0 = 1@100, 1 = 1@50, 2 = 1@67, and 3 = 1@80)
                    conditions[each_cond], #what block we are on - so we can see the order of which the conditiosn appeared
                    round(pos_c[0], 4), #x-value of circle position to 4 decimal places
                    round(pos_c[1], 4), #y value of circle position to 4 decimal places
                    round(pos_s[0], 4), #x-value of square position to 4 decimal places
                    round(pos_s[1], 4), #y-value of square position to 4 decimal places
                    TAFC_corr_trig, #which side has the correct color from target shape (0 = left, 1= right)
                    *(round(x, 4) for x in opt_color), #unpacking RGB of opt_color, red- green- blue gets its own column, to 4 decimal places
                    *(round(x,4) for x in circle_color),  #unpacking RGB of circle_color, red- green- blue gets its own column, to 4 decimal places
                    *(round(x, 4) for x in square_color), #unpacking RGB of square_color, red- green- blue gets its own column, to 4 decimal places
                    round(wait_time, 4), #delay before trial to 4 decimal places
                    TARG_TYPE, #target shape for the trial (0 = circle, 1 = square)
                    *(round(x, 4) for x in colorPicked), #unpack RGB of participants chosen color, red- green- blue gets its own column, to 4 decimal places
                    reward, #points earned for trial
                    accuracy, #2AFC accuracy (1 = correct, 0 = incorrect)
                    round(stim_dis, 4), #distance that each stimuli is away from each other
                    round(pos_dis_c, 4), #distance circle is away from fixation
                    round(pos_dis_s, 4), #distance square is away from fixation
                    round(stimuli_diff, 4),#difference in hue (color) between the square and circle
                    round(alt_diff, 4) #difference in hue (color) between the target shape and 2AFC opisitional color
                ]) #at end the file is closed 
    ## 1@67 CONDITION ##
    elif each_cond == 2: #1@67 condition
        show_instructions(block67Msg) #show clock instructions
        random.shuffle(Trial_67) #shuffle the list of 0s and 1s
        for trial in Trial_67: # do this for each trial
            TRIAL_NUM += 1 #add 1 to trial number
            TAFC_corr_trig = random.choice(trig_correct) #for each trial randomly chooses from trig list for which trig will have the correct color
            if trial == 0: #for trials where circle is the target
                TARG_TYPE = 0 #circle is  the target
                accuracy, reward, colorPicked, pos_c, pos_s, circle_color, square_color, opt_color, wait_time, stim_dis, pos_dis_c, pos_dis_s, stimuli_diff, alt_diff = run_trial(win, TARG_TYPE, wheel_colors, TAFC_corr_trig, 7, 3) #run trial where reward for circle is 7 points and reward for square is 3
            if trial == 1: #for trials where the square is the target
                TARG_TYPE = 1 #SQUARE is  the target
                accuracy, reward, colorPicked, pos_c, pos_s, circle_color, square_color, opt_color, wait_time, stim_dis, pos_dis_c, pos_dis_s, stimuli_diff, alt_diff = run_trial(win, TARG_TYPE, wheel_colors, TAFC_corr_trig, 7, 3) #run trial where reward for circle is 7 points and reward for square is 3
            with open(SubjectDataFile, "a", newline="") as f:
                writer = csv.writer(f) #creates something that will write the values as csv
                writer.writerow([
                    info['Participant'], #subject ID
                    TRIAL_NUM, #current trial number
                    each_cond, #condition code (0 = 1@100, 1 = 1@50, 2 = 1@67, and 3 = 1@80)
                    conditions[each_cond], #what block we are on - so we can see the order of which the conditiosn appeared
                    round(pos_c[0], 4), #x-value of circle position to 4 decimal places
                    round(pos_c[1], 4), #y value of circle position to 4 decimal places
                    round(pos_s[0], 4), #x-value of square position to 4 decimal places
                    round(pos_s[1], 4), #y-value of square position to 4 decimal places
                    TAFC_corr_trig, #which side has the correct color from target shape (0 = left, 1= right)
                    *(round(x, 4) for x in opt_color), #unpacking RGB of opt_color, red- green- blue gets its own column, to 4 decimal places
                    *(round(x,4) for x in circle_color),  #unpacking RGB of circle_color, red- green- blue gets its own column, to 4 decimal places
                    *(round(x, 4) for x in square_color), #unpacking RGB of square_color, red- green- blue gets its own column, to 4 decimal places
                    round(wait_time, 4), #delay before trial to 4 decimal places
                    TARG_TYPE, #target shape for the trial (0 = circle, 1 = square)
                    *(round(x, 4) for x in colorPicked), #unpack RGB of participants chosen color, red- green- blue gets its own column, to 4 decimal places
                    reward, #points earned for trial
                    accuracy, #2AFC accuracy (1 = correct, 0 = incorrect)
                    round(stim_dis, 4), #distance that each stimuli is away from each other
                    round(pos_dis_c, 4), #distance circle is away from fixation
                    round(pos_dis_s, 4), #distance square is away from fixation
                    round(stimuli_diff, 4),#difference in hue (color) between the square and circle
                    round(alt_diff, 4) #difference in hue (color) between the target shape and 2AFC opisitional color
                ]) #at end the file is closed 
   ## 1@80 CONDITION ##
    elif each_cond == 3: #1@80 condition
        show_instructions(block80Msg) #shows condition instructions
        random.shuffle(Trial_80) #shuffle the list of 0s and 1s
        for trial in Trial_80: # do this for each trial
            TRIAL_NUM += 1 #add 1 to trial number
            TAFC_corr_trig = random.choice(trig_correct) #for each trial randomly chooses from trig list for which trig will have the correct color
            if trial == 0: #for trials where circle is the target
                TARG_TYPE = 0 #circle is  the target
                accuracy, reward, colorPicked, pos_c, pos_s, circle_color, square_color, opt_color, wait_time, stim_dis, pos_dis_c, pos_dis_s, stimuli_diff, alt_diff = run_trial(win, TARG_TYPE, wheel_colors, TAFC_corr_trig, 8, 2) #run trials where reward for circle is 8 points and reward for square is 2
            if trial == 1: #for trials where the square is the target
                TARG_TYPE = 1 #square is  the target
                accuracy, reward, colorPicked, pos_c, pos_s, circle_color, square_color, opt_color, wait_time, stim_dis, pos_dis_c, pos_dis_s, stimuli_diff, alt_diff = run_trial(win, TARG_TYPE, wheel_colors, TAFC_corr_trig, 8, 2) #run trials where reward for circle is 8 points and reward for sqaure is 2
            #open the data file in append mode so it does not overwrite exisiting data, and newline makes sure that it is wirtten without extra blank lines
            with open(SubjectDataFile, "a", newline="") as f:
                writer = csv.writer(f) #creates something that will write the values as csv
                writer.writerow([
                    info['Participant'], #subject ID
                    TRIAL_NUM, #current trial number
                    each_cond, #condition code (0 = 1@100, 1 = 1@50, 2 = 1@67, and 3 = 1@80)
                    conditions[each_cond], #what block we are on - so we can see the order of which the conditiosn appeared
                    round(pos_c[0], 4), #x-value of circle position to 4 decimal places
                    round(pos_c[1], 4), #y value of circle position to 4 decimal places
                    round(pos_s[0], 4), #x-value of square position to 4 decimal places
                    round(pos_s[1], 4), #y-value of square position to 4 decimal places
                    TAFC_corr_trig, #which side has the correct color from target shape (0 = left, 1= right)
                    *(round(x, 4) for x in opt_color), #unpacking RGB of opt_color, red- green- blue gets its own column, to 4 decimal places
                    *(round(x,4) for x in circle_color),  #unpacking RGB of circle_color, red- green- blue gets its own column, to 4 decimal places
                    *(round(x, 4) for x in square_color), #unpacking RGB of square_color, red- green- blue gets its own column, to 4 decimal places
                    round(wait_time, 4), #delay before trial to 4 decimal places
                    TARG_TYPE, #target shape for the trial (0 = circle, 1 = square)
                    *(round(x, 4) for x in colorPicked), #unpack RGB of participants chosen color, red- green- blue gets its own column, to 4 decimal places
                    reward, #points earned for trial
                    accuracy, #2AFC accuracy (1 = correct, 0 = incorrect)
                    round(stim_dis, 4), #distance that each stimuli is away from each other
                    round(pos_dis_c, 4), #distance circle is away from fixation
                    round(pos_dis_s, 4), #distance square is away from fixation
                    round(stimuli_diff, 4),#difference in hue (color) between the square and circle
                    round(alt_diff, 4) #difference in hue (color) between the target shape and 2AFC opisitional color
                ]) #at end the file is closed 


show_instructions(thankMsg) #show thank you message at end of experiment


#quit the program, close window first
win.close()
core.quit()