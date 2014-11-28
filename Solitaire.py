# Solitaire Game by Anjan Momi

import simplegui
import random

# Link to sets http://imgur.com/dEoEdBG,rjCP3uF,HfL7T9o,B0PojjI

# Classes
class Card:

    def __init__(self, location, suit, value, exposed, exposedimg, cardnum, unexposedimg):
        self.location = location
        self.suit = suit
        self.value = value
        self.exposed = exposed
        self.exposedimg = exposedimg
        self.cardnum = cardnum
        self.unexposedimg = unexposedimg
    
    def __str__(self):
        return self.value + " of " + self.suit + ". It's location is" + self.location + ". Exposed:" + self.exposed + "Exposed image is:" + self.exposedimg + " Cardnum:" + str(self.cardnum) + "unexposedimg:" + self.unexposedimg
        
# Global variables
ranks = ("King", "Queen", "Joker", "10", "9", "8", "7", "6", "5", "4", "3", "2", "Ace")
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

# Where the rank starts in the deck
diamonds = 0
spades = 13
hearts = 26
clovers = 39

# Link to a set's images. These might need quotes. Bugs
diamondsimg = "http://i.imgur.com/rjCP3uF.png"
spadesimg = "http://i.imgur.com/B0PojjI.png"
heartsimg = "http://i.imgur.com/HfL7T9o.png"
cloversimg = "http://i.imgur.com/dEoEdBG.png"

# Helper Functions
def main():
    global deck, shuffled, diamonds, spades, hearts, clovers
    global diamondsimg, spadesimg, heartsimg, cloversimg
    
    makedeck()
    
    definecards(diamonds, "diamonds", diamondsimg)
    definecards(spades, "spades", spadesimg)
    definecards(hearts, "hearts", heartsimg)
    definecards(clovers, "clovers", cloversimg)
    
    shuffle()
    
    assign_loc(1, layer1)
    assign_loc(2, layer2)
    assign_loc(3, layer3)
    assign_loc(4, layer4)
    assign_loc(5, layer5)
    assign_loc(6, layer6)
    assign_loc(7, layer7)
    
def assign_loc(numofcards, layer):
    global shuffled
    
    for x in range(numofcards):
        layer.append(shuffled[x])
        # To-do change location of card that was appended
        shuffled.pop(0)

def makedeck():
    global ranks, suits, deck, shuffled
    
    for suit in suits:
        for rank in ranks:
            print rank + suit
            deck.append(rank + suit)
            
def definecards(deckstart, suit, setimg):
    global deck, ranks
    # Width of a set's picture
    imgwidth = 2179
    # Width of one card. This might create a bug
    CARDWIDTH = 167
    CARDLENGTH = 243
    DRAWSCALE = 1
    # IMAGE = simplegui.load_image(setimg)    
    
    for x in range(13):
        deck[x + deckstart] = Card("shuffled", suit, ranks[x], "no", setimg, x, "http://i.imgur.com/7yg05Co.png")
        
    
def shuffle():
    global deck, shuffled
    
    for card in deck:
        shuffled.append(card)
        
    random.shuffle(shuffled)
    
    
# Event Handlers

# Make Frame

# Call Event Handlers

# Start Frame and Timers

main()
