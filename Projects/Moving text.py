# A program that draws a background image on the canvas with a banner
# message over it that streams across the bottom.

import simplegui
import random

FRAME_WIDTH = 700
FRAME_HEIGHT = 700


class Background: 
    # Added background class
    
    def __init__(self, image):
        self.image = simplegui.load_image(image)
        while self.image.get_width() == 0:
            pass
        self.width = self.image.get_width() 
        self.height = self.image.get_height()
        self.draw_scaleX = FRAME_WIDTH // self.width
        self.draw_scaleY = FRAME_HEIGHT // self.height
        
    def draw(self, canvas):
        LOC_BACK_X = self.width / 2
        LOC_BACK_Y = self.height / 2

        canvas.draw_image(self.image, (self.width / 2, self.height / 2 ), 
                     (self.width, self.height), 
                     (LOC_BACK_X * self.draw_scaleX, LOC_BACK_Y * self.draw_scaleY), 
                     (self.width * self.draw_scaleX, self.height * self.draw_scaleY))
        
    def set_background(self, image):
        self.image = simplegui.load_image(image)
        while self.image.get_width() == 0:
            pass
        self.width = self.image.get_width() 
        self.height = self.image.get_height()
        self.draw_scaleX = FRAME_WIDTH // self.width
        self.draw_scaleY = FRAME_HEIGHT // self.height

class Banner:
    def __init__(self, message, pos, colour, size, vel, acc, bounce):
       self.message = message
       self.pos = pos
       self.colour = colour
       self.size = size
       self.vel = vel
       self.acc = acc
       self.bounce = bounce

    def draw(self,canvas):
        canvas.draw_text(self.message, self.pos, self.size, self.colour)

    def update(self):
        # x += v
        for i in range(2):
            self.pos[i] += self.vel[i]

        if self.bounce == True:
            if frame.get_canvas_textwidth(self.message, self.size) + self.pos[0] >= FRAME_WIDTH:
                self.vel[0] = self.vel[0] * -1

            if self.pos[0] <= 0:
                self.vel[0] = self.vel[0] * -1

            if self.pos[1] - 10 <= 0:
                self.vel[1] = self.vel[1] * -1

            if self.pos[1] >= FRAME_HEIGHT:
                self.vel[1] = self.vel[1] * -1

        elif self.bounce == False:
            self.pos[0] = self.pos[0] % FRAME_WIDTH
            self.pos[1] = self.pos[1] % FRAME_HEIGHT

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

    def set_bounce(self, bounce):
        self.bounce = bounce

    def get_bounce(self):
        return self.bounce

# Handler for mouse click
def message_handler(text_input):
    pass

def background_handler(text_input):
    # Added text field to change the background
    background.set_background(text_input)

def click_message_change():
    # Text input box to change message
    banner.set_text(inp.get_text())

def bounce_change():
    # Additional button that change movement in
    # different ways (bounce off edge of canvas,
    # move diagonally, etc.)
    if banner.get_bounce():
        banner.set_bounce(False)
    else:
        banner.set_bounce(True)

# Handler to draw on canvas
def draw(canvas):
    background.draw(canvas)
    banner.draw(canvas)
    banner.update()
    
def keydown(key):
    # Key down handler and key up handler to change
    # speed
    if key == simplegui.KEY_MAP['left']:
        banner.vel[0] -= 1
    elif key == simplegui.KEY_MAP['right']:
        banner.vel[0] += banner.acc

def keyup(key):
    # Increase Speed up or down. Additional.
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
banner = Banner("ayy lmao", [50,250], "blue", 24, [1,1], 1, False)
background = Background("http://mario.nintendo.com/img/mario_logo.png")
inp = frame.add_input('Change message:', message_handler, 100)
inp2 = frame.add_input('Change background:',background_handler, 100)
frame.add_button("Confirm", click_message_change)
frame.set_canvas_background('White')
frame.add_button("Change Movement", bounce_change)

frame.start()
timer.start()
