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
# logic dictionaries so program knows whether it can put two cards in the same
# layer, top, etc
layercolour_dic = {'red': 'black', 'black': 'red'}
layerval_dic = {'Ace': '2', '2': '3', '3': '4', '4': '5', '5': '6', '6':'7',
                '7':'8', '8':'9', '9': '10', '10': 'Joker', 'Joker' : 'Queen',
                'Queen': 'King', 'blank': 'Ace' }

ranks = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Joker", "Queen", "King")
suits = ("Diamonds", "Spades", "Hearts", "Clovers")

deck = []
shuffled = []

cards_shown = []
set_to_append = []

layer1 = []
layer2 = []
layer3 = []
layer4 = []
layer5 = []
layer6 = []
layer7 = []

top0 = []
top1 = []
top2 = []
top3 = []

location_in_deck_add = 3
location_in_deck = 0

x = 0
y = 0

card1 = " "
card2 = " "

CARDWIDTH = 85 / 2
CARDHEIGHT = 125 / 2

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
    # Initializing function
    # Assigns each card to a layer. 
    global shuffled, Cards
    
    for x in range(numofcards):
        layer.append(shuffled[0])
        # To-do change location of card that was appended
        shuffled[0].set_location(layer)
        shuffled.pop(0)

      
def makedeck():
    # Initializing function
    # Makes cards so I dont have to write out each of the 52 cards.
    global ranks, suits, deck, shuffled
    
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)
           
            
def definecards(deckstart, suit, setimg, colour):
    # Initializing function
    # Defines all of the 52 cards to it's own class
    global deck, ranks
   
    for x in range(13):
        deck[x + deckstart] = Card(shuffled, suit, ranks[x], False, setimg, x, colour, 0, 0)
    
        
def shuffle():
    global deck, shuffled
    # Initializing function
    # Shuffles deck.
    
    for card in deck:
        shuffled.append(card)
    random.shuffle(shuffled)

    
def drawlayer(layer, layernum, canvas):
    # GUI function
    # Draws each of the layers.
    
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

            
def assign_new_cards_to_show_from_deck():
    # GUI Backend Function
    # Adds cards from the deck to cards_show list. 
    # Since two functions need to know what cards are shown from the deck
    #(drawing shown cards and selecting shown cards) this must be a seperate modular function.
    global x, y, location_in_deck, cards_shown, shuffled
    
    TOPLEFTDECK_Y = 19
    TOPLEFTDECK_X = 59
    
    BOTTOMRIGHTDECK_Y = 131
    BOTTOMRIGHTDECK_X = 143
    
        
    # Check if player has clicked on the deck
    if BOTTOMRIGHTDECK_X > x > TOPLEFTDECK_X:
        if BOTTOMRIGHTDECK_Y > y > TOPLEFTDECK_Y:
                
            cards_shown = []
            # Since the number of cards in deck are changing (because we are taking 
            # them out. The len(cards_shown) will not always be a multiple of 3. 
            # Therefore, we must adapt how many cards we add to cards_shown 
            # in order to ensure that we dont cause an error to show.
            
            if location_in_deck + 3 <= len(shuffled):
                adding = 3
            elif location_in_deck + 2 <= len(shuffled):
                adding = 2
            elif location_in_deck + 1 <= len(shuffled):
                adding = 1
            else:
                location_in_deck = 0
                adding = 0
                cards_shown = []
                                         
            for x in range(adding):
                cards_shown.append(shuffled[x + location_in_deck])
                cards_shown[x].set_exposed(True)
            
            # location in deck keeps track of where we are in the deck. Ie. When after
            # we run this function once we will no longer wanna show the first 3 cards
            # again but instead show the 3 cards after the first 3 cards.
            location_in_deck = location_in_deck + adding          
            
            
def show_new_cards_from_deck (canvas):
    # GUI function
    # Draws each card from the cards_shown list.
    global cards_shown
    
    LOC_BACK_X = 100
    LOC_BACK_Y = 75
   
    for card in range(len(cards_shown)):
        LOC_BACK_X += 100
        cards_shown[card].get_cardfront(canvas)
        cards_shown[card].set_X(LOC_BACK_X)
        cards_shown[card].set_Y(LOC_BACK_Y)

        
