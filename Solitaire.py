# Solitaire Game by Anjan Momi

import simplegui
import random

# Link to sets http://imgur.com/dEoEdBG,rjCP3uF,HfL7T9o,B0PojjI
# Current bugs. Layer 2 draw repeats 4 times
# Layer 3 draw repeats 9
# My card width probably go off the end of the set.
# Missing Cards: 6 of spades
# 8 of spades
# 2 of spades
# Queen of spades
# 5 of spades

# Classes
class Card:

    def __init__(self, location, suit, value, exposed, exposedimg, cardnum):
        self.location = location
        self.suit = suit
        self.value = value
        self.exposed = exposed
        self.exposedimg = exposedimg
        self.cardnum = cardnum
    
    def __str__(self):
        return self.value + " of " + self.suit + ". It's location is" + self.location + ". Exposed:" + str(self.exposed) + ". Exposed image is:" + str(self.exposedimg) + " Cardnum:" + str(self.cardnum)
       
    # Getters
    def get_exposed(self):
        return self.exposed
    
    def get_exposedimg(self):
        return self.exposedimg
    
    def get_cardnum(self):
        return self.cardnum
        
    # Setters
    
    def set_location(self, location):
        self.location = location
        
    def set_exposed(self, exposed):
        self.exposed = exposed
        
   
# Global variables
ranks = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Joker", "Queen", "King")
suits = ("Diamonds", "Spades", "Hearts", "Clovers")
deck = []
shuffled = []

layer1 = []
layer2 = []
layer3 = []
layer4 = []
layer5 = []
layer6 = []
layer7 = []

top1 = []
top2 = []
top3 = []
top4 = []

# How many times the player has clicked the deck. So that 
# the same 3 cards everytime together when they click the
# deck unless they move something out the deck.
timesdecked = 0

spadesimg = simplegui.load_image("http://i.imgur.com/soZWEII.png")
diamondsimg = simplegui.load_image("http://i.imgur.com/rjCP3uF.png")
heartsimg = simplegui.load_image("http://i.imgur.com/HfL7T9o.png")
cloversimg = simplegui.load_image("http://i.imgur.com/dEoEdBG.png")


# Where the rank starts in the deck. Made changes. May cause bugs.

# Helper Functions
def main():
    global deck, shuffled, diamonds, spades, hearts, clovers
    global layer1, layer2, layer3, layer4, layer5, layer6
    global layer7, spadesimg, diamondsimg, heartsimg, cloversimg
    
    makedeck()
    
    ranklen = 13
    diamondsstart = 0 * ranklen
    spadesstart = 1 * ranklen
    heartsstart = 2 * ranklen
    cloversstart = 3 * ranklen
    

    definecards(diamondsstart, 'Diamonds', diamondsimg)
    definecards(spadesstart, 'Spades', spadesimg)
    definecards(heartsstart, 'Hearts', heartsimg)
    definecards(cloversstart, 'Clovers', cloversimg)
    
    shuffle()
    
    assign_loc(1, layer1, "layer1")
    layer1[-1].set_exposed(True)
    assign_loc(2, layer2, "layer2")
    layer2[-1].set_exposed(True)
    assign_loc(3, layer3, "layer3")
    layer3[-1].set_exposed(True)
    assign_loc(4, layer4, "layer4")
    layer4[-1].set_exposed(True)
    assign_loc(5, layer5, "layer5")
    layer5[-1].set_exposed(True)
    assign_loc(6, layer6, "layer6")
    layer6[-1].set_exposed(True)
    assign_loc(7, layer7, "layer7")
    layer7[-1].set_exposed(True)
    
    
def assign_loc(numofcards, layer, name_of_layer):
    global shuffled, Cards
    
    for x in range(numofcards):
        layer.append(shuffled[0])
        # To-do change location of card that was appended
        shuffled[0].set_location(name_of_layer)
        shuffled.pop(0)

      
