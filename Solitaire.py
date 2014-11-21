# Solitaire Game by Anjan Momi

import simplegui
import random


def assign_loc(num, list):
    global shuffled
    
    for x in range(num):
        list.append(shuffled[x])
        shuffled.pop(x)

# Classes
class Card:

    def __init__(self, varname, name, location, suit, value):
        self.varname = varname
        self.name = name
        self.location = location
        self.suit = suit
        self.value = value
    
    def picture(self):
        self.image

# Global variables
base_cards = ("King", "Queen", "Joker", "10", "9", "8", "7", "6", "5", "4", "3", "2", "Ace")
suited = (" of Diamonds", " of Spades", " of Hearts", " of Clovers")
cards = ()

variables = []
shuffled = []

deck = []

deck1 = []
deck2 = []
deck3 = []
deck4 = []
deck5 = []
deck6 = []
deck7 = []

top1 = []
top2 = []
top3 = []
top4 = []

for x in range(52):
    x = str(x)
    variables.append("card" + x)

for x in range(52):
    shuffled.append(variables[x])

random.shuffle(shuffled)

# Clean this up with a for loop
assign_loc(1, deck1)
assign_loc(2, deck2)
assign_loc(3, deck3)
assign_loc(4, deck4)
assign_loc(5, deck5)
assign_loc(6, deck6)
assign_loc(7, deck7)

for x in range(52):
    



# Helper Functions



# Event Handlers

# Make Frame

# Call Event Handlers

# Start Frame and Timers
