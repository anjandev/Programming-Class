# Solitaire Game by Anjan Momi

import simplegui
import random

# Classes
class Card:

    def __init__(self, location, suit, value, exposed):
        self.location = location
        self.suit = suit
        self.value = value
        self.exposed = exposed
    
    def __str__(self):
        return self.value + " of " + self.suit
        
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


# Helper Functions
def main():
    global deck, shuffled
    
    makedeck()
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
    
    for rank in ranks:
        for suit in suits:
            print rank + suit
            deck.append(rank + suit)
            # To-do Assign card images
            deck[-1] = Card("shuffled", suit, rank, "no")

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