def draw_card_back(canvas, LOC_BACK_X, LOC_BACK_Y):
    # GUI function
    # If a card is not supposed to be exposed this function is called. It draws a 
    # simple graphic of a card back. 
    SET = simplegui.load_image('http://i.imgur.com/p6hCw9U.png')
    CARDWIDTH = SET.get_width()
    CARDHEIGHT = SET.get_height()
    DRAWSCALE = 1.2
            
    return canvas.draw_image(SET, (CARDWIDTH /2 , CARDHEIGHT / 2), 
                     (CARDWIDTH, CARDHEIGHT), 
                     (LOC_BACK_X, LOC_BACK_Y), 
                     (CARDWIDTH * DRAWSCALE, CARDHEIGHT * DRAWSCALE))


def click_on_last_card_in_layer(layer, layernum):
    # GUI Backend Function
    # Checks if user has clicked the last card in the layer as specified 
    # and assigns card1 or card2 to the card selected by user.
    global y, x, card1, card2, CARDWIDTH, CARDHEIGHT

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
                if card1 == " ":
                    if layer[-1].get_exposed() == True:
                        card1 = layer[-1]
                    else:
                        layer[-1].set_exposed(True)
                        
                elif card2 == " ":
                    if layer[-1].get_exposed() == True:
                        card2 = layer[-1]
                    else:
                        layer[-1].set_exposed(True)

    
def check_if_2_cards_compatible():
    # GUI Backend Function
    # Checks if the two cards the user has selected are compatible.
    global layercolour_dic, layerval_dic, card1, card2, shuffled 
    global layer1, layer2, layer3, layer4, layer5, layer6, layer7, set_to_append

    if card2 == " ":
        pass
    # I honestly don't know what this does but Im too scared that Itll  break 
    # my program if I take it out.
    elif card1 == str(card1):
        pass
    # fixes bug where if two kings are clicked the game crashes.
    elif card1.get_val() == card2.get_val():
        card1 = " "
        card2 = " "
    else:
        card1colour = card1.get_colour()
        card2colour = card2.get_colour()
        
        card1val = card1.get_val()
        card2val = card2.get_val()
        
        if layerval_dic[card1val] == card2val:
            if layercolour_dic[card1colour] == card2colour:  
                # This if else statement checks if the user is trying to move multiple 
                # cards or just one card. If multiple cards are needing to be moved
                # the following function is played.
                if card1.get_location()[-1] != card1 and card1.get_location() != shuffled:
                    card1_location = card1.get_location()
                    
                    for cards in set_to_append:
                        card2.get_location().append(cards)
                        card1_location.remove(cards)
                        cards.set_location(card2.get_location())
                        
                    card1 = " "
                    card2 = " "
                # If only one card is needing to be moved the following function is played.    
                else:
                    card2.get_location().append(card1)
                    card1.get_location().remove(card1)
                    card1.set_location(card2.get_location())
                    card1 = " "
                    card2 = " "
               
        
def click_on_cards_from_deck():
    # GUI Backend Function
    # Checks if cards shown from the deck are clicked and selects them 
    # for checking for compatibility
    global cards_shown, x, y, card1, card2, CARDWIDTH, CARDHEIGHT
    
    if len(cards_shown) > 0:
        START_X = 101
        START_Y = 76
        
        DIST_BETWEEN = 100
        
        for selectedcard in range(len(cards_shown)):
            START_X += DIST_BETWEEN

            card_top = START_Y - CARDHEIGHT
            card_bot = START_Y + CARDHEIGHT
        
            card_left = START_X - CARDWIDTH
            card_right = START_X + CARDWIDTH
                        
            if card_left < x < card_right:
                if card_top < y < card_bot:
                    if card1 == " ":
                        card1 = cards_shown[selectedcard]
                    elif card2 == " ":
                        card2 = cards_shown[selectedcard]
                    
                    
