# Solitaire Game by Anjan Momi
# THIS GAME HAS UNSOLVABLE BUGS. PLEASE READ THIS:
# https://github.com/anjandev/Programming-Class/wiki/Solitaire

import simplegui
import random

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
    
    def get_name(self):
        return str(self.value) + " of " + str(self.suit)
    
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
    
    def get_suit(self):
        return self.suit
    
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
                'Queen': 'King', 'blank': 'Ace' }

ranks = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Joker", "Queen", "King")
suits = ("Diamonds", "Spades", "Hearts", "Clovers")

# This list temproraly holds all cards (in order of ranks) before they are shuffled.
deck = []

# Once cards are shuffled and initially appended to their own layers this list
# holds all "left over" cards (aka the dealer's deck)
shuffled = []

# This list holds the cards that are shown from the deck at a time. Everytime
# the deck gui element is clicked, the next 3 cards from the deck are shown.
cards_shown = []
# When the deck is clicked, this variable tracks which cards the player
# has already seen
location_in_deck = 0

# When multiple cards are selected to move, this list holds all the 
# cards that were selected to move
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

# Where the player has clicked (the x and y coordinates)
x = 0
y = 0

# Holds the first and second card that was clicked by the user
card1 = " "
card2 = " "


spadesimg = simplegui.load_image("http://i.imgur.com/soZWEII.png")
diamondsimg = simplegui.load_image("http://i.imgur.com/rjCP3uF.png")
heartsimg = simplegui.load_image("http://i.imgur.com/HfL7T9o.png")
cloversimg = simplegui.load_image("http://i.imgur.com/dEoEdBG.png")


# Helper Functions
def main():
    # This function holds all the functions needed to initialize the game.
    global deck, shuffled, diamonds, spades, hearts, clovers
    global layer1, layer2, layer3, layer4, layer5, layer6
    global layer7, spadesimg, diamondsimg, heartsimg, cloversimg
    
    makedeck()
    
    # The deck list's first 13 cards are diamonds. After those 13 cards the spades
    # start. This calculates where to start the defining of each of the suits.
    ranklen = 13
    diamondsstart = 0 * ranklen
    spadesstart = 1 * ranklen
    heartsstart = 2 * ranklen
    cloversstart = 3 * ranklen

    # Since each of the suits have similar attributes (their image, their colour
    # and where they start in the deck list) we can use a function to define
    # each of them instead of defining each of the 52 cards.
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
    
#### Main function helpers ####
def makedeck():
    # Combines the 13 suits and 4 ranks and puts them into a list so that
    # I can automate the defining of the classes.
    global ranks, suits, deck, shuffled
    
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)


def definecards(deckstart, suit, setimg, colour):
    # Defines each of the cards based on their rank

    global deck, ranks
   
    for x in range(13):
        deck[x + deckstart] = Card(shuffled, suit, ranks[x], False, setimg, x, colour, 0, 0)


def shuffle():
    # Copies cards to a seperate list(shuffled) and shuffles them. Shuffled (list) becomes the new deck.
    global deck, shuffled
    
    for card in deck:
        shuffled.append(card)
    random.shuffle(shuffled)


def assign_loc(numofcards, layer, name_of_layer):
    # Lets say the 3rd layer needs 3 cards. This function will take the first 
    # 3 cards from the shuffled list and append them to the 3rd layer. This 
    # function also removes them from shuffled so that shuffled can act as a deck. 
    global shuffled
    
    for x in range(numofcards):
        layer.append(shuffled[0])
        # To-do change location of card that was appended
        shuffled[0].set_location(layer)
        shuffled.pop(0)
#### END OF Main function helpers ####
     
### Drawing function helpers ###

def draw_card_back(canvas, LOC_BACK_X, LOC_BACK_Y):
    # returns a graphic that represents the back of a card

    SET = simplegui.load_image('http://i.imgur.com/p6hCw9U.png')
    CARDWIDTH = SET.get_width()
    CARDHEIGHT = SET.get_height()
    DRAWSCALE = 1.2
            
    return canvas.draw_image(SET, (CARDWIDTH /2 , CARDHEIGHT / 2), 
                     (CARDWIDTH, CARDHEIGHT), 
                     (LOC_BACK_X, LOC_BACK_Y), 
                     (CARDWIDTH * DRAWSCALE, CARDHEIGHT * DRAWSCALE))

    
