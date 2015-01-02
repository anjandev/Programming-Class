# SnapChat clone by Anjan Momi

import simplegui

# Load image
IMAGE = simplegui.load_image('http://i.imgur.com/uzgmcO5.jpg')

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

# Handler for user inputted image (Extra feature)
def image_handler(text_input):
    global WIDTH, HEIGHT, IMAGE
    
    IMAGE = simplegui.load_image(text_input)
    WIDTH = IMAGE.get_width()
    HEIGHT = IMAGE.get_height()
    
# Handler for clear button
def clear_click():
    global dots
    
    dots = []
    
# Handler for thickness input
def thickness_handler(text_input):
    global thickness
    
    inp = int(text_input)
    thickness = inp
    
# Handler for color input
def color_handler(text_input):
    global colour
    
    inp = str(text_input)
    colour = inp
    
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
    global dots, IMAGE, WIDTH, HEIGHT
    
    canvas.draw_image(IMAGE, (WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT), (50 * DRAWSCALE, 50 * DRAWSCALE), (100 * DRAWSCALE, 100 * DRAWSCALE))
    for x in range(len(dots)):
        canvas.draw_circle( dots[x][0], dots[x][2], dots[x][2], dots[x][1], dots[x][1])
        
# Create a frame 
FRAMEWIDTHHEIGHT = 100 * DRAWSCALE
TEXT_FIELD_LEN = 200

frame = simplegui.create_frame('SnapChat Game Doodler', FRAMEWIDTHHEIGHT, FRAMEWIDTHHEIGHT)

# Add buttons and inputs to frame
frame.add_button("Clear", clear_click) 
frame.add_input('Colour', color_handler, TEXT_FIELD_LEN) 
frame.add_input('Thickness', thickness_handler, TEXT_FIELD_LEN) 
frame.add_input('Image URL', image_handler, TEXT_FIELD_LEN) 

# Assign callbacks to event handlers
frame.set_draw_handler(draw) 
frame.set_mouseclick_handler(mouse_handler) 
frame.set_mousedrag_handler(mouse_handler) #same for both click and drag in this case 

# Start the frame animation
frame.start()
