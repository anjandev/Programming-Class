# Doodler Game.  

import simplegui

# Load image
image = simplegui.load_image('http://i.imgur.com/uzgmcO5.jpg')

# Sets how much to multiply the size of the file by
DRAWSCALE = 6

# Define constants for image width and height
WIDTH = 500
HEIGHT = 543

# Initialize color and thickness variables
colour = 'Blue'
thickness = 3

# Create empty lists to hold dots 
dots = []
newdot = []

# Handler for clear button
def clear_click():
    dots = []
    
# Handler for thickness input
def thickness_handler(text_input):
    global thickness
    
    if len(text_input) > 0:
        thickness = text_input
    
# Handler for color input
def color_handler(text_input):
    global colour
    
    if len(text_input) > 0:
        colour = text_input
    
# Handler for mouse click
def mouse_handler(position):
    global newdot, colour, thickness, dots
    
    newdot.append(position)
    newdot.append(colour)
    newdot.append(thickness)
    dots.append(newdot)
    newdot = []
    
# Handler to draw on canvas
def draw(canvas):
    global dots, thick, col
    
    canvas.draw_image(image, (WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT), (50 * DRAWSCALE, 50 * DRAWSCALE), (100 * DRAWSCALE, 100 * DRAWSCALE))
    
    print dots
    print
    
    for x in range(len(dots)):
		    
# Create a frame 

FRAMEWIDTHHEIGHT = 100 * DRAWSCALE

frame = simplegui.create_frame('Testing', FRAMEWIDTHHEIGHT, FRAMEWIDTHHEIGHT)
frame.add_button("Clear", clear_click) 
color_input = frame.add_input('colour', color_handler, FRAMEWIDTHHEIGHT) 
thickness_input = frame.add_input('thickness', thickness_handler, FRAMEWIDTHHEIGHT) 
frame.set_draw_handler(draw) 
frame.set_mouseclick_handler(mouse_handler) 
frame.set_mousedrag_handler(mouse_handler) #same for both click and drag in this case 

#needs work

# Add buttons and inputs to frame

# Assign callbacks to event handlers

# Start the frame animation
frame.start()
