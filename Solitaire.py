# Solitaire Game by Anjan Momi

import simplegui
import random


def assign_loc(numofcards, layer):
    global shuffled
    
    for x in range(numofcards):
        layer.append(shuffled[x])
        shuffled[x] = Card(layer, suit, rank, "no")
        shuffled.pop(0)
        
# Classes
class Card:

    def __init__(self, location, suit, value, exposed):
        self.location = location
        self.suit = suit
        self.value = value
        self.exposed = exposed
    
    def __str__(self):
        return self.value + self.suit
        
# Global variables
ranks = ("King", "Queen", "Joker", "10", "9", "8", "7", "6", "5", "4", "3", "2", "Ace")
suits = (" of Diamonds", " of Spades", " of Hearts", " of Clovers")
deck = []

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

for rank in ranks:
    for suit in suits:
        deck.append(rank + suit)
        
shuffled = deck
random.shuffle(shuffled)


for card in shuffled:
    card = Card(shuffled, suit, rank, "no")
    
print shuffled

assign_loc(1, layer1)
assign_loc(2, layer2)
assign_loc(3, layer3)
assign_loc(4, layer4)
assign_loc(5, layer5)
assign_loc(6, layer6)
assign_loc(7, layer7)


print layer1
print layer2
print layer3
print layer4


    


# Helper Functions



# Event Handlers

# Make Frame

# Call Event Handlers

# Start Frame and Timers