def drawlayer(layer, layernum, canvas):
    # Draws each of the cards in the layer. If the card is not exposed, it 
    # calls the draw_card_back function
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

            
def draw_shown_cards(canvas):
    # Draws cards in the cards_shown list. 
    # cards_shown holds the current cards that are shown from the deck.
    global cards_shown
    
    LOC_BACK_X = 100
    LOC_BACK_Y = 75
   
    for card in range(len(cards_shown)):
        LOC_BACK_X += 100
        cards_shown[card].get_cardfront(canvas)
        cards_shown[card].set_X(LOC_BACK_X)
        cards_shown[card].set_Y(LOC_BACK_Y)

    
def draw_tops(canvas):
    # Draws the blank tops and if the length of the top is greater 
    # than 0 it draws the last card in the top
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
        # BUG.
        if len(top_dict[tops]) > 0: 
            top_dict[tops][-1].set_X(LOC_BACK_X)
            top_dict[tops][-1].set_Y(LOC_BACK_Y)
            
            SET = top_dict[tops][-1].exposedimg
            CARD_SPOT_IN_SETIMG = top_dict[tops][-1].cardnum
            top_dict[tops][-1].get_cardfront(canvas)
### END OF Drawing function helpers ###

### Clicking/Backend function helpers ###    
def show_new_cards_from_deck():
    # Checks if the player clicks on the deck gui element.
    # If true, it appends new cards to cards_shown from the 
    # deck.
    
    global x, y, location_in_deck, cards_shown, shuffled
    
    TOPLEFTDECK_Y = 19
    TOPLEFTDECK_X = 59
    
    BOTTOMRIGHTDECK_Y = 131
    BOTTOMRIGHTDECK_X = 143
    
    LOC_BACK_Y = 75
    LOC_BACK_X = 100 
    
        
    # Check if player has clicked on the deck
    if BOTTOMRIGHTDECK_X > x > TOPLEFTDECK_X:
        if BOTTOMRIGHTDECK_Y > y > TOPLEFTDECK_Y:
                
            cards_shown = []
            
            # Since cards are removed from the deck we cant always
            # show in multiples of 3. This if else calculates the
            # maximum number of cards we can show before showing 
            # more than are in the deck. 
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
                                         
            # Add if else statement here when the feature to move cards
            # out of the deck is added. Potential bug
            for x in range(adding):
                cards_shown.append(shuffled[x + location_in_deck])
                cards_shown[x].set_exposed(True)
                
            location_in_deck = location_in_deck + adding


def last_card_in_layer_select(layer, layernum):
    # Allows user to select the last card in a layer
    global y, x, card1, card2
    
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

    
def check_cards_and_move():
    # A "glueing" function. This function checks if the card2 can be moved to card1
    # according to solitaire rules and moves them. If card1 is more than one card
    # then it moves all the cards in the set to card2's location
    global layercolour_dic, layerval_dic, card1, card2, shuffled 
    global layer1, layer2, layer3, layer4, layer5, layer6, layer7, set_to_append
    global cards_shown

    if card2 == " ":
        pass
    elif card1 == str(card1):
        pass
    # fixes bug where if two kings are clicked the game crashes.
    elif card1.get_val() == card2.get_val():
        card1 = " "
        card2 = " "
        pass
    else:
        card1colour = card1.get_colour()
        card2colour = card2.get_colour()
        
        card1val = card1.get_val()
        card2val = card2.get_val()
        if layerval_dic[card1val] == card2val:
            if layercolour_dic[card1colour] == card2colour:  
                if card1.get_location()[-1] != card1 and card1.get_location() != shuffled:
                    card1_location = card1.get_location()
                    
                    for cards in set_to_append:
                        card2.get_location().append(cards)
                        card1_location.remove(cards)
                        cards.set_location(card2.get_location())
                        
                    card1 = " "
                    card2 = " "
                    set_to_append = []
                    
                else:
                    card2.get_location().append(card1)
                    card1.get_location().remove(card1)
                    card1.set_location(card2.get_location())
                    if card1 in cards_shown:
                        cards_shown.remove(card1)
                        
                    card1 = " "
                    card2 = " "
               
        
