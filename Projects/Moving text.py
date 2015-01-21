# A program that draws a background image on the canvas with a banner 
# message over it that streams across the bottom.  

import simplegui
import random

FRAME_WIDTH = 700
FRAME_HEIGHT = 700

class Banner:
    def __init__(self, message, pos, colour, size, vel, acc):
       self.message = message
       self.pos = pos
       self.colour = colour
       self.size = size
       self.vel = vel
       self.acc = acc
        
    def draw(self,canvas):
        canvas.draw_text(self.message, self.pos, self.size, self.colour)
        
    def update(self):
        # x += v
        for i in range(2):
            self.pos[i] += self.vel[i]
        
        if frame.get_canvas_textwidth(self.message, self.size) + self.pos[0] >= FRAME_WIDTH:
            self.vel[0] = self.vel[0] * -1
        
        if self.pos[0] <= 0:
            self.vel[0] = self.vel[0] * -1
            
        if self.pos[1] - 10 <= 0:
            self.vel[1] = self.vel[1] * -1
            
        if self.pos[1] >= FRAME_HEIGHT:
            self.vel[1] = self.vel[1] * -1
        
    def set_text(self, new_message):
        if len(new_message) > 0:
            self.message = new_message
            
    def set_colour(self, new_colour):
        self.colour = new_colour
        
    def get_size(self):
        return self.size
    
    def get_message(self):
        return self.message   
    
    def get_pos(self):
        return self.pos
            
# Handler for mouse click
def message_handler(text_input):
    pass

def click_message_change():
    banner.set_text(inp.get_text())  

# Handler to draw on canvas
def draw(canvas):
    banner.draw(canvas)
    banner.update()

def keydown(key):
    if key == simplegui.KEY_MAP['left']:
        banner.vel[0] -= 1
    elif key == simplegui.KEY_MAP['right']:
        banner.vel[0] += banner.acc
                
def keyup(key):
    if key == simplegui.KEY_MAP['up']:
        banner.vel[1] -= 1
    elif key == simplegui.KEY_MAP['down']:
        banner.vel[1] += banner.acc
            
            
def timer_handler():
    new_colour = "#"
    for i in range(6):
        new_colour += random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9",
                                     "A", "B", "C", "D", "E", "F"])
    
    banner.colour = new_colour
    
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", FRAME_WIDTH, FRAME_HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
timer = simplegui.create_timer(500, timer_handler)

# Start the frame animation
banner = Banner("ayy lmao", [50,250], "blue", 24, [1,1], 1)
inp = frame.add_input('Change message', message_handler, 100)
frame.add_button("Confirm", click_message_change)

frame.start()
timer.start()
