# Doodler Game.  

import simplegui
import math


img_link = ('http://i.imgur.com/uzgmcO5.jpg')
image = simplegui.load_image(img_link)

# Wait until image loads
while image.get_width() == 0:
    pass

width = image.get_width()
height = image.get_height()

# Initialize global variables
message = "Let's Doodle!"
mouse_function = "draw"
colour = 'Red'
dots = []
lines = []
thickness = 5

# Helper function to calculate distance using formula
# d = sqrt(x^2+y^2)
def distance(pos1,pos2):
    x = pos1[0] - pos2[0]
    y = pos1[1] - pos2[1]
    
    distance = math.sqrt(x**2+y**2)
    return distance

def drawer_handler():
    global mouse_function
    
    mouse_function = "draw"

# Definition of Dot class
class Dot:
    def __init__(self, position, thickness, colour):
        self.position = position
        self.thickness = thickness
        self.colour = colour
        
    def __str__(self):
        return "Position:" + str(self.position),", Colour:" + self.colour,", Thickness:" + self.thickness,
        
    def get_position(self):
        return self.position
    
    def get_colour(self):
        return self.colour
    
    def get_thickness(self):
        return self.thickness
    
    
    def set_thickness(self, new_thickness):
        self.thickness = new_thickness
    
    def set_colour(self, new_colour):
        self.colour = new_colour

        
# Handler for clear button
def clear_handler():
    global dots
    dots = []
    
# Handler for eraser button
# Changes mouse function to erase rather than draw
def eraser_handler():
    global mouse_function
    
    mouse_function = "erase"
    
# Handler to change thickness    
def thickness_handler(text_input):
    global thickness
    thickness = int(text_input)
    
# Handler to change color    
def color_handler(text_input):
    global colour
    colour = text_input
    
# Mouse click handler
# If mouse function is set to draw, adds a dot at that 
# position using the current thickness and color settings
# If mouse function is set to erase, checks all dots
# to see if the distance from the center is less than the
# radius of the dot and removes the dot if it is.
def mouse_handler(position):
    global mouse_function, dots, colour, lines, thickness 
    
    if mouse_function == "draw":
        dots.append(Dot(position, thickness, colour))
    elif mouse_function == "erase":
        for dot in dots:
            dist = distance(position, dot.get_position())
            print dist
            radius = dot.get_thickness()
            if dist < radius:
                dots.remove(dot)
            
            
# Handler to draw on canvas
def draw(canvas):
    global dots
    canvas.draw_image(image, 
                      (width/2, height/2), 
                      (width, height), 
                      (width/2, height/2), 
                      (width, height))
    for dot in dots:
        canvas.draw_circle(dot.get_position(),
                           dot.get_thickness(), 
                           1, 
                           dot.get_colour(), 
                           dot.get_colour())

#   canvas.draw_circle()
    canvas.draw_text(message, [180,42], 36, "White")
        
# Create a frame 
frame = simplegui.create_frame("Doodler", width, height)

# Create buttons & text inputs
frame.add_button("Clear", clear_handler)
frame.add_button("Erase", eraser_handler)
frame.add_button("Draw", drawer_handler)
frame.add_input('Color', color_handler, 100)
frame.add_input('Thickness (1-20)', thickness_handler, 100)

# Assign callbacks to handler functions
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouse_handler)
frame.set_mousedrag_handler(mouse_handler)

# Start the frame animation
frame.start()
