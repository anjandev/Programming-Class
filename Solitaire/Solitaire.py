# Solitaire Game by Anjan Momi

import simplegui
import random

# Link to sets http://imgur.com/dEoEdBG,rjCP3uF,HfL7T9o,B0PojjI

# Classes
class Card:

    def __init__(self, location, suit, value, exposed, exposedimg, cardnum, colour, LOC_BACK_X, LOC_BACK_Y):
        self.location = location
        self.suit = suit
        self.value = value
        self.exposed = exposed
        self.exposedimg = exposedimg
        self.cardnum = cardnum
        self.LOC_BACK_X = LOC_BACK_X
        self.LOC_BACK_Y = LOC_BACK_Y
        self.colour = colour
    
    def __str__(self):
        return str(self.suit) + " " + str(self.value)
    
    # Getters
    def get_exposed(self):
        return self.exposed
    
    def get_exposedimg(self):
        return self.exposedimg
    
    def get_cardnum(self):
        return self.cardnum
    
    def get_LOC_BACK_X(self):
        return self.LOC_BACK_X
    
    def get_LOC_BACK_Y(self):
        return self.LOC_BACK_Y
    
    def get_colour(self):
        return self.colour
    
    def get_val(self):
        return self.value
    
    def get_location(self):
        return self.location
    
    def get_cardfront(self, canvas):
        
        CARDWIDTH = 167
        CARDHEIGHT = 243
        DRAWSCALE = 0.5
        
        CARD_SPOT_IN_SETIMG = self.cardnum
        LOC_BACK_X = self.LOC_BACK_X
        LOC_BACK_Y = self.LOC_BACK_Y
        
        SET = self.exposedimg
            
        return canvas.draw_image(SET, (CARDWIDTH / 2 + CARDWIDTH * CARD_SPOT_IN_SETIMG, CARDHEIGHT / 2), 
                     (CARDWIDTH, CARDHEIGHT), 
                     (LOC_BACK_X, LOC_BACK_Y), 
                     (CARDWIDTH * DRAWSCALE, CARDHEIGHT * DRAWSCALE))
    
    # Setters
    
    def set_location(self, location):
        self.location = location
        
    def set_exposed(self, exposed):
        self.exposed = exposed
    
    def set_X(self, LOC_BACK_X):
        self.LOC_BACK_X = LOC_BACK_X
        
    def set_Y(self, LOC_BACK_Y):
        self.LOC_BACK_Y = LOC_BACK_Y

   
# Global variables
layercolour_dic = {'red': 'black', 'black': 'red'}
layerval_dic = {'Ace': '2', '2': '3', '3': '4', '4': '5', '5': '6', '6':'7',
                '7':'8', '8':'9', '9': '10', '10': 'Joker', 'Joker' : 'Queen',
                'Queen': 'King'}

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

x = 0
y = 0
clickednum = 0
clickedlayer1 = " "
clickedlayer2 = " "

deckcard1 = 0
deckcard2 = 0
deckcard3 = 0

layercard1 = 0
layercard2 = 0
layercard3 = 0
layercard4 = 0
layercard5 = 0
layercard6 = 0
layercard7 = 0


# How many times the player has clicked the deck. So that 
# the same 3 cards everytime together when they click the
# deck unless they move something out the deck.
timesdecked = 0

spadesimg = simplegui.load_image("http://i.imgur.com/soZWEII.png")
diamondsimg = simplegui.load_image("http://i.imgur.com/rjCP3uF.png")
heartsimg = simplegui.load_image("http://i.imgur.com/HfL7T9o.png")
cloversimg = simplegui.load_image("http://i.imgur.com/dEoEdBG.png")


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

    definecards(diamondsstart, 'Diamonds', diamondsimg, "red")
    definecards(spadesstart, 'Spades', spadesimg, "black")
    definecards(heartsstart, 'Hearts', heartsimg, "red")
    definecards(cloversstart, 'Clovers', cloversimg, "black")
    
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
           
            
def definecards(deckstart, suit, setimg, colour):
    global deck, ranks
   
    for x in range(13):
        deck[x + deckstart] = Card("shuffled", suit, ranks[x], False, setimg, x, colour, 0, 0)
    
        
