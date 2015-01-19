# A program that draws a background image on the canvas 
# with a banner message over it that streams across the 
# bottom.  

import simplegui

FRAME_WIDTH = 300
FRAME_HEIGHT = 300

class Banner:
    def __init__(self, message, pos, colour, size, vel):
       self.message = message
       self.pos = pos
       self.colour = colour
       self.size = size
       self.vel = vel
        
    def draw(self,canvas):
        canvas.draw_text(self.message, self.pos, self.size, self.colour)
        
    def update(self):
        # x += v
        for i in range(2):
            self.pos[i] += self.vel[i]
        self.pos[0] = self.pos[0] % FRAME_WIDTH
        
    def set_text(self, new_message):
        if len(new_message) > 0:
            self.message = new_message
    
# Handler for mouse click
def message_handler(text_input):
    pass

def click_message_change():
    banner.set_text(inp.get_text())  

# Handler to draw on canvas
def draw(canvas):
    banner.draw(canvas)
    banner.update()
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", FRAME_WIDTH, FRAME_HEIGHT)
frame.set_draw_handler(draw)

# Start the frame animation
banner = Banner("Hello World", [50,250], "blue", 24, [2,0])
inp = frame.add_input('Change message', message_handler, 100)
frame.add_button("Confirm", click_message_change)

frame.start()
