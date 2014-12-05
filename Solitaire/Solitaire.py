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
    
    def get_cardfront(self, canvas, side, LOC_BACK_X, LOC_BACK_Y):
        
        CARDWIDTH = 167
        CARDHEIGHT = 243
        CARD_SPOT_IN_SETIMG = self.cardnum
        DRAWSCALE = 0.5
        
        if side == "front":
            SET = self.exposedimg
            # TODO make this work if back is selected (change pic to back)
        elif side == "back":
            SET = simplegui.load_image('http://i.imgur.com/p6hCw9U.png')
            CARDWIDTH = SET.get_width()
            CARDHEIGHT = SET.get_height()
            DRAWSCALE = 1.2
            
        return canvas.draw_image(SET, (CARDWIDTH / 2 + CARDWIDTH * CARD_SPOT_IN_SETIMG, CARDHEIGHT / 2), 
                     (CARDWIDTH, CARDHEIGHT), 
                     (LOC_BACK_X, LOC_BACK_Y), 
                     (CARDWIDTH * DRAWSCALE, CARDHEIGHT * DRAWSCALE))
        
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

cards_shown = []

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

location_in_deck = 0 

x1 = 0
x2 = 0 
y1 = 0
y2 = 0
clicknum = 0

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
    
    print deck[0]
    
    
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
    
    for cards in range(len(layer)):
        BACK = simplegui.load_image('http://i.imgur.com/p6hCw9U.png')
        BACKWIDTH = BACK.get_width()
        BACKHEIGHT = BACK.get_height()
        LOC_BACK_Y = 300
        LOC_BACK_X = 100 * layernum
        DRAWSCALE = 1.25
        DIST_FROM_LAST = 25
        LOC_BACK_Y = LOC_BACK_Y + DIST_FROM_LAST * cards
        
        if layer[cards].exposed == False:
            # Because the back for all cards is the same, I can use any 
            # card from my list of cards(the deck) to draw the back.
            # Thats why I chose deck[0]. It's completely abritrary.
            deck[0].get_cardfront(canvas, "back", LOC_BACK_X, LOC_BACK_Y)
            
        else:
            # Width of one card. This might create a bug
            CARDWIDTH = 167
            CARDHEIGHT = 243
            SET = layer[cards].exposedimg
            CARD_SPOT_IN_SETIMG = layer[cards].cardnum
            
            layer[cards].get_cardfront(canvas, "front", LOC_BACK_X, LOC_BACK_Y)
            
            
def draw_new_set_from_deck(canvas):
    global cards_shown
    
    LOC_BACK_X = 100
    LOC_BACK_Y = 75
   
    for card in range(len(cards_shown)):
        LOC_BACK_X += 85
        cards_shown[card].get_cardfront(canvas, "front", LOC_BACK_X, LOC_BACK_Y)

        
def click_new_set_from_deck():
    global x1, y1, x2, x1, location_in_deck, cards_shown
    
    TOPLEFTDECK_Y = 19
    TOPLEFTDECK_X = 59
    
    BOTTOMRIGHTDECK_Y = 131
    BOTTOMRIGHTDECK_X = 143
    
    LOC_BACK_Y = 75
    LOC_BACK_X = 100 
    
    if clicknum == 1:
        x = x1
        y = y1
    else:
        x = x2
        y = y2
        
    # Check if player has clicked on the deck
    if BOTTOMRIGHTDECK_X > x > TOPLEFTDECK_X:
        if BOTTOMRIGHTDECK_Y > y > TOPLEFTDECK_Y:
            
            location_in_deck += 3
            
            cards_shown = []
            
            num_of_cards = len(shuffled)
            
            if location_in_deck == num_of_cards:
                location_in_deck = 0
                cards_shown = []
                
            else:
                cards_shown = []
                # Add if else statement here when the feature to move cards
                # out of the deck is added. Potential bug
                for x in range(3):
                    cards_shown.append(shuffled[x + location_in_deck])
        else:
            pass
    else:
        pass  


# Event Handlers

def draw_handler(canvas):
    global layer1, layer2, layer3, layer4, layer5, layer6, layer7 
    global DRAWSCALE, deck, cards_shown
    
    # Drawing Deck
    LOC_BACK_Y = 75
    LOC_BACK_X = 100
    deck[0].get_cardfront(canvas, "back", LOC_BACK_X, LOC_BACK_Y)
    
    drawlayer(layer1, 1, canvas)
    drawlayer(layer2, 2, canvas)
    drawlayer(layer3, 3, canvas)
    drawlayer(layer4, 4, canvas)
    drawlayer(layer5, 5, canvas)
    drawlayer(layer6, 6, canvas)
    drawlayer(layer7, 7, canvas)
    
    draw_new_set_from_deck(canvas)
    
    
def mouse_handler(position):
    global x1, x2, y1, y2, clicknum

    # To play need to select a card and then click on what you
    # where you want to put it. This allows us to keep track
    # of what was selected (x1/y1) and where it was put(x2/y2).
    
    if clicknum == 0:
        x1 = position[0]
        y1 = position[1]
        clicknum = 1
    elif clicknum == 1:
        x2 = position[0]
        y2 = position[1]
        clicknum = 0
        
    click_new_set_from_deck()
        

# Make Frame
frame = simplegui.create_frame('Solitaire', 1000, 850)
frame.set_canvas_background('Green')

# Call Event Handlers
frame.set_draw_handler(draw_handler)
frame.set_mouseclick_handler(mouse_handler)

# Start Frame and Timers
main()
frame.start()
