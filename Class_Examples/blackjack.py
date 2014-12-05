# Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables: 
# boolean in_play, strings player_message and dealer_message
in_play = False

player_message = ''
dealer_mesasge = ''

# define globals for cards:
# tuples for suits and ranks
# dictionary of values
SUITS = ('C','S','H','D')

RANKS = ('A','2','3','4','5','6',
         '7','8','9','10','J','Q','K')

VALUES = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}



# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid Card:", suit, rank
            
            
    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    
    #Position is top left corner of card
    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] + RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))

        canvas.draw_image(card_images,
                          card_loc,
                          CARD_SIZE,
                          [pos[0]+ CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                          CARD_SIZE)
        
card1 = Card('D','3')
card2 = Card('H','5')
hand = Hand[]
hand.add_card(card1)

# define hand class
class Hand:
    def __init__(self):
        self.cards = []
        
        
    def __str__(self):
        s = ''
    	
        for card in self.cards:
            s += str(card) + ' '
        
        return s
    
    def add_card(self, card):
        self.cards.append(card)
        
    def get_value(self):
        pass
        
    def draw(self, canvas, pos):
        pass
        
        
# define deck class 
class Deck:
    def __init__(self):
        pass
    
    def shuffle(self):
        pass
    
    def deal_card(self):
        pass
    
    def __str__(self):
        pass
    
#define event handlers for buttons

#count deal in the middle of a round as a forfeit
#initialize deck
#initialize hands
#add cards to hands

def deal():
    pass

# if the hand is in play, deal a card to player's hand
# if busted, update message and in_play status
def hit():
    pass
       
# if hand is in play, repeatedly hit dealer until 
# his hand has value 17 or more
# update message and in_play
def stand():
    pass
    
        
# draw handler    
def draw(canvas):
    card.draw(canvas, [50,50])

# initialize frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and callbacks
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()