def check_click_on_cardsshown():
    # checks if the player has clicked on a card that was shown from the 
    # shuffled deck and selects that card.
    global cards_shown, x, y, card1, card2
    
    CARDWIDTH = 84 / 2
    CARDHEIGHT = 125 / 2
    
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
                    
                    
def select_multiple_cards_to_move(layer, layernum):
    # Allows the player to select multiple cards to be moved. 
    global x, y, card1, card2, set_to_append
    
    CARDWIDTH = 85 / 2
    
    if len(layer) > 0:
        DIST_FROM_LAST = 26
        
        
        LOC_BACK_X = 100 * layernum
        left_X = LOC_BACK_X - CARDWIDTH
        right_X = LOC_BACK_X + CARDWIDTH
        
        START_bottom = 266
        START_top = 244
        
        if right_X > x > left_X:
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
                       
                            
                    elif card2 == " ":
                        if layer[cardloc].get_exposed() == True:
                            card2 = layer[cardloc]
                            # bug here

                            
def move_to_top_layers():
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
                    card1suit = card2.get_suit()
                else:
                    card1 = tops[numtop][-1]
                    card1suit = card1.get_suit()
                    card1val = card1.get_val()
                
                if layerval_dic[card1val] == card2val:
                    if card1suit == card2.get_suit(): 
                        tops[numtop].append(card2)
                        card2.get_location().remove(card2)
                        card2.set_location(tops[numtop])
                        
                        # removes cards from cards_shown so the draw function
                        # doesnt keep drawing them. 
                        if card2 in cards_shown:
                            cards_shown.remove(card2)
                        elif card1 in cards_shown:
                            cards_shown.remove(card1)
                            
                        card1 = " "
                        card2 = " "
                
                            
def move_to_empty_layer():
    # Allows the player to move a card or a group of cards to an empty layer
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
        if card1 == " ":
            pass
        elif topleft_X < x < bottomright_X:
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
            
            
def clear_cards():
    # If a pair of cards fail all the tests then it is cleared by this function
    global card1, card2
    
    if card1 != " " and card2 != " ":
        card1 = " "
        card2 = " "
        
def check_if_win(canvas):
    global top0, top1, top2, top3
    
    if len(top0) == 13 and len(top1) == 13 and len(top2) == 13 and len(top3) == 13:
        canvas.draw_text("You win!", [275,575],60, "black")
### END OF Clicking/Backend function helpers ###    

    
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
    
    draw_shown_cards(canvas)
    
    if card1 != " ":
        canvas.draw_text("Card1: " + card1.get_name(), [275,700],20, "black")
    
    check_if_win(canvas)
    
def mouse_handler(position):
    global x, y, layer1, layer2, layer3, layer4, layer5, layer6, layer7, card1, card2
    
    x = position[0]
    y = position[1]
    
    show_new_cards_from_deck()
    
    last_card_in_layer_select(layer1, 1)
    last_card_in_layer_select(layer2, 2)
    last_card_in_layer_select(layer3, 3)
    last_card_in_layer_select(layer4, 4)
    last_card_in_layer_select(layer5, 5)
    last_card_in_layer_select(layer6, 6)
    last_card_in_layer_select(layer7, 7)
    
    select_multiple_cards_to_move(layer1, 1)
    select_multiple_cards_to_move(layer2, 2)
    select_multiple_cards_to_move(layer3, 3)
    select_multiple_cards_to_move(layer4, 4)
    select_multiple_cards_to_move(layer5, 5)
    select_multiple_cards_to_move(layer6, 6)
    select_multiple_cards_to_move(layer7, 7)
    
    check_click_on_cardsshown()
    
    move_to_top_layers()

    check_cards_and_move()
    move_to_empty_layer()
    clear_cards()
    
    
# Make Frame
frame = simplegui.create_frame('Solitaire', 1000, 850)
frame.set_canvas_background('Green')

# Call Event Handlers
frame.set_draw_handler(draw_handler)
frame.set_mouseclick_handler(mouse_handler)

# Start Frame and Timers
main()
frame.start()