def makedeck():
    global ranks, suits, deck, shuffled
    
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)
           
            
def definecards(deckstart, suit, setimg):
    global deck, ranks

    print suit
    
    for x in range(13):
        print deck[x + deckstart]
        print [x + deckstart]
        deck[x + deckstart] = Card("shuffled", suit, ranks[x], False, setimg, x)

        
def shuffle():
    global deck, shuffled
    
    for card in deck:
        shuffled.append(card)

    random.shuffle(shuffled)

    
def drawlayer(layer, layernum, canvas):
    BACK = simplegui.load_image('http://i.imgur.com/p6hCw9U.png')
    
    for cards in range(len(layer)):
        BACKWIDTH = BACK.get_width()
        BACKHEIGHT = BACK.get_height()
        LOC_BACK_Y = 300
        LOC_BACK_X = 100 * layernum
        DRAWSCALE = 1.25
        DIST_FROM_LAST = 25
        
        if layer[cards].exposed == False:
            canvas.draw_image(BACK, (BACKWIDTH / 2, BACKHEIGHT / 2), 
                     (BACKWIDTH, BACKHEIGHT), 
                     (LOC_BACK_X, LOC_BACK_Y + DIST_FROM_LAST * cards), 
                     (BACKWIDTH * DRAWSCALE, BACKHEIGHT * DRAWSCALE))
        else:
            # Width of one card. This might create a bug
            CARDWIDTH = 167
            CARDHEIGHT = 243
            SET = layer[cards].exposedimg
            CARD_SPOT_IN_SETIMG = layer[cards].cardnum
            
            canvas.draw_image(SET, (CARDWIDTH / 2 + CARDWIDTH * CARD_SPOT_IN_SETIMG, CARDHEIGHT / 2), 
                     (CARDWIDTH, CARDHEIGHT), 
                     (LOC_BACK_X, LOC_BACK_Y + DIST_FROM_LAST * cards), 
                     (BACKWIDTH * DRAWSCALE, BACKHEIGHT * DRAWSCALE))
            
def draw_new_set_from_deck(canvas):
    global shuffled
    for cards in shuffled:
        pass
    
            
# Event Handlers
# Use a getter for this
#image = simplegui.load_image('http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg')

def draw_handler(canvas):
    global layer1, layer2, layer3, layer4, layer5, layer6, layer7
    
    # Drawing Deck
    BACK = simplegui.load_image('http://i.imgur.com/p6hCw9U.png')
    BACKWIDTH = BACK.get_width()
    BACKHEIGHT = BACK.get_height()
    LOC_BACK_Y = 75
    LOC_BACK_X = 100
    DRAWSCALE = 1.25

    canvas.draw_image(BACK, (BACKWIDTH / 2, BACKHEIGHT / 2), 
                     (BACKWIDTH, BACKHEIGHT), 
                     (LOC_BACK_X, LOC_BACK_Y), 
                     (BACKWIDTH * DRAWSCALE, BACKHEIGHT * DRAWSCALE))
    
    drawlayer(layer1, 1, canvas)
    drawlayer(layer2, 2, canvas)
    drawlayer(layer3, 3, canvas)
    drawlayer(layer4, 4, canvas)
    drawlayer(layer5, 5, canvas)
    drawlayer(layer6, 6, canvas)
    drawlayer(layer7, 7, canvas)
    
def mouse_handler(position):
    x = position[0]
    y = position[1]
    
    TOPLEFTDECK_Y = 19
    TOPLEFTDECK_X = 59
    
    BOTTOMRIGHTDECK_Y = 131
    BOTTOMRIGHTDECK_X = 143
    
    # Check if player click on deck
    if BOTTOMRIGHTDECK_X > x > TOPLEFTDECK_X:
        if BOTTOMRIGHTDECK_Y > y > TOPLEFTDECK_Y:
            pass
        else:
            pass
    else:
        pass
    
    
# Make Frame
frame = simplegui.create_frame('Solitaire', 1000, 850)
frame.set_canvas_background('Green')
frame.set_draw_handler(draw_handler)
frame.set_mouseclick_handler(mouse_handler)

# Call Event Handlers

# Start Frame and Timers
main()

frame.start()