def shuffle():
    global deck, shuffled
    
    for card in deck:
        shuffled.append(card)
    random.shuffle(shuffled)

    
def drawlayer(layer, layernum, canvas):
    
    for card in range(len(layer)):
        
        DRAWSCALE = 1.25
        DIST_FROM_LAST = 25
        
        LOC_BACK_Y = 300
        
        LOC_BACK_Y = LOC_BACK_Y + DIST_FROM_LAST * card
        LOC_BACK_X = 100 * layernum
        
        if layer[card].exposed == False:
            draw_card_back(canvas, LOC_BACK_X, LOC_BACK_Y)
            
        else:
            CARDWIDTH = 167
            CARDHEIGHT = 243
            
            layer[card].set_X(LOC_BACK_X)
            layer[card].set_Y(LOC_BACK_Y)
            
            SET = layer[card].exposedimg
            CARD_SPOT_IN_SETIMG = layer[card].cardnum
            layer[card].get_cardfront(canvas)

            
def draw_new_set_from_deck(canvas):
    global cards_shown
    
    LOC_BACK_X = 100
    LOC_BACK_Y = 75
   
    for card in range(len(cards_shown)):
        LOC_BACK_X += 100
        cards_shown[card].get_cardfront(canvas)
        cards_shown[card].set_X(LOC_BACK_X)
        cards_shown[card].set_Y(LOC_BACK_Y)

        
def click_new_set_from_deck():
    global x, y, location_in_deck, cards_shown
    
    TOPLEFTDECK_Y = 19
    TOPLEFTDECK_X = 59
    
    BOTTOMRIGHTDECK_Y = 131
    BOTTOMRIGHTDECK_X = 143
    
    LOC_BACK_Y = 75
    LOC_BACK_X = 100 
    
        
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
                for cards in cards_shown:
                    cards_shown[card].set_X("deck")
                    cards_shown[card].set_Y("deck")
                
                cards_shown = []
                # Add if else statement here when the feature to move cards
                # out of the deck is added. Potential bug
                for x in range(3):
                    cards_shown.append(shuffled[x + location_in_deck])
                    cards_shown[x].set_exposed(True)
        else:
            pass
    else:
        pass 
    
    
def draw_card_back(canvas, LOC_BACK_X, LOC_BACK_Y):
    
    SET = simplegui.load_image('http://i.imgur.com/p6hCw9U.png')
    CARDWIDTH = SET.get_width()
    CARDHEIGHT = SET.get_height()
    DRAWSCALE = 1.2
            
    return canvas.draw_image(SET, (CARDWIDTH /2 , CARDHEIGHT / 2), 
                     (CARDWIDTH, CARDHEIGHT), 
                     (LOC_BACK_X, LOC_BACK_Y), 
                     (CARDWIDTH * DRAWSCALE, CARDHEIGHT * DRAWSCALE))


def check_if_click_on_layer(layer, layernum):
    global y, x, clickedlayer1, clickednum, clickedlayer2
    global clickedlayernum1, clickedlayernum2
    
    CARDWIDTH = 85 / 2
    CARDHEIGHT = 125 / 2
    
    if len(layer) > 0:
        DIST_FROM_LAST = 25
        LOC_BACK_Y = 277
        
        LOC_BACK_Y = LOC_BACK_Y + DIST_FROM_LAST * len(layer)
        LOC_BACK_X = 100 * layernum
        
        topleft_X = LOC_BACK_X - CARDWIDTH
        topleft_Y = LOC_BACK_Y - CARDHEIGHT
        
        bottomright_X = LOC_BACK_X + CARDWIDTH
        bottomright_Y = LOC_BACK_Y + CARDHEIGHT
        
        if bottomright_X > x > topleft_X:
            if bottomright_Y > y > topleft_Y:
                if clickednum == 0:
                    if layer[-1].get_exposed() == True:
                        clickedlayer1 = layer
                        clickednum = 1
                    else:
                        layer[-1].set_exposed(True)
                else:
                    if layer[-1].get_exposed() == True:
                        clickedlayer2 = layer
                        clickednum = 0  
                    else:
                        layer[-1].set_exposed(True)

    
