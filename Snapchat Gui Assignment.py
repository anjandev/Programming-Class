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
    global thickness, newdot, dots
    
    newdot.append(thickness)
    
# Handler for color input
def color_handler(text_input):
    global colour, newdot, dots
    
    text_input = colour
    
    newdot.append(colour)
    
# Handler for mouse click
def mouse_handler(position):
    global newdot, colour, thickness, dots
    
    newdot.append(position)
    dots.append(newdot)
    newdot = []
    
# Handler to draw on canvas
def draw(canvas):
    global dots, thick, col
    
    canvas.draw_image(image, (WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT), (50 * DRAWSCALE, 50 * DRAWSCALE), (100 * DRAWSCALE, 100 * DRAWSCALE))
    
    print dots
    print
    
    #for x in range(len(dots)):
        #canvas.draw_circle(dots[0], dots[1], dots[1], dots[2], dots[2])
    
# Create a frame 

FRAMEWIDTHHEIGHT = 100 * DRAWSCALE

frame = simplegui.create_frame('Testing', FRAMEWIDTHHEIGHT, FRAMEWIDTHHEIGHT)
frame.add_button("Clear", clear_click) 
frame.set_draw_handler(draw) 
frame.set_mouseclick_handler(mouse_handler) 
frame.set_mousedrag_handler(mouse_handler) #same for both click and drag in this case 

#needs work
color_input = frame.add_input(colour, color_handler, FRAMEWIDTHHEIGHT) 
thickness_input = frame.add_input(thickness, thickness_handler, FRAMEWIDTHHEIGHT) 

# Add buttons and inputs to frame

# Assign callbacks to event handlers

# Start the frame animation
frame.start()