def moving_sets(layer, layernum):
    # GUI Backend Function
    # Only the top of each exposed card is shown when put into a set. This function 
    # checks if the tops of each exposed card is clicked and puts the cards in that set
    # into it's own list so other functions can manipulate it.
    global x, y, card1, card2, set_to_append, CARDWIDTH
    
    if len(layer) > 0:
        DIST_FROM_LAST = 26
        
        LOC_BACK_X = 100 * layernum
        left_X = LOC_BACK_X - CARDWIDTH
        right_X = LOC_BACK_X + CARDWIDTH
        
        START_bottom = 266
        START_top = 244
        
        if right_X > x > left_X:
            # Finds which card has been clicked and excludes the last card since
            # we have a seperate function for moving one card to one card.
            for cardloc in range((len(layer) - 1)):
                bottom = START_bottom + DIST_FROM_LAST * cardloc
                top = START_top + DIST_FROM_LAST * cardloc
                if top < y and y < bottom: 
                    if card1 == " ":
                        if layer[cardloc].get_exposed() == True:
                            card1 = layer[cardloc]
                            set_to_append = []
                    
                            set_start = card1.get_location().index(card1)
                            card1_location = card1.get_location()
                    
                            for card in range(len(card1_location) - set_start):
                                set_to_append.append(card1_location[card + set_start])
                       
                    # DELETE THIS. OR BUG        
                    #elif card2 == " ":
                        #if layer[cardloc].get_exposed() == True:
                            #card2 = layer[cardloc]

                            
def move_to_top_layers():
    # GUI Backend Function
    # Takes a card that the user wishes to move to a top, checks if that card is compatible 
    # with the last card in the top and appends it to that top if compatible. 
    global x, y, top0, top1, top2, top3, card1, card2, layerval_dic
    global shuffled, layer1, layer2, layer3, layer4, layer5, layer6 
    global layer7, cards_shown
    
    CARDWIDTH = 84 / 2
    CARDHEIGHT = 125 / 2
    
    START_X = 500
    START_Y = 76
        
    DIST_BETWEEN = 100
    
    tops = [top0, top1, top2, top3]
            
    for numtop in range(len(tops)):
        X_CARD_MID = START_X + DIST_BETWEEN * numtop

        card_top = START_Y - CARDHEIGHT
        card_bot = START_Y + CARDHEIGHT
        
        card_left = X_CARD_MID - CARDWIDTH
        card_right = X_CARD_MID + CARDWIDTH
        
        if card1 == " " and card2 == " ":
            break
            
        if card_left < x and x < card_right:
            if card_top < y and y < card_bot: 
                if card2 == " " and card1 != " ":
                    card2 = card1
                    card1 = " "
                        
                card2colour = card2.get_colour()
                card2val = card2.get_val()
                                
                if len(tops[numtop]) == 0:
                    card1val = 'blank'
                    card1colour = card2.get_colour()
                else:
                    card1 = tops[numtop][-1]
                    card1colour = card1.get_colour()
                    card1val = card1.get_val()
                
                if layerval_dic[card1val] == card2val:
                    if card1colour == card2colour: 
                        tops[numtop].append(card2)
                        card2.get_location().remove(card2)
                        card2.set_location(tops[numtop])
                        if card2 in cards_shown:
                            cards_shown.remove(card2)
                        elif card1 in cards_shown:
                            cards_shown.remove(card1)
                        card1 = " "
                        card2 = " "
                
def clear_cards():
    # Backend Function
    # clears selected cards and set to append at the end if they are found to not be 
    # compatible
    global card1, card2, set_to_append
    
    if card1 != " " and card2 != " ":
        card1 = " "
        card2 = " "
    set_to_append = []
                    
def draw_tops(canvas):
    # GUI function
    # Draws black squares to represent tops and also draws the last card in that top
    global top0, top1, top2, top3
    
    TOPBACK = simplegui.load_image('http://i.imgur.com/MOQhHbc.png')
    CARDWIDTH = TOPBACK.get_width()
    CARDHEIGHT = TOPBACK.get_height()
    DRAWSCALE = 1.1
    
    LOC_BACK_Y = 76
        
    START_X = 500
    DIST_BETWEEN = 100
    
    top_dict = [top0, top1, top2, top3]  
    
    for tops in range(4):
            
        LOC_BACK_X =START_X + DIST_BETWEEN * tops
        
        canvas.draw_image(TOPBACK, (CARDWIDTH /2 , CARDHEIGHT / 2), 
                     (CARDWIDTH, CARDHEIGHT), 
                     (LOC_BACK_X, LOC_BACK_Y), 
                     (CARDWIDTH * DRAWSCALE, CARDHEIGHT * DRAWSCALE))        
        
        if len(top_dict[tops]) > 0: 
            top_dict[tops][-1].set_X(LOC_BACK_X)
            top_dict[tops][-1].set_Y(LOC_BACK_Y)
            
            SET = top_dict[tops][-1].exposedimg
            CARD_SPOT_IN_SETIMG = top_dict[tops][-1].cardnum
            top_dict[tops][-1].get_cardfront(canvas)

            