def put_in_series():
    global clickedlayer1, clickedlayer2, layercolour_dic, layerval_dic

    if clickedlayer2 == " ":
        pass
    
    else:
        # This fixes bug when the same card is clicked twice
        if clickedlayer1[-1].get_val() != clickedlayer2[-1].get_val():
            card1colour = clickedlayer1[-1].get_colour()
            card2colour = clickedlayer2[-1].get_colour()
        
            card1val = clickedlayer1[-1].get_val()
            card2val = clickedlayer2[-1].get_val()
        
            if layercolour_dic[card1colour] == card2colour:            
                if layerval_dic[card1val] == card2val:
                    clickedlayer2.append(clickedlayer1[-1])
                    clickedlayer1.pop()
                    clickedlayer1 = " "
                    clickedlayer2 = " "
                
            elif layercolour_dic[card2colour] == card1colour:
                if layerval_dic[card2val] == card1val:
                    clickedlayer1.append(clickedlayer2[-1])
                    clickedlayer2.pop()
                    clickedlayer1 = " "
                    clickedlayer2 = " "

        
        
def click_on_cards_from_deck():
    global cards_shown, clickednum, x, y
    
    CARDWIDTH = 84 / 2
    CARDHEIGHT = 125 / 2
    
    if len(cards_shown) > 0:
        START_X = 101
        START_Y = 76
        
        DIST_BETWEEN = 100
        
        for t in range(len(cards_shown)):
            START_X += DIST_BETWEEN


            card_top = START_Y - CARDHEIGHT
            card_bot = START_Y + CARDHEIGHT
        
            card_left = START_X - CARDWIDTH
            card_right = START_X + CARDWIDTH
                        
            if card_left < x < card_right:
                if card_top < y < card_bot:
                    print "it works"

                    
# Event Handlers

def draw_handler(canvas):
    global layer1, layer2, layer3, layer4, layer5, layer6, layer7 
    global DRAWSCALE, deck, cards_shown
    
    # Drawing Deck
    LOC_BACK_Y = 75
    LOC_BACK_X = 100
    draw_card_back(canvas, LOC_BACK_X, LOC_BACK_Y)
    
    drawlayer(layer1, 1, canvas)
    drawlayer(layer2, 2, canvas)
    drawlayer(layer3, 3, canvas)
    drawlayer(layer4, 4, canvas)
    drawlayer(layer5, 5, canvas)
    drawlayer(layer6, 6, canvas)
    drawlayer(layer7, 7, canvas)
    
    draw_new_set_from_deck(canvas)
    
    
def mouse_handler(position):
    global x, y, layer1, layer2, layer3, layer4, layer5, layer6, layer7
    
    x = position[0]
    y = position[1]
    
    click_new_set_from_deck()
    
    check_if_click_on_layer(layer1, 1)
    check_if_click_on_layer(layer2, 2)
    check_if_click_on_layer(layer3, 3)
    check_if_click_on_layer(layer4, 4)
    check_if_click_on_layer(layer5, 5)
    check_if_click_on_layer(layer6, 6)
    check_if_click_on_layer(layer7, 7)
    
    put_in_series()
    
    click_on_cards_from_deck()
    
def button_handler():
    pass
    
# Make Frame
frame = simplegui.create_frame('Solitaire', 1000, 850)
frame.set_canvas_background('Green')
restart = frame.add_button('Retart', button_handler, 50)


# Call Event Handlers
frame.set_draw_handler(draw_handler)
frame.set_mouseclick_handler(mouse_handler)

# Start Frame and Timers
main()
frame.start()