def move_to_empty_layer():
    # GUI backend function
    # Allows user to move a set or a card to an empty layer.
    global layer1, layer2, layer3, layer4, layer5, layer6, layer7
    global set_to_append, card1, card2
    
    layers = [layer1, layer2, layer3, layer4, layer5, layer6, layer7]
    
    for layernum in range(len(layers)):
        LOC_BACK_X = 100 + 100 * layernum
        LOC_BACK_Y = 300
        
        CARDWIDTH = 84 / 2
        CARDHEIGHT = 125 / 2
        
        topleft_X = LOC_BACK_X - CARDWIDTH
        topleft_Y = LOC_BACK_Y - CARDHEIGHT
        
        bottomright_X = LOC_BACK_X + CARDWIDTH
        bottomright_Y = LOC_BACK_Y + CARDHEIGHT
        
        if topleft_X < x < bottomright_X:
            if topleft_Y < y < bottomright_Y:
                if len(layers[layernum]) == 0:
                    if len(set_to_append) == 0:
                        layers[layernum].append(card1)
                        card1.get_location().remove(card1)
                        card1.set_location(layers[layernum])
                        card1 = " "
                        card2 = " "
                    else:
                        card1location = set_to_append[0].get_location()
                        
                        for card in set_to_append:
                            layers[layernum].append(card)
                            card1location.remove(card)
                            card.set_location(layers[layernum])
                        card1 = " "
                        card2 = " "
                        set_to_append = []
            
                        
# Event Handlers

def draw_handler(canvas):
    global layer1, layer2, layer3, layer4, layer5, layer6, layer7 
    global DRAWSCALE, deck, cards_shown
    
    # Drawing Deck
    LOC_BACK_Y = 75
    LOC_BACK_X = 100
    draw_card_back(canvas, LOC_BACK_X, LOC_BACK_Y)
    
    draw_tops(canvas)
    
    drawlayer(layer1, 1, canvas)
    drawlayer(layer2, 2, canvas)
    drawlayer(layer3, 3, canvas)
    drawlayer(layer4, 4, canvas)
    drawlayer(layer5, 5, canvas)
    drawlayer(layer6, 6, canvas)
    drawlayer(layer7, 7, canvas)
    
    show_new_cards_from_deck(canvas)
    
    
def mouse_handler(position):
    global x, y, layer1, layer2, layer3, layer4, layer5, layer6, layer7, card1, card2
    
    x = position[0]
    y = position[1]
    
    assign_new_cards_to_show_from_deck()
    
    click_on_last_card_in_layer(layer1, 1)
    click_on_last_card_in_layer(layer2, 2)
    click_on_last_card_in_layer(layer3, 3)
    click_on_last_card_in_layer(layer4, 4)
    click_on_last_card_in_layer(layer5, 5)
    click_on_last_card_in_layer(layer6, 6)
    click_on_last_card_in_layer(layer7, 7)
    
    moving_sets(layer1, 1)
    moving_sets(layer2, 2)
    moving_sets(layer3, 3)
    moving_sets(layer4, 4)
    moving_sets(layer5, 5)
    moving_sets(layer6, 6)
    moving_sets(layer7, 7)
    
    click_on_cards_from_deck()
    
    move_to_top_layers()

    check_if_2_cards_compatible()
    move_to_empty_layer()
    clear_cards()
    
def button_handler():
    pass
    
# Make Frame
frame = simplegui.create_frame('Solitaire', 1000, 850)
frame.set_canvas_background('Green')
restart = frame.add_button('Restart', button_handler, 60)


# Call Event Handlers
frame.set_draw_handler(draw_handler)
frame.set_mouseclick_handler(mouse_handler)

# Start Frame and Timers
main()
frame.start()
